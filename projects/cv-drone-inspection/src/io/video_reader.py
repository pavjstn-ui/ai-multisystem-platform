# src/io/video_reader.py

from pathlib import Path
from typing import Iterator, Tuple

import cv2


def open_video(video_path: Path) -> cv2.VideoCapture:
    """
    Open a video file and validate it.

    Why:
    - Centralized video opening logic
    - Easier to swap OpenCV backend later if needed
    """
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open video: {video_path}")
    return cap


def get_video_fps(cap: cv2.VideoCapture, fallback: float = 30.0) -> float:
    """
    Get FPS from video metadata.

    Why:
    - Some FPV videos report FPS = 0 or NaN
    - We must handle this safely
    """
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps is None or fps <= 0:
        return fallback
    return float(fps)


def iter_frames(
    cap: cv2.VideoCapture,
    fps: float
) -> Iterator[Tuple[int, float, any]]:
    """
    Iterate through frames yielding:
    (frame_index, timestamp_seconds, frame_bgr)

    Why:
    - Keeps timing logic consistent
    - Useful later for temporal aggregation
    """
    idx = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break

        time_sec = idx / fps
        yield idx, time_sec, frame
        idx += 1
