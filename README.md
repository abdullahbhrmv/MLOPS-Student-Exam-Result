# MLOPS-Student-Exam-Result

## Amaç

Projenin amacı ve hedefi burada açıklanır. Hangi sorunu çözmeyi amaçladığınızı veya hangi ihtiyaca cevap verdiğinizi belirtin.

## Kurulum

### Gereksinimler

Projenin çalıştırılması için gerekli olan yazılım ve kütüphaneleri belirtin.

### Kurulum Adımları

1. Projeyi klonlayın: `git clone https://github.com/kullanıcı/mlops_odev`
2. Proje dizinine gidin: `cd mlops_odev`
3. Virtual environment oluşturun: `python -m venv venv`
4. Virtual environment'i etkinleştirin:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
5. Gerekli kütüphaneleri yükleyin: `pip install -r requirements.txt`
6. Veritabanını oluşturun: `python manage.py migrate`
7. Sunucuyu başlatın: `python manage.py runserver`

## Çalıştırma

1. Terminali açın.
2. Proje dizinine gidin: `cd mlops_odev`
3. Virtual environment'i etkinleştirin.
4. Sunucuyu başlatın: `python manage.py runserver`
5. Tarayıcıda http://localhost:8000 adresine gidin ve projenin çalışıp çalışmadığını kontrol edin.

## Kullanım

### Ana Sayfa

Ana sayfa, projenin temel işlevlerini ve projenin genel tanımını içerir.

- **URL:** http://localhost:8000
- **İçerik:** Model değerlendirmesi sonuçları, istatistikler, vb.
- ![main](image.png)

### Açıklama Sayfası

Açıklama sayfası, modelin açıklanabilirliğini gösteren SHAP grafiğini içerir.

- **URL:** http://localhost:8000/explain
- **İçerik:** Model açıklaması, SHAP grafiği
- ![/explain](image-1.png)

## MLOps Adımları

### Öğrenci Sınav Sonucu Verileri

1. Veri analizi ve istatistikler
2. Veri temizleme ve hazırlık

### MLOps Tasarım Kalıpları

1. Model tasarımı
2. Yazılım ürün tasarımı

### MLOps

1. Açıklanabilir yapay zeka teknikleri
2. Veri güvenliği
3. Sürekli entegrasyon
4. Sürekli ortam yüklemesi

## Katkıda Bulunma

Projenin geliştirilmesine nasıl katkıda bulunabileceklerini açıklayın. Pull request gönderme adımlarını belirtin.
