# Immobiliare Scraper

Immobiliare Scraper is a Python script that fetches and analyzes real estate data from [Immobiliare.it](https://www.immobiliare.it). The script computes the average price per square meter for new and old houses in the Triante-San Giuseppe area of Monza, Italy by default, but you can change the URL in the script based on your desired area, simply choose it from the website and copy the url directly from your browser, and replace it with the existing one in this script.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Fetches real estate data from Immobiliare.it
- Calculates average price per square meter for new and old houses and also the combined price per average without accounting for new and old houses.
- Option to enable debug mode for more detailed output

## Requirements

- Python 3.6+
- BeautifulSoup4
- Requests

## Installation

1. Clone this repository:

   git clone https://github.com/aport1996/immobiliare_scraper.git

2. Change into the project directory:

   cd immobiliare_scraper

3. Install the required Python packages:

   pip install -r requirements.txt

## Usage

To run the script, use the following command:

python immobiliare_scraper.py


To enable debug mode for more detailed output, use the `--debug` flag:

python immobiliare_scraper.py --debug

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request or create an issue.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](LICENSE) file for details.
