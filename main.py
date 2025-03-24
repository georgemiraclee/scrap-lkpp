from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import argparse
import os
import re

def main(url):
    print(f"Scraping dari URL: {url}")
    driver = Driver(uc=True)  # Gunakan mode undetected Chrome

    driver.get(url)
    time.sleep(5)  # Tunggu halaman termuat

    # List untuk menyimpan semua data sebagai dictionary
    data_list = []
    
    print("=== Mengambil Data dari Halaman Utama ===")
    select_num = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "//select[@name='tbllelang_length']"))
    )
    
    dropdown = Select(select_num)
    
    dropdown.select_by_value("100")
    
    time.sleep(5)

    while True:
        try:
            # Tunggu elemen muncul
            target_links = WebDriverWait(driver, 8).until(
                EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/eproc4/') and contains(@href, '/pengumumanlelang')]"))
            )

            for link in target_links:
                main_window = driver.current_window_handle
                href = link.get_attribute("href")

                # Buka link di tab baru
                driver.execute_script("window.open(arguments[0]);", href)
                time.sleep(2)

                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(2)

                print(f"\n=== Mengambil Data dari Halaman Baru ===")
                print(f"Title: {driver.title}")
                print(f"URL: {driver.current_url}\n")

                # Dictionary untuk menyimpan data dari 1 halaman
                data_dict = {
                    'year_url': url,
                    "URL": driver.current_url,
                    "Judul": driver.title
                }

                try:
                    # Tunggu tabel muncul
                    table = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.TAG_NAME, "table"))
                    )
                    tbody = table.find_element(By.TAG_NAME, "tbody")
                    rows = tbody.find_elements(By.TAG_NAME, "tr")

                    for row in rows:
                        col_names = row.find_elements(By.TAG_NAME, "th")
                        col_values = row.find_elements(By.TAG_NAME, "td")

                        for col_name, col_value in zip(col_names, col_values):
                            data_dict[col_name.text.strip()] = col_value.text.strip()

                    # print(data_dict)
                    data_list.append(data_dict)
                    
                    # break

                except Exception as e:
                    print("Tidak dapat mengambil isi halaman:", e)

                driver.close()
                driver.switch_to.window(main_window)

            # Cek tombol Next
            try:
                next_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.page-link[aria-label='Next']"))
                )
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
                time.sleep(1)

                # Klik tombol Next
                driver.execute_script("arguments[0].click();", next_button)
                print("Klik tombol Next")
                time.sleep(5)
                
                # break

            except Exception:
                print("Pagination selesai.")
                break  # Hentikan loop jika tidak ada tombol Next

        except Exception as e:
            print("Terjadi error dalam scraping:", e)
            break  # Hentikan loop jika error besar

    driver.quit()

    # Buat folder 'data' jika belum ada
    if not os.path.exists("data"):
        os.makedirs("data")

    # Simpan hasil ke CSV & Excel
    # file_name = f"data/scraping_{url.split('/')[-1]}"
    file_name = f"data/scraping_{re.sub(r'[^a-zA-Z0-9_-]', '_', url.split('/')[-1])}"
    df = pd.DataFrame(data_list)
    df.to_csv(f"{file_name}.csv", index=False, encoding="utf-8")
    df.to_excel(f"{file_name}.xlsx", index=False, engine='openpyxl')

    print(f"Data disimpan sebagai: {file_name}.csv dan {file_name}.xlsx")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape data dari sebuah URL.")

    # Argument untuk URL
    parser.add_argument("-url", type=str, required=True, help="URL yang akan di-scrape")

    # Parse argumen
    args = parser.parse_args()

    # Jalankan fungsi utama
    main(args.url)
