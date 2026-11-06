import os
import time

print("YouTube Otomasyon Botu Başlatıldı...")
# API anahtarları kontrolü
gemini_key = os.getenv("GEMINI_API_KEY")
youtube_key = os.getenv("YOUTUBE_API_KEY")

if not gemini_key or not youtube_key:
    print("Uyarı: API anahtarları eksik! Lütfen Render panelinden ekleyin.")
else:
    print("API anahtarları başarıyla okundu.")

# Bot işlemleri burada gerçekleşecek
print("Video üretim süreci simüle ediliyor...")
time.sleep(2)
print("İşlem tamamlandı!")
