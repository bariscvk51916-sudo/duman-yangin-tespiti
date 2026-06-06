# Duman ve Yangın Tespiti

Bu repo Dijital Görüntü Çözümleme dersi için yaptığım dönem projesi.

Projede amacım kameradan veya yüklenen bir fotoğraftan duman ve yangın olup olmadığını tespit etmek. Plaka tanıma örneğine benzer mantıkta ilerledim ama konu olarak yangın/duman seçtim çünkü güvenlik açısından daha anlamlı geldi.

Kullandığım araçlar:
- YOLO (ultralytics kütüphanesi) -> nesne tespiti
- OpenCV -> görüntü okuma
- Streamlit -> basit web arayüzü
- Veri seti -> Roboflow üzerinden indirdim

## Klasörler ne işe yarıyor

- `app/` -> streamlit arayüzü burada
- `src/` -> model ile tahmin yapan kod
- `data/` -> eğitim için kullandığım görseller (dosyalar büyük olduğu için githuba atmadım)
- `models/` -> eğittikten sonra best.pt dosyası buraya geliyor
- `notebooks/` -> colabda eğitim yaparken kullandığım notebook
- `configs/` -> dataset yaml dosyası

## Nasıl çalıştırılır

Önce gerekli paketleri kur:

```
pip install -r requirements.txt
```

Sonra arayüzü aç:

```
streamlit run app/streamlit_app.py
```

Tarayıcıda sayfa açılınca fotoğraf yüklüyorsun, sistem tespit ederse kutucuklarla gösteriyor.

Not: İlk aşamada models klasöründe best.pt yoksa program uyarı verir. Modeli colabda eğitip indirdikten sonra models klasörüne koymak gerekiyor.

## Model eğitimi (kısaca)

Bilgisayarımda ekran kartı olmadığı için eğitimi Google Colab'da yaptım. Roboflow'dan YOLO formatında veri indirdim, notebooktaki adımları takip ettim. Eğitim bitince çıkan best.pt dosyasını projeye ekledim.

Raporda mAP, precision, recall gibi metrikleri ve eğitim sırasında oluşan grafikleri de kullandım.

## İletişim

Sorular için ders hocasına mail atılabilir: huseyinyanik@mersin.edu.tr
