# import required libraries
import requests
from bs4 import BeautifulSoup
import json
import re

class WikipediaScraper:
    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}

    def refresh_cookie(self):
        cookie_url = self.base_url + self.cookies_endpoint
        response = requests.get(cookie_url)
        self.cookie = response.cookies
        return self.cookie

    def get_countries(self):
        countries_url = self.base_url + self.country_endpoint
        response = requests.get(countries_url, cookies=self.cookie)
        countries = response.json()
        return countries

    def get_leaders(self, country):
        leaders_url = self.base_url + self.leaders_endpoint
        response = requests.get(leaders_url, params={"country": country}, cookies=self.cookie)
        leaders = response.json()
        self.leaders_data[country] = leaders

    def get_first_paragraph(self, wikipedia_url):
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

    def to_json_file(self, filepath):
        with open(filepath, "w") as json_file:
            json.dump(self.leaders_data, json_file)
