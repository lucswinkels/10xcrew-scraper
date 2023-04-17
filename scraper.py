import requests
from bs4 import BeautifulSoup
import pandas as pd

# Headers to pass to the request to avoid CAPTCHA
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive'
}

# URL of the Amazon page to scrape
url = "https://www.amazon.com/s?k=earplugs&ref=nb_sb_noss"

# Make a GET request to the URL and get the HTML content
response = requests.get(url, headers=headers)
content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find all the product containers on the page
product_containers = soup.find_all('div', {'class': 's-result-item'})
# Initialize an empty list to store the product details
product_details = []

# Loop through each product container and extract details
# extract details of only the first 40 products
for container in product_containers[:40]:
    # Extract the product name
    name = getattr(container.find('h2'), 'text', None)

    # Extract the product price
    price_container = container.find('span', {'class': 'a-offscreen'})
    if price_container:
        price = price_container.text.strip()
    else:
        price = "N/A"

    # Extract the product rating
    rating_container = container.find('span', {'class': 'a-icon-alt'})
    if rating_container:
        rating = rating_container.text.strip()
    else:
        rating = "N/A"

    # Add the product details to the list
    product_details.append({'Name': name, 'Price': price, 'Rating': rating})

# Create a Pandas dataframe from the product details list
df = pd.DataFrame(product_details)

# Print the dataframe to the console
print(df.to_string(index=False))

# Export the dataframe to an Excel file
df.to_excel('product_details.xlsx', index=False)
