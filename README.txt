Project Name: Amazon Product Web Scraper


Description
This project involves scraping product information from Amazon India's website, specifically focusing on bags. It consists of two parts:

Part 1: Scraping product information from multiple pages of search results.
Part 2: Extracting additional details from individual product pages.
The data collected will be exported in CSV format.

Table of Contents:-
Installation
Usage
Scraping Details
Exported Data
Contributing
License


Installation

Clone this repository to your local machine.
git clone https://github.com/yourusername/amazon-product-scraper.git

Install the required dependencies:
pip install -r requirements.txt

Scraping Details
Part 1
In Part 1, we scrape product information from Amazon search result pages. We aim to scrape the following details for each product:

Product URL
Product Name
Product Price
Rating
Number of Reviews
We use a web scraping library 'bs4 from BeautifulSoup' to accomplish this.

Part 2
In Part 2, we visit individual product pages using the Product URLs obtained in Part 1 and extract additional information, including:

Description
ASIN
Product Description
Manufacturer
Around 200 Product URLs are visited and data is collected.

Exported Data
The scraped data is saved in CSV format. The CSV files are named appropriately for your convenience.

Deployment
Please share the GitHub repository link, where the code and documentation are hosted, for deployment and access to the collected data.

GitHub Repository
Your GitHub Repository Link