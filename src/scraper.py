import requests
from bs4 import BeautifulSoup
import json
import re


class WikipediaScraper:
    """ 
    A web scraper for collecting information on country leaders 
    """

    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}
    
    def __str__(self):
        return (f"WikipediaScraper targeting API {self.base_url}, has "
                f"scraped data for {len(self.leaders_data)} countries")

    def refresh_cookie(self) -> object:
        """
        Refresh cookies by making request to the cookies' endpoint
        """
        cookie_url = self.base_url + self.cookies_endpoint
        response = requests.get(cookie_url)
        self.cookie = response.cookies
        return self.cookie

    def get_countries(self) -> list:
        """
        Get a list of countries from the countries' endpoint
        """
        countries_url = self.base_url + self.country_endpoint
        response = requests.get(countries_url, cookies=self.cookie)
        countries = response.json()
        return countries

    def get_leaders(self, country: str) -> None: 
        """
        Get information about the leaders for a specific country 
        and save the data
        """
        leaders_url = self.base_url + self.leaders_endpoint
        response = requests.get(leaders_url, params={"country": country}, cookies=self.cookie)
        leaders = response.json()
        
        for leader in leaders:
            if isinstance(leader, dict) and leader.get("id"):
               leader_id = leader.get("id")
               leader_url = self.base_url + "/leader"
               leader_response = requests.get(leader_url, params={"leader_id": leader_id}, cookies=self.cookie)
               leader_data = leader_response.json()
               wikipedia_url = leader_data.get("wikipedia_url")
               first_paragraph = self.get_first_paragraph(wikipedia_url)
               self.leaders_data[leader_id] = {"wikipedia_url": wikipedia_url, "first_paragraph": first_paragraph}  

    def get_first_paragraph(self, wikipedia_url: str) -> str:
        """
        Extract the first paragraph of the leader's wikipedia page
        """
        response_wiki = requests.get(wikipedia_url)
        soup = BeautifulSoup(response_wiki.text, "html.parser")

        bodyContent = soup.find("div", id="bodyContent")
        paragraphs = bodyContent.find_all("p")
        
        first_paragraph = ""
        for paragraph in paragraphs:
            if paragraph.find("b"):
                first_paragraph = paragraph.text
                break

        first_paragraph = re.sub(r"\{.*?\}|<.*?>|\[.*?\]", "", first_paragraph)
        return first_paragraph

    def to_json_file(self, filepath: str) -> None:
        """
        Save the leaders' data to a JSON file
        """
        with open(filepath, "w") as json_file:
            json.dump(self.leaders_data, json_file)
