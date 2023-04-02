import argparse
from scraper import ImmobiliareScraper


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="enable debug mode", action="store_true")
    args = parser.parse_args()

    scraper = ImmobiliareScraper(debug_mode=args.debug)
    scraper.run()


if __name__ == '__main__':
    main()

