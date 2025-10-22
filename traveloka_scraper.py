from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Gunakan ChromeDriverManager untuk mengelola driver
def init_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Fungsi untuk Scraping
def scrape_reviews(driver, url):
    driver.get(url)
    
    # Tunggu halaman ulasan termuat
    time.sleep(20)

    # List untuk menyimpan data ulasan
    data = []

    while True:
        soup = BeautifulSoup(driver.page_source, "html.parser")

        review_section = soup.find("div", attrs={"data-testid": "review-list-container"})
        review_wrapper = review_section.find("div", class_="css-1dbjc4n r-6koalj r-1ssbvtb r-1pi2tsx r-x03415 r-bnwqim r-13qz1uu")
        reviews = review_wrapper.find_all("div", class_="css-1dbjc4n r-18u37iz r-1fdih9r")

        for review in reviews:
            # Ambil Username
            try:
                user = review.find("div", class_="css-901oao r-uh8wd5 r-ubezar r-b88u0q r-135wba7 r-fdjqy7").text.strip()
            except:
                user = "Anonymous"
            
            # Ambil Ulasan/Comment
            try:
                comment = review.find("div", class_="css-901oao css-cens5h r-uh8wd5 r-1b43r93 r-majxgm r-rjixqe r-fdjqy7").text.strip()
            except:
                comment = "Gak ada/null"
            
            # Ambil Rating
            try:
                rating = review.find("div", attrs={"data-testid": "tvat-ratingScore"}).text.strip()
            except:
                rating = "gak ada"
            
            # Ambil Tanggal Ulasan
            try:
                date = review.find("div", class_="css-901oao r-1ud240a r-uh8wd5 r-1b43r93 r-b88u0q r-1cwl3u0 r-fdjqy7").text.strip()
            except:
                date = "Nothing"
            
            data.append([user, comment, rating, date])

        # Cek Next Button
        try:
            next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@data-testid= 'next-page-btn']"))
                )
            if next_button.get_attribute("aria-disabled") == "true":
                print("Telah mencapai halaman terakhir")
                break
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(5)
        except:
            print("Tidak ada halaman selanjutnya")
            break

    return data

def save_to_excel(data, nama_file):

    # Simpan ke dalam DataFrame
    df = pd.DataFrame(data, columns=["username", "user_review", "rating", "review_date"])
    
    # Simpan ke file Excel
    df.to_excel(nama_file+".xlsx", index=False)

def main():
    # Input Link Review
    url = input("Masukkan link review (Traveloka): ")

    # Masukkan Nama File Hasil Scrapping
    nama_file = input("Masukkan Nama File Hasil Scraping: ")
    driver = init_driver()

    # Jalankan Proses Scraping
    try:
        data = scrape_reviews(driver, url)
        save_to_excel(data, nama_file)
    finally:
        # Tutup browser
        driver.quit()
        print("Scraping selesai! Semua ulasan telah disimpan")

if __name__ == "__main__":
    main()
