# Traveloka Website Scraper
Program Python sederhana untuk melakukan scraping ulasan pengguna pada situs Traveloka

### Fungsi
Mengambil username, ulasan, rating dan waktu dari kolom reviews lalu menyimpannya kedalam file excel (.xlsx)

### Library
- Selenium
- Webdriver Manager
- Pandas
- Openpyxl
- BautifulSoup

### Cara Menggunakan
- Buat virtual environtment dan jalankan venv
```bash
python -m venv venv

venv\Scripts\activate      #Windows
source venv/bin/activate   #Linux & MacOS
```

- Install paket yang ada di requirements.txt
```
pip install -r requirements.txt
```

- Jalankan program
```
python traveloka_scraper.py
```

- Masukkan link review
- Masukkan nama file hasil scraping
- Jika muncul _human verification_ pada situs saat program dijalankan, selesaikan proses verifikasi
- File akan tersimpan di folder

## Disclaimer
> Projek ini tidak bertujuan untuk digunakan secara komersial, melainkan sebagai sarana pembelajaran saja
