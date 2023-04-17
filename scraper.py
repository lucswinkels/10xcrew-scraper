import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Amazon page to scrape
url = "https://www.amazon.com/Eargasm-Musicians-Motorcycles-Sensitivity-Conditions/dp/B019M576XW/ref=sr_1_9?crid=3TJTCL31OEHGC&keywords=Motorcycle%2BEar%2BPlugs&qid=1681721023&sprefix=motorcycle%2Bear%2Bplugs%2Caps%2C173&sr=8-9&th=1"

# Make a GET request to the URL and get the HTML content
response = requests.get(url)
content = response.content
print(content)
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())
# Find all the product containers on the page
product_containers = soup.find_all('div', {'class': 's-result-item'})

# Initialize an empty list to store the product details
product_details = []

# Loop through each product container and extract details
# extract details of only the first 40 products
for container in product_containers[:40]:
    # Extract the product name
    name = container.find('h2').text.strip()

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
