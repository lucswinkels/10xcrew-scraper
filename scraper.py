import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.com/s?k=earplugs&ref=nb_sb_noss"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

products = []
for idx, product in enumerate(soup.find_all('div', {'data-component-type': 's-search-result'})):
    product_name = product.h2.a.text.strip()
    product_url = "https://www.amazon.com" + product.h2.a.get('href')
    product_price = product.find('span', {'class': 'a-offscreen'})
    if product_price is None:
        product_price = 'Not available'
    else:
        product_price = product_price.text
    products.append({'Product Name': product_name,
                    'URL': product_url, 'Price': product_price})
    print(f"{idx+1}) Product Name: {product_name}, URL: {product_url}, Price: {product_price}")

df = pd.DataFrame(products)
df.to_excel('amazon_products.xlsx', index=False)
