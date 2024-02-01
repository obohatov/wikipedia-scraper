# import required libraries
import requests
from bs4 import BeautifulSoup
import json
import re

class WikipediaScraper:
    def __init__(self):
        self.base_url = 'https://country-leaders.onrender.com'
        self.country_endpoint = '/countries'
        self.leaders_endpoint = '/leaders'
        self.cookies_endpoint = '/cookie'
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
        pass

    def get_first_paragraph(self, wikipedia_url):
        pass

    def to_json_file(self, filepath):
        pass
    