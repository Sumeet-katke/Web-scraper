Amazon Product Scraper

## Description
This Python script scrapes product information from Amazon India's website, specifically focusing on bags. It consists of two parts:

- Part 1: Scraping product information from multiple pages of search results.
- Part 2: Extracting additional details from individual product pages.

The scraped data is saved in CSV files, which are stored in this GitHub repository.

## Installation
- Clone this repository to your local machine.
git clone https://github.com/Sumeet-katke/Web-scraper.git

Install the required dependencies:
pip install -r requirements.txt

### Note: Amazon Web Scraping Policies

This web scraping project is subject to Amazon's web scraping policies and restrictions. Amazon may implement various measures to prevent and limit web scraping activities on their platform. Due to these policies, the functionality of this web scraper may be limited or restricted, and it may not work optimally. Some potential issues and limitations you might encounter include:

IP Blocking: Amazon may temporarily or permanently block the IP address from which scraping requests are made if they detect excessive or unauthorized scraping.

Rate Limiting: Amazon may impose rate limits on requests, leading to slower scraping processes or incomplete data collection.

Changes in Website Structure: Amazon frequently updates its website's structure, which can break the scraping code. As a result, the code may need periodic adjustments to remain functional.

Captchas and Authentication: Amazon may require additional user interactions, such as solving CAPTCHAs or providing authentication, to access certain data, making automated scraping more challenging.

Legal Considerations: Comply with Amazon's terms of service and policies, as well as relevant laws and regulations, when conducting web scraping activities on their platform.

Please be aware that while this web scraper is designed to fetch data from Amazon, its performance and functionality may be impacted by the factors mentioned above

# Usage
Modify the URLs in the code to target the desired product category and number of pages to scrape.

Run the script to scrape the data:
python ecom_ai.py

The scraped data will be saved in CSV files (product_listings.csv and product_details.csv).


## Scraping Details
#Part 1
In Part 1, we scrape product information from Amazon search result pages. We extract the following details for each product:

Product URL
Product Name
Product Price
Rating
Number of Reviews


#Part 2
In Part 2, we visit individual product pages and extract additional information, including:

Description
ASIN
Product Description
Manufacturer
The data collected in Part 1 and Part 2 is saved in separate CSV files.

Exported Data
The scraped data is saved in CSV format:

product_listings.csv: Contains data from Part 1, including product listings.
product_details.csv: Contains data from Part 2, including additional product details.

GitHub Repository Link
https://github.com/Sumeet-katke/Web-scraper