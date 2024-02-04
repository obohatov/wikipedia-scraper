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
        self.leader_endpoint = "/leader"
        self.cookies_endpoint = "/cookie"
        self.session = requests.Session() 
        self.cookie = self.refresh_cookie()
        self.leaders_data = {}

    def __str__(self):
        return (f"WikipediaScraper targeting API {self.base_url}, has "
                f"scraped data for {len(self.leaders_data)} countries")
    
    def get_response(self, 
                     url: str, 
                     params: dict = None
                     ) -> requests.Response:
        """
        Send a GET request to the specified URL with optional parameters 
        and cookies
        """        
        response = self.session.get(
            url, 
            params=params, 
            cookies=self.cookie
            )
        return response

    def refresh_cookie(self) -> object:
        """
        Refresh cookies by making request to the cookies' endpoint
        """
        cookie_url = self.base_url + self.cookies_endpoint
        response = self.session.get(cookie_url)
        return response.cookies

    def get_countries(self) -> list:
        """
        Get a list of countries from the countries' endpoint
        """
        countries_url = self.base_url + self.country_endpoint
        response = self.session.get(countries_url, cookies=self.cookie)
        if response.status_code == 200:
            countries = response.json()            
            return countries
        else: 
            raise Exception('Could not fetch countries')

    def get_leader(self, leader_id: str) -> dict:
        """
        Get information about specific leader from the leader endpoint
        """
        leader_url = self.base_url + self.leader_endpoint
        response = self.session.get(leader_url, 
                                params={"leader_id": leader_id}, 
                                cookies=self.cookie
                                )
        if response.status_code == 403:
            self.cookie = self.refresh_cookie()
            response = self.session.get(
                leader_url, 
                params={"leader_id": leader_id}, 
                cookies=self.cookie
                )
        if response.status_code == 200:
            leader = response.json()
        else:
            print(f"Response code: {response.status_code}")
            print(f"Response text: {response.text}")
            raise Exception(
                f"Could not fetch leader information with id {leader_id}"
                )
        return leader

    def get_leaders(self, country: str) -> None: 
        """
        Get information about the leaders for a specific country 
        and save the data
        """
        leaders_url = self.base_url + self.leaders_endpoint
        response = self.session.get(
            leaders_url, 
            params={"country": country}, 
            cookies=self.cookie
            )
        if response.status_code == 403:
            self.cookie = self.refresh_cookie()
            response = self.session.get(
                leaders_url, 
                params={"country": country}, 
                cookies=self.cookie
                )
        if response.status_code == 200:
            leaders = response.json()
        else:
            raise Exception(f"Could not fetch leaders for {country}")
        return leaders 

    def get_first_paragraph(self, wikipedia_url: str) -> str:
        """
        Extract the first paragraph of the leader's wikipedia page
        """
        response_wiki = self.session.get(wikipedia_url)
        soup = BeautifulSoup(response_wiki.text, "lxml")

        bodyContent = soup.find("div", {"id": "bodyContent"})
        paragraphs = bodyContent.find_all("p")
        for paragraph in paragraphs:
            if paragraph.find("b"):
                first_paragraph = paragraph.text
                break
                
        first_paragraph = re.sub(
            r"\{.*?\}|<.*?>|\[.*?\]", 
            "", 
            first_paragraph
            )
        return first_paragraph.strip()

    def store_leader_data(self, country: str) -> dict:
        """
        Get information about the leaders for a specific country 
        and store in the leaders_data
        """
        leaders = self.get_leaders(country)
        country_leaders_data = {}
        for leader in leaders:
            leader_info = self.get_leader(leader["id"])
            wiki_intro = self.get_first_paragraph(
                leader_info["wikipedia_url"]
                )
            country_leaders_data[leader["id"]] = {
            "first_name": leader_info["first_name"],
            "last_name": leader_info["last_name"],
            "wikipedia_intro": wiki_intro,
            }
        return country_leaders_data
