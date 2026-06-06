# Duman / Yangın Tespit Sistemi

Dijital Görüntü Çözümleme dönem projesi — YOLO ile duman ve yangın tespiti + Streamlit web arayüzü.

## Proje Konusu

**Problem:** Görüntülerde duman ve yangın bölgelerinin otomatik tespiti  
**Yöntem:** Ultralytics YOLO (nesne tespiti)  
**Arayüz:** Streamlit dashboard (görüntü yükle → sonuç göster)

## Klasör Yapısı

```
duman-yangin-tespiti/
├── app/                 # Streamlit arayüzü
├── configs/             # dataset.yaml
├── data/                # Veri seti (GitHub'a yüklenmez)
├── models/              # Eğitilmiş model (best.pt)
├── notebooks/           # Colab eğitim notebook'u
├── src/                 # Tespit kodu
└── requirements.txt
```

## Kurulum

```powershell
cd duman-yangin-tespiti
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Arayüzü Çalıştırma

```powershell
streamlit run app/streamlit_app.py
```

## Eğitim Akışı

1. Roboflow'dan veri seti indir (YOLOv8 formatı)
2. `notebooks/egitim_colab.ipynb` dosyasını Google Colab'da aç
3. Modeli eğit, metrikleri kaydet
4. `best.pt` dosyasını `models/` klasörüne kopyala

## Değerlendirme Metrikleri

Eğitim sonrası raporda şunlar yer almalı:

- mAP@50
- mAP@50-95
- Precision
- Recall
- Eğitim grafikleri (`results.png`, `confusion_matrix.png`)

## Geliştirici

Mersin Üniversitesi — Dijital Görüntü Çözümleme Final Projesi
