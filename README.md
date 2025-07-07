
# Newegg Graphics Card Scraper

A Python-based web scraper that extracts graphics card listings from Newegg.com across multiple pages. Built with `Selenium` and `BeautifulSoup`, this script collects comprehensive product metadata including price, shipping, promotions, ratings, and stock availability.


## Features

- Multi-page scraping (until the last page is reached)
- Extracts:
  - Product Name
  - Price
  - Shipping Information
  - Promotion/Discounts
  - Ratings
  - Stock Availability
- Automatically saves data into a clean CSV file

## Output

A file named `graphics_cards_detailed.csv` will be created in the working directory, containing the following columns:

- `Product Name`
- `Price`
- `Shipping`
- `Promotion`
- `Rating`
- `Availability`

## Requirements

Ensure the following Python packages are installed:

```bash
pip install selenium beautifulsoup4
```

You must also download [ChromeDriver](https://sites.google.com/chromium.org/driver/) and update the `CHROMEDRIVER_PATH` variable in the script to match your system path.


## Usage

1. **Clone the repository** or copy the script to your local machine.
2. **Edit the path** to your `chromedriver.exe` in the script:
   ```python
   CHROMEDRIVER_PATH = r"your/path/to/chromedriver.exe"
   ```
3. **Run the script:**

```bash
python newegg_scraper.py
```

4. The script will navigate Newegg’s GPU listings, collect data, and save it to `graphics_cards_detailed.csv`.

---

## Notes

- This scraper uses Selenium with Chrome WebDriver; ensure Chrome is installed.
- Dynamic websites like Newegg may change structure over time, which could break the scraper.
- Be mindful of scraping ethics and site terms of service.


## Author

**Cyrus Macharia**  
Date: July 5, 2025


## License

This project is open-source and available under the [MIT License](LICENSE).
