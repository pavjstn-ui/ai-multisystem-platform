# src/quality/blur.py

import cv2
import numpy as np


def laplacian_variance(gray: np.ndarray) -> float:
    """
    Compute blur score using Laplacian variance.

    Why:
    - Simple
    - Fast
    - Industry standard baseline
    """
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    return float(lap.var())


def is_blurry(gray: np.ndarray, threshold: float) -> bool:
    """
    Decide if a frame is blurry.

    Why:
    - Keeps threshold logic in one place
    - Makes experimentation easy
    """
    return laplacian_variance(gray) < threshold
