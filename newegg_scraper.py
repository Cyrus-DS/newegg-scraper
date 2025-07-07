
"""
Title: Newegg Graphics Card Scraper
Author: Cyrus Macharia
Date: 05/07/2025
Description:
    Scrapes product data from Newegg search results for graphics cards,
    spanning multiple pages until no more results are found.
    Captures product name, price, shipping info, promo/discounts, ratings, and stock availability.
"""

import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# 1. Configuration
CHROMEDRIVER_PATH = r"D:\Data Science\Data Science\Phoenix KE Analytics Case Study\Phoenix KE Mentorship Projects\Webscrapping project\chromedriver.exe"
BASE_URL = "https://www.newegg.com/p/pl?d=graphics+card"
CSV_FILENAME = "graphics_cards_detailed.csv"

# 2. Setup WebDriver
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(BASE_URL)
time.sleep(5)  # Initial load wait

products = []

# 3. Loop through pages dynamically
page_number = 1
while True:
    print(f"Scraping Page {page_number}...")

    # Get and parse current page's HTML
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="item-cell")

    # Extract product details
    for item in items:
        title_tag = item.find("a", class_="item-title")
        price_tag = item.find("li", class_="price-current")
        shipping_tag = item.find("li", class_="price-ship")
        promo_tag = item.find("p", class_="item-promo")
        rating_tag = item.find("a", class_="item-rating")  # tooltip with star rating
        availability_text = item.text.upper()

        if title_tag:
            product_name = title_tag.text.strip()
            price = price_tag.text.strip() if price_tag else "N/A"
            shipping = shipping_tag.text.strip() if shipping_tag else "N/A"
            promo = promo_tag.text.strip() if promo_tag else "None"
            rating = rating_tag["title"] if rating_tag and "title" in rating_tag.attrs else "No Rating"
            availability = "Out of Stock" if "OUT OF STOCK" in availability_text else "Available"

            products.append({
                "Product Name": product_name,
                "Price": price,
                "Shipping": shipping,
                "Promotion": promo,
                "Rating": rating,
                "Availability": availability
            })

    # Check for Next button to proceed
    try:
        next_button = driver.find_element(By.CLASS_NAME, "btn-next")
        if "disabled" in next_button.get_attribute("class"):
            print("Reached last page.")
            break
        next_button.click()
        page_number += 1
        time.sleep(5)  # Wait for next page to load
    except NoSuchElementException:
        print("No 'Next' button found. Ending scrape.")
        break

# 4. Save to CSV
driver.quit()

with open(CSV_FILENAME, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["Product Name", "Price", "Shipping", "Promotion", "Rating", "Availability"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

print(f"\n✅ Successfully saved {len(products)} products to '{CSV_FILENAME}'")
