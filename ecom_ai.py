# Python program to scrape product details from an E-Commerce webpage (HTML in this case)

# Importing necessary libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Part 1: Scraping Product Listings
product_listings = []

for page in range(1, 21):  # Scrape 20 pages
    url = f"https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{page}"

    # Send an HTTP GET request to the Amazon URL and retrieve the HTML content
    response = requests.get(url)

    # Parsing the HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract product information retrieved
    for product in soup.find_all('div', class_='s-result-item'):
        # Product URL
        product_url_element = product.find('a', class_='a-link-normal')
        product_url = 'https://www.amazon.in' + product_url_element['href'] if product_url_element else None

        # Product Name
        product_name_element = product.find('span', class_='a-text-normal')
        product_name = product_name_element.text if product_name_element else None

        # Product Price
        product_price_element = product.find('span', class_='a-price-whole')
        product_price = product_price_element.text if product_price_element else None

        # Rating
        product_rating_element = product.find('span', class_='a-icon-alt')
        product_rating = product_rating_element.text if product_rating_element else None

        # Number of reviews
        product_reviews_element = product.find('span', class_='a-size-base')
        product_reviews = product_reviews_element.text if product_reviews_element else None

        # Store the extracted information in a dictionary and add it to the product_listings list
        product_info = {
            'Product URL': product_url,
            'Product Name': product_name,
            'Product Price': product_price,
            'Rating': product_rating,
            'Number of Reviews': product_reviews
        }
        product_listings.append(product_info)


#PArt - 02:
# List to scrape the product details
product_details = []

# Loop through the list of product URLs obtained in Part 1
for product_info in product_listings:
    product_url = product_info['Product URL']

    # Send an HTTP GET request to the product URL and retrieve the HTML content
    response = requests.get(product_url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting additional product details (Description, ASIN, Product Description, Manufacturer)
    product_description = soup.find('div', {'id': 'productDescription'})
    if product_description:
        description = product_description.get_text().strip()
    else:
        description = None

    asin = soup.find('th', text='ASIN').find_next('td').text.strip() if soup.find('th', text='ASIN') else None

    product_desc = soup.find('span', {'id': 'productTitle'}).get_text().strip() if soup.find('span', {'id': 'productTitle'}) else None

    manufacturer = soup.find('a', {'id': 'bylineInfo'}).get_text().strip() if soup.find('a', {'id': 'bylineInfo'}) else None

    # Storing and adding the extracted information in a dictionary
    product_details.append({
        'Description': description,
        'ASIN': asin,
        'Product Description': product_desc,
        'Manufacturer': manufacturer
    })

# Export the data to CSV files
product_listings_df = pd.DataFrame(product_listings)
product_details_df = pd.DataFrame(product_details)

# Combining dataframes
final_data = pd.concat([product_listings_df, product_details_df], axis=1)

# Export to CSV files
product_listings_df.to_csv('product_listings.csv', index=False)
product_details_df.to_csv('product_details.csv', index=False)
