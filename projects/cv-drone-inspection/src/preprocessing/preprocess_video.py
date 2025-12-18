# src/preprocessing/preprocess_video.py

import argparse
import csv
from pathlib import Path

import cv2
import numpy as np

from src.io.video_reader import open_video, get_video_fps, iter_frames
from src.quality.blur import laplacian_variance


def apply_clahe(frame_bgr: np.ndarray) -> np.ndarray:
    """
    Normalize lighting using CLAHE on L channel.

    Why:
    - FPV footage has extreme lighting variation
    - CLAHE preserves local contrast
    """
    lab = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l2 = clahe.apply(l)

    lab = cv2.merge((l2, a, b))
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)


def preprocess_frame(
    frame: np.ndarray,
    width: int,
    height: int,
    denoise_strength: int
) -> tuple[np.ndarray, float]:
    """
    Apply preprocessing and return processed frame + blur score.
    """
    frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
    frame = apply_clahe(frame)

    frame = cv2.fastNlMeansDenoisingColored(
        frame, None,
        h=denoise_strength,
        hColor=denoise_strength,
        templateWindowSize=7,
        searchWindowSize=21
    )

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur_score = laplacian_variance(gray)

    return frame, blur_score


def main() -> None:
    parser = argparse.ArgumentParser(description="FPV video preprocessing pipeline")
    parser.add_argument("--video", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--target-fps", type=float, default=3.0)
    parser.add_argument("--width", type=int, default=640)
    parser.add_argument("--height", type=int, default=360)
    parser.add_argument("--blur-threshold", type=float, default=120.0)
    parser.add_argument("--denoise", type=int, default=6)

    args = parser.parse_args()

    video_path = Path(args.video)
    out_dir = Path(args.out)
    frames_dir = out_dir / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)

    cap = open_video(video_path)
    fps = get_video_fps(cap)

    step = max(1, int(round(fps / args.target_fps)))

    metadata_path = out_dir / "metadata.csv"
    with metadata_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "frame_index",
                "time_sec",
                "blur_score",
                "saved",
                "path"
            ]
        )
        writer.writeheader()

        for idx, time_sec, frame in iter_frames(cap, fps):
            if idx % step != 0:
                continue

            processed, blur = preprocess_frame(
                frame,
                args.width,
                args.height,
                args.denoise
            )

            keep = blur >= args.blur_threshold
            output_path = ""

            if keep:
                filename = f"frame_{idx:08d}.jpg"
                output_path = str(frames_dir / filename)
                cv2.imwrite(output_path, processed)

            writer.writerow({
                "frame_index": idx,
                "time_sec": round(time_sec, 4),
                "blur_score": round(blur, 2),
                "saved": int(keep),
                "path": output_path
            })

    cap.release()
    print("Preprocessing complete.")


if __name__ == "__main__":
    main()
