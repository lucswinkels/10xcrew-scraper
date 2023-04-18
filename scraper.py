import requests
from bs4 import BeautifulSoup
import pandas as pd

amazon_url = "https://www.amazon.com/s?k=earplugs&ref=nb_sb_noss"

amazon_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive'
}

amazon_response = requests.get(amazon_url, headers=amazon_headers)
amazon_soup = BeautifulSoup(amazon_response.content, 'html.parser')

products = []
for idx, product in enumerate(amazon_soup.find_all('div', {'data-component-type': 's-search-result'})):
    if product.find('a', {'class': 'puis-sponsored-label-text'}):
        product_sponsored = "Sponsored"
    else:
        product_sponsored = " "
    product_name = product.h2.a.text.strip()
    product_url = "https://www.amazon.com" + product.h2.a.get('href')
    product_price = product.find('span', {'class': 'a-offscreen'})
    if product_price is None:
        product_price = 'Not available'
    else:
        product_price = product_price.text
    products.append({'Product Name': product_name,
                    'URL': product_url, 'Price': product_price, 'Sponsored': product_sponsored})
    if idx + 1 == 20:
        # Limit the number of results to 20
        break

df = pd.DataFrame(products)
df.to_excel('amazon_products.xlsx', index=False)
