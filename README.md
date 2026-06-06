# duman-yangin-tespiti

Dijital görüntü çözümleme dersi dönem projem.

Fotoğraf yükleyince görüntüde duman veya yangın var mı diye bakıyor. Varsa ekranda kutu içinde gösteriyor. Hocanın derste anlattığı plaka sistemi gibi düşünülebilir ama ben yangın konusunu seçtim.

## ne kullandım

yolo ile nesne tespiti yaptım. görüntü işleme için opencv, arayüz için streamlit kullandım. veri setini roboflowdan indirdim çünkü hazır etiketli veri vardı orada.

## klasörler

app klasöründe streamlit dosyası var  
src klasöründe tespit kodu  
data klasörüne eğitim görselleri geliyor (githuba yüklemedim çok yer kaplıyor)  
models klasörüne eğitim bitince best.pt koyuluyor  
notebooks klasöründe colab için notebook var  

## çalıştırmak için

terminalde proje klasörüne gir sonra:

pip install -r requirements.txt

kurulum bitince:

streamlit run app/streamlit_app.py

komutunu yaz. tarayıcı açılıyor, oradan resim seçiyorsun.

models klasöründe henüz model yoksa uyarı çıkar, o normal. önce colabda eğitim yapıp best.pt indirmek lazım.

## model eğitimi

laptopda gpu olmadığı için google colab kullandım. roboflowdan yolov8 formatında zip indirdim, notebooks içindeki dosyayı colaba yükledim ve oradan eğittim. 

eğitim sonunda precision recall map falan çıkıyor zaten, onları rapora koydum. results.png ve confusion matrix görselini de ekledim.
