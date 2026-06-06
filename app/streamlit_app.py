from __future__ import annotations

import sys
from pathlib import Path

import cv2
import numpy as np
import streamlit as st
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.detect import bgr_to_rgb, load_model, run_detection

st.set_page_config(
    page_title="Duman / Yangın Tespiti",
    page_icon="🔥",
    layout="wide",
)

st.title("🔥 Duman ve Yangın Tespit Sistemi")
st.caption("YOLO tabanlı nesne tespiti — Dijital Görüntü Çözümleme Dönem Projesi")

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("1. Görüntü Yükle")
    uploaded = st.file_uploader(
        "Bir görüntü seçin (JPG, PNG)",
        type=["jpg", "jpeg", "png"],
    )
    confidence = st.slider("Güven eşiği", min_value=0.1, max_value=0.9, value=0.35, step=0.05)

with col_right:
    st.subheader("2. Tespit Sonucu")

    if uploaded is None:
        st.info("Başlamak için soldan bir görüntü yükleyin.")
    else:
        file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
        image_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        image_rgb = bgr_to_rgb(image_bgr)

        st.image(image_rgb, caption="Yüklenen görüntü", use_container_width=True)

        try:
            model = load_model()
            with st.spinner("Tespit yapılıyor..."):
                annotated_bgr, detections = run_detection(image_bgr, model, conf=confidence)

            annotated_rgb = bgr_to_rgb(annotated_bgr)
            st.image(annotated_rgb, caption="Tespit edilen bölgeler", use_container_width=True)

            st.subheader("3. Sonuç Özeti")
            if not detections:
                st.warning("Duman veya yangın tespit edilmedi.")
            else:
                for i, det in enumerate(detections, start=1):
                    st.success(
                        f"#{i} — Sınıf: **{det['label'].upper()}** | "
                        f"Güven: **{det['confidence']:.1%}**"
                    )
        except FileNotFoundError as exc:
            st.error(str(exc))
            st.markdown(
                """
                **Model henüz yok.** Sıradaki adım:
                1. Roboflow'dan veri setini indir
                2. Colab'da YOLO modelini eğit
                3. `best.pt` dosyasını `models/` klasörüne koy
                """
            )
