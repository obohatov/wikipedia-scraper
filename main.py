from src.scraper import WikipediaScraper

def main():
    """
    This function completes the following steps:
    1. Creates an instance of the WikipediaScraper class.
    2. Refreshes the website cookies.
    3. Retrieves a list of countries from the website.
    4. For each country, the function gets leaders information from the website.
    5. For each leader, it fetches the first paragraph of their Wikipedia page.
    6. It saves the leaders' data to a JSON file.
    """
    scraper = WikipediaScraper()
    scraper.refresh_cookie()
    countries = scraper.get_countries()

    for country in countries:
        scraper.get_leaders(country)
        for leader in scraper.leaders_data[country]:
            wiki_url = leader["wikipedia_url"]
            leader["first_paragraph"] = scraper.get_first_paragraph(wiki_url)

    scraper.to_json_file("leaders_data.json")

if __name__ == "__main__":
    main()
