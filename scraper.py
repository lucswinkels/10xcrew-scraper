import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

amazon_url = "https://www.amazon.com/s?k=earplugs&ref=nb_sb_noss"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive'
}

amazon_response = requests.get(amazon_url, headers=headers)
amazon_soup = BeautifulSoup(amazon_response.content, 'html.parser')

products = []
max_results = 50

for idx, product in enumerate(amazon_soup.find_all('div', {'data-component-type': 's-search-result'})):
    position = idx + 1
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
    productpage_response = requests.get(product_url, headers=headers)
    time.sleep(1)
    productpage = BeautifulSoup(productpage_response.content, 'html.parser')
    canonical_link = productpage.find('link', {'rel': 'canonical'}).get('href')
    products.append({'Position': position, 'Product Name': product_name,
                    'URL': product_url, 'Price': product_price, 'Sponsored': product_sponsored, 'Canonical Link': canonical_link})
    if idx + 1 == max_results:
        break

df = pd.DataFrame(products)
df.to_excel('amazon_products.xlsx', index=False)
