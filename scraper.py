from utils import get_total_pages, get_page_data


class ImmobiliareScraper:
    def __init__(self, debug_mode=False):
        self.debug_mode = debug_mode

    def run(self):
        total_new_house_price = 0
        total_new_house_area = 0
        total_old_house_price = 0
        total_old_house_area = 0

        new_houses_url = 'https://www.immobiliare.it/vendita-case/monza/triante-san-giuseppe/?stato=1&noAste=1'
        old_houses_url = 'https://www.immobiliare.it/vendita-case/monza/triante-san-giuseppe/?noAste=1'

        urls = [
            (new_houses_url, 'new'),
            (old_houses_url, 'old')
        ]

        for url, house_type in urls:
            print(f'Processing {house_type} houses...')
            total_pages = get_total_pages(url)

            print(f'Total pages found for {house_type} houses: {total_pages}')

            for page_number in range(1, total_pages + 1):
                print(f'Processing {house_type} houses on page {page_number}...')
                house_page_prices, house_page_areas = get_page_data(page_number, url, debug_mode=self.debug_mode)

                if house_type == 'new':
                    total_new_house_price += sum(house_page_prices)
                    total_new_house_area += sum(house_page_areas)
                else:
                    total_old_house_price += sum(house_page_prices)
                    total_old_house_area += sum(house_page_areas)

        if total_new_house_area > 0:
            average_new_house_price_per_sqm = total_new_house_price / total_new_house_area
            print(f'Average price per square meter for new houses: {total_new_house_price} divided by {total_new_house_area}: {average_new_house_price_per_sqm:.2f} EUR')
        else:
            print('No new house data found.')

        if total_old_house_area > 0:
            average_old_house_price_per_sqm = total_old_house_price / total_old_house_area
            print(f'Average price per square meter for old houses: {total_old_house_price} divided by {total_old_house_area}: {average_old_house_price_per_sqm:.2f} EUR')
        else:
            print('No old house data found.')

        total_price = total_new_house_price + total_old_house_price
        total_area = total_new_house_area + total_old_house_area

        if total_area > 0:
            average_price_per_sqm = total_price / total_area
            print(f'Average price per square meter for all ads: {average_price_per_sqm:.2f} EUR')
        else:
            print('No data found.')

