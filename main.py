from concurrent.futures import ProcessPoolExecutor

from src.scraper import WikipediaScraper

def main():
    """
    This function completes the following steps:
    1. Creates an instance of the WikipediaScraper class.
    2. Retrieves a list of countries from API.
    3. For each country, it gets leaders information from API.
    4. It saves the leaders' data to a JSON file.
    """
    scraper = WikipediaScraper()
    countries = scraper.get_countries()
    with ProcessPoolExecutor() as executor:
        executor.map(scraper.store_leader_data, countries)
    scraper.to_json_file("leaders_data1.json")

if __name__ == "__main__":
    main()
