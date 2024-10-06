from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# The URL to scrape
url = "https://completelydifferent.atlassian.net/wiki/external/ZWRjZTQ3NDcwNGE5NDA0MzliYzdhMzk1YTg5Y2M0ZDE"

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode to avoid opening a browser window
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Load the page
    logging.info("Loading the page...")
    driver.get(url)
    time.sleep(10)  # Wait for the page to fully load (adjust if necessary)

    # Extract the main content from the page using BeautifulSoup
    logging.info("Extracting page source with BeautifulSoup...")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # Log the page source for debugging purposes
    logging.debug(f"Page Source: {driver.page_source[:1000]}... (truncated)")
    
    # Try different possible content containers
    possible_selectors = [
        ("div", {"id": "content"}),
        ("div", {"class": "wiki-content"}),
        ("div", {"class": "main-content"}),
        ("div", {"class": "external-content"}),
        ("body", {})
    ]

    page_content = None
    for tag, attrs in possible_selectors:
        page_content = soup.find(tag, attrs)
        if page_content:
            logging.info(f"Content found using tag '{tag}' with attributes {attrs}")
            break

    if page_content:
        text_content = page_content.get_text(separator="\n", strip=True)

        # Save the extracted content to a JSON file
        data = {
            "url": url,
            "content": text_content
        }

        with open("confluence_content.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        logging.info("Content successfully scraped and saved to 'confluence_content.json'")
    else:
        logging.warning("Could not find the main content on the page. Trying to save raw HTML.")
        with open("confluence_raw.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
        logging.info("Raw HTML saved to 'confluence_raw.html' for further inspection.")

except Exception as e:
    logging.error(f"An error occurred while fetching the URL: {e}")

finally:
    # Close the WebDriver
    logging.info("Closing the WebDriver...")
    driver.quit()