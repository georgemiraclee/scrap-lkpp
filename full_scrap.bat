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
