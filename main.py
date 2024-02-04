import pandas as pd
from concurrent.futures import ProcessPoolExecutor

from src.scraper import WikipediaScraper

def main():
    """
    This function completes the following steps:
    1. Creates an instance of the WikipediaScraper class.
    2. Retrieves a list of countries from API.
    3. For each country, it gets leaders information from API.
    4. It saves the leaders' data to a CSV file.
    """
    scraper = WikipediaScraper()
    countries = scraper.get_countries()
    leaders_data = {}
    with ProcessPoolExecutor() as executor:
        results = executor.map(scraper.store_leader_data, countries)
        for result in results:
            leaders_data.update(result)
    df = pd.DataFrame.from_dict(leaders_data, orient="index")
    df.to_csv("leaders_data.csv", index=False, sep="\t")

if __name__ == "__main__":
    main()
