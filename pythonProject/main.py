import pandas as pd # Kullanacağımız kütüphaneleri projeye import ediyoruz.

dosya_yolu = r"C:\Users\shila\Downloads\YetGen_Mock_Data.xlsx" # Excel dosyasının yolunu belirtiyoruz.
df = pd.read_excel(dosya_yolu, sheet_name='MOCK_DATA.csv') # Excelde bulunan sheet ismini girerek sayfayı okumasını sağlıyoruz.
not_sutunlari = ['Not 1', 'Not 2', 'Not 3'] # Sayfada bulunan not sütunlarının isimlerini belirtiyoruz.
df['Toplam Puan'] = df[not_sutunlari].sum(axis=1) # Not sütunlarının değerlerini sum ile topluyoruz. axis=1 satır bazında işlem yapmak anlamına gelir.
df_filtre = df[df['Toplam Puan'] <= 100] # Toplam puanı 100'den fazla olmayan satırları seçiyoruz.
with pd.ExcelWriter(dosya_yolu, engine='openpyxl', mode='a') as writer: # Aynı dosya içine yeni bir sayfa ekleyerek verileri yeni sayfaya yazıyoruz. mode='a', mevcut dosyaya ekleme yapmamızı sağlar. Index=False, DataFrame'deki index sütununu Excel dosyasına yazmamamızı sağlar.
    df_filtre.to_excel(writer, sheet_name='Filtrelenmiş', index=False)
print("Filtrelenen veriler başarıyla yeni bir sayfaya yazıldı.") # Kod sonunda başarı ile tamamladığımızı anlamak amaçlı yazılmış satırdır.

