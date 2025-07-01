#!/usr/bin/env python
# coding: utf-8

# In[24]:


pip install selenium beautifulsoup4


# In[29]:


# Loading necessary drivers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv


# In[26]:


# Update path where chromedriver was saved
CHROMEDRIVER_PATH = "D:\Data Science\Data Science\Phoenix KE Analytics Case Study\Phoenix KE Mentorship Projects\chromedriver.exe"

# Start chrome browser with selenium
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

# Open newegg graphics card search page
url = "https://www.newegg.com/p/pl?d=graphics+card"
driver.get(url)

time.sleep(5)

# To get HTML content after JS has loaded
html = driver.page_source
soup = BeautifulSoup(html,"html.parser")



# In[32]:


# Scrapping data, Finding all prodcut containers
items = soup.find_all("div", class_="item-cell")

# Create a list to store product info
products = []

#Loop through & extract info:
for item in items:
    title_tag = item.find("a", class_="item-title")
    price_tag = item.find("li", class_="price-current")

    if title_tag and price_tag:
        title = title_tag.text.strip()
        price = price_tag.text.strip()
        products.append({"Product Name": title, "Price":price})


# In[33]:


# Save to CSV
csv_filename = "graphics_cards.csv"
with open(csv_filename, mode="w", newline="",encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Product Name", "Price"])
    writer.writeheader()
    writer.writerows(products)

print(f"Saved {len(products)} items to '{csv_filename}'")

