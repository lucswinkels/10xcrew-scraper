import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

search_term = "office+chair"
amazon_url = f'https://www.amazon.com/s?k={search_term}&ref=nb_sb_noss'

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
max_results = 100

direct_link = None
for idx, product in enumerate(amazon_soup.find_all('div', {'data-component-type': 's-search-result'})):
    position = idx + 1
    if product.find('a', {'class': 'puis-sponsored-label-text'}):
        product_sponsored = "Sponsored"
    else:
        product_sponsored = " "
    product_name = product.h2.a.text.strip()
    product_price = product.find('span', {'class': 'a-offscreen'})
    if product_price is None:
        product_price = 'Not available'
    else:
        product_price = product_price.text
    product_url = "https://www.amazon.com" + product.h2.a.get('href')
    regex = r"&url=%2F(.*)%2Fdp%2F([A-Z0-9]+)%2F"
    matches = re.finditer(regex, product_url, re.MULTILINE)
    match_found = False
    for matchNum, match in enumerate(matches, start=1):
        match_found = True
        print("Match {matchNum} was found at {start}-{end}: {match}".format(
            matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
                                                                            start=match.start(groupNum), end=match.end(groupNum), group=match.group(groupNum)))
        canonical_link = f'https://www.amazon.com/{match.group(1)}/dp/{match.group(2)}'
        products.append({'Position': position, 'Product Name': product_name,
                        'URL': product_url, 'Price': product_price, 'Sponsored': product_sponsored, 'Canonical Link': canonical_link})
        break
    if not match_found:
        canonical_link = product_url
        products.append({'Position': position, 'Product Name': product_name,
                         'URL': product_url, 'Price': product_price, 'Sponsored': product_sponsored, 'Canonical Link': canonical_link.split('/ref=')[0]})
    if not direct_link:
        direct_link = canonical_link

    if idx + 1 == max_results:
        break

df = pd.DataFrame(products)
df.to_excel(f'{search_term}.xlsx', index=False)
