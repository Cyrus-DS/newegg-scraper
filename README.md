# newegg-scraper

````markdown
# 🛒 Newegg Graphics Card Scraper

This project is a simple web scraping script built using **Selenium** and **BeautifulSoup** to extract graphics card listings from [Newegg](https://www.newegg.com/). It fetches product names and prices from the search results and saves them into a CSV file.

---

## 📌 Features

- Launches a Chrome browser using Selenium WebDriver
- Loads Newegg's graphics card search page
- Waits for page content to fully load
- Parses the page using BeautifulSoup
- Extracts:
  - Product titles
  - Current prices
- Saves extracted data into a CSV file (`graphics_cards.csv`)

---

## 🛠️ Requirements

Before running the script, install the required libraries:

```bash
pip install selenium beautifulsoup4
````

Make sure you also have:

* **Google Chrome** installed
* **ChromeDriver** downloaded and the path updated in the script

---

## 🚀 How to Run

1. Clone or download this repository.
2. Update the `CHROMEDRIVER_PATH` in the script to the actual location of your `chromedriver.exe`.

```python
CHROMEDRIVER_PATH = "D:\\Data Science\\Data Science\\Phoenix KE Analytics Case Study\\chromedriver.exe"
```

3. Run the script in your Python environment:

```bash
python index.py
```

4. After execution, you’ll see a CSV file (`graphics_cards.csv`) with the scraped data.

---

## 📂 Output Sample

The output CSV will have the following structure:

| Product Name                        | Price    |
| ----------------------------------- | -------- |
| MSI Ventus GeForce RTX 4070 Ti      | \$799.99 |
| GIGABYTE GeForce RTX 3060 Gaming OC | \$299.99 |
| ...                                 | ...      |

---

## 📌 Notes

* Ensure that the Chrome browser version matches the version of ChromeDriver.
* You may need to adjust the wait time (`time.sleep(5)`) depending on your internet speed and Newegg's page load time.

---

## 📄 License

This project is for educational purposes and not affiliated with Newegg. Please respect the website's `robots.txt` and terms of service
