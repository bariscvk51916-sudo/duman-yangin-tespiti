from __future__ import annotations

from pathlib import Path
from typing import Any

import cv2
import numpy as np
from ultralytics import YOLO


DEFAULT_MODEL = Path(__file__).resolve().parent.parent / "models" / "best.pt"


def load_model(model_path: str | Path | None = None) -> YOLO:
    path = Path(model_path) if model_path else DEFAULT_MODEL
    if not path.exists():
        raise FileNotFoundError(
            f"Model bulunamadı: {path}\n"
            "Önce Colab'da modeli eğitip models/best.pt dosyasını buraya kopyalayın."
        )
    return YOLO(str(path))


def run_detection(
    image_bgr: np.ndarray,
    model: YOLO,
    conf: float = 0.35,
) -> tuple[np.ndarray, list[dict[str, Any]]]:
    results = model.predict(source=image_bgr, conf=conf, verbose=False)
    result = results[0]

    annotated = result.plot()
    detections: list[dict[str, Any]] = []

    if result.boxes is not None and len(result.boxes) > 0:
        names = result.names
        for box in result.boxes:
            cls_id = int(box.cls[0])
            score = float(box.conf[0])
            label = names.get(cls_id, str(cls_id))
            detections.append(
                {
                    "label": label,
                    "confidence": round(score, 3),
                    "bbox": box.xyxy[0].tolist(),
                }
            )

    return annotated, detections


def bgr_to_rgb(image_bgr: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
