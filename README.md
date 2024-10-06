# Confluence Scraper Project

## Overview

This project provides a script to scrape content from a Confluence page and save it as structured data. The goal is to extract meaningful content from a Confluence page and store it in a JSON format for easy access and further processing. The project is useful for extracting knowledge from Confluence pages that may not have an API endpoint or other means of easy data retrieval.

## Prerequisites

To use this project, you need to have the following installed:

- Python 3.x
- Google Chrome Browser
- ChromeDriver (handled by `webdriver-manager`)
- Virtual environment (optional, but recommended)

## Installation

1. **Clone the Repository**

   ```sh
   git clone <repository-url>
   cd confluence_scraper_project
   ```

2. **Create a Virtual Environment** (optional but recommended)

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Install the required Python packages by running:
   ```sh
   pip install -r requirements.txt
   ```
   The main dependencies include Selenium, BeautifulSoup, and WebDriver Manager.

## Usage

The script scrapes the specified Confluence URL and saves the content as JSON. To run the scraper:

```sh
python confluence_scraper.py
```

Make sure you have the necessary permissions to access the target Confluence page.

### Key Parameters

- **`url`**: Update the URL variable inside the script to the Confluence page you wish to scrape. Currently, it is set to:
  ```python
  url = "https://completelydifferent.atlassian.net/wiki/external/ZWRjZTQ3NDcwNGE5NDA0MzliYzdhMzk1YTg5Y2M0ZDE"
  ```
- **Chrome Options**: The script runs in headless mode, making it suitable for running on servers or CI/CD pipelines without a display.

## Output

- **`confluence_content.json`**: The output is a JSON file containing the extracted text content from the Confluence page. For example, the file may look like:

  ```json
  {
    "url": "https://completelydifferent.atlassian.net/wiki/external/ZWRjZTQ3NDcwNGE5NDA0MzliYzdhMzk1YTg5Y2M0ZDE",
    "content": "rutabaga"
  }
  ```

  If the main content could not be located, the script saves the entire HTML page for further inspection.

- **`confluence_raw.html`**: This file will contain the raw HTML of the page if the scraper could not successfully locate the main content.

## Troubleshooting

- **Missing ChromeDriver**: If you receive an error stating that ChromeDriver could not be found, ensure `webdriver_manager` is installed properly. The script automatically manages the driver installation.
- **No Content Found**: The page may be using JavaScript to render content, which requires additional waiting time or more sophisticated parsing logic.
- **Import Errors**: If you encounter `ImportError`, make sure to install the `webdriver-manager` using:
  ```sh
  pip install webdriver-manager
  ```

## Logging

The script uses Python's built-in `logging` library for informational messages and debugging purposes. Logs include details about the scraping process, including any issues encountered.

## Customization

- **Page Content Selector**: By default, the script attempts to locate a `div` with the class `content-body`. Depending on the structure of the Confluence page, you may need to modify the selector to accurately target the desired content.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request with any enhancements or bug fixes.

## Contact

If you have any questions or issues, please contact [your-email@example.com].
