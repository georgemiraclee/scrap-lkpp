# Web Scraper dengan Selenium

## Cara Kerja Program

1. **Membuka Halaman Web:**
   - Program menerima URL sebagai input.
   - Selenium membuka halaman web yang diberikan.
   
2. **Mengatur Tampilan Data:**
   - Program mengubah tampilan data menjadi 100 item per halaman.
   
3. **Mengambil Data dari Halaman Utama:**
   - Mencari semua tautan yang sesuai dengan pola tertentu.
   
4. **Mengambil Data dari Halaman Detail:**
   - Untuk setiap tautan yang ditemukan:
     - Membuka tautan di tab baru.
     - Mengambil informasi dari tabel yang tersedia.
     - Menyimpan data dalam dictionary.
     - Menutup tab dan kembali ke halaman utama.
   
5. **Navigasi ke Halaman Berikutnya:**
   - Jika tombol "Next" tersedia, program akan mengkliknya dan mengulangi proses.
   
6. **Menyimpan Data:**
   - Setelah semua halaman selesai diproses, data disimpan dalam folder `data/` dalam format `.csv` dan `.xlsx`.

## How to Run

### Create Virtual Environment
#### Create `.venv` in Windows
```sh
python -m venv .venv
```

#### Create `.venv` in Linux
```sh
python3 -m venv .venv
```

### Activate Virtual Environment
#### Windows `(git bash)`:
```sh
source .venv\Scripts\activate
```
#### Linux/Mac:
```sh
source .venv/bin/activate
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Run the Program
#### Manual Execution:
```sh
python main.py -url "https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2014"
```

#### Running with Shell Script (`full_scrap.sh`):
```sh
#!/bin/bash

# Berhenti jika ada error
set -e

# Array of URLs
url_targets=(
    "https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2014"
    "https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2015"
    "https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2016"
    "https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2017"
    "https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2018"
    "https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2019"
    "https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2020"
    "https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2021"
    "https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2022"
    "https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2023"
    "https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2024"
)

for url in "${url_targets[@]}"; do
    echo "Scraping data from: $url"
    python main.py -url="$url"
done

echo "All URLs processed!"
```

#### Run the Script 
```sh
chmod +x run.sh
./run.sh
```

