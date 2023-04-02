import re
import requests
from bs4 import BeautifulSoup


def get_total_pages(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f'Error fetching the first page: {response.status_code}')
        return 1

    soup = BeautifulSoup(response.content, 'html.parser')
    pagination = soup.find('div', class_='in-pagination__list')

    if not pagination:
        print('Pagination element not found. Assuming there is only one page.')
        return 1

    last_page_link = pagination.find_all('a', class_='in-pagination__item')[-1]['href']
    last_page_number = int(re.search(r'pag=(\d+)', last_page_link).group(1))
    return last_page_number


def get_page_data(page_number, url, debug_mode=False):
    url = f'{url}&pag={page_number}'
    response = requests.get(url)

    if response.status_code != 200:
        print(f'Error fetching page {page_number}: {response.status_code}')
        return [], []

    soup = BeautifulSoup(response.content, 'html.parser')

    ads = soup.find_all('li', class_='nd-list__item in-realEstateResults__item')
    print(f'Ads found on page {page_number}: {len(ads)}')

    house_prices = []
    house_areas = []

    for ad in ads:
        price = ad.find('li', class_='nd-list__item in-feat__item in-feat__item--main in-realEstateListCard__features--main')
        area = ad.find('li', class_='nd-list__item in-feat__item', attrs={'aria-label': 'superficie'})

        if price and area:
            price_text = price.text.strip()
            area_text = area.text.strip()

            try:
                price_number = float(price_text.replace('.', '').replace(',', '.').replace('€', '').strip())
                area_number = float(area_text.replace('m²', '').strip())
                print(f'Price for ad is {price_number} for {area_number} sqm2')
                house_prices.append(price_number)
                house_areas.append(area_number)
            except ValueError:              
                pass
        elif debug_mode:
            print(f'Price or area not found in ad: {ad}\n{ad.prettify()}')
        else:
            print(f'Price not found in ad: {ad.find("a").text}')
    print(f'Total house prices: {house_prices} Total house areas: {house_areas}')
    return house_prices, house_areas

