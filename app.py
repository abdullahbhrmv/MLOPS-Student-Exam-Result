import pandas as pd

# Verileri yükle
data = pd.read_csv("Original_data_with_more_rows.csv")

# Veri seti hakkında genel bilgi
print(data.info())

# Her sütunun istatistiklerini göster
print(data.describe())

# Eksik değerleri kontrol et
print(data.isnull().sum())

# Eksik değerleri ortalama ile doldur
data["MathScore"].fillna(data["MathScore"].mean(), inplace=True)
data["ReadingScore"].fillna(data["ReadingScore"].mean(), inplace=True)
data["WritingScore"].fillna(data["WritingScore"].mean(), inplace=True)

# Veri tipi hatalarını kontrol et
print(data.dtypes)

# Veri tiplerini düzelt
data["MathScore"] = data["MathScore"].astype(int)
data["ReadingScore"] = data["ReadingScore"].astype(int)
data["WritingScore"] = data["WritingScore"].astype(int)

# Gereksiz sütunları sil (örneğin, 'StudentID' sütunu)
if 'StudentID' in data.columns:
    data.drop(columns=['StudentID'], inplace=True)

# Verileri kaydet
data.to_csv("cleaned_data.csv", index=False)
