# Wikipedia Scraper

## Description
This project creates a web scraper that gathers information from a specific API and scrapes data from Wikipedia. This application is designed to assist in accumulating a list of countries and their past political leaders' short bio. We leveraged the knowledge of creating a self-contained development environment, retrieving data from an API, scraping a website, and storing the output for later use.

The information is initially obtained by querying an API for a list of countries and their previous political leaders. Subsequently, the scraper scans and sanitizes their brief biography from Wikipedia, finally storing the acquired data on a local disk. The software employs Python's venv for environment isolation, the requests library for API calls, BeautifulSoup to extract text from HTML, and pandas to organize and store the data.

This application primarily involves the following technical aspects:
<ul>
  <li>Retrieval of information from an API.</li>
  <li>Web scraping from Wikipedia pages.</li>
  <li>Sanitization of text data using regular expressions.</li> 
  <li>Application of multiprocessing for efficient extraction of data.</li> 
  <li>Creation and management of HTTP sessions for API calls.</li> 
  <li>Storing of resulting data in CSV format.</li> 
  <li>Exception handling for efficient debugging and error tracing.</li>
</ul>

## Installation
To install the script, you'll need to have Python installed on your machine. You can clone the repository to your local machine using the following commands:
```bash
git clone https://github.com/obohatov/wikipedia-scraper.git
cd wikipedia-scraper
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

## Usage
To run the script, you can execute the main.py file from your command line:
```
python main.py
```
<ol>
  <li>Upon execution, the program begins by initializing a WikipediaScraper object that aims to extract information from given APIs and Wikipedia pages.</li>
  <li>The WikipediaScraper.get_countries() method retrieves a list of countries from the API which supports the application.</li>
  <li>Using this list, for each country, the WikipediaScraper.get_leaders(country) method extracts the data of each leader, retrieves their biography from their Wikipedia page and returns this information.</li> 
  <li>The returned data is collected and combined in the main function and is then stored into a CSV file using pandas DataFrame's to_csv method.</li> 
</ol>

Now you have a CSV file <b>leaders_data.csv</b> which includes crucial data about political leaders of different countries. This data is ready to be used for analysis or any other purpose.

## Visuals
<img src="./assets/its-on-wikipedia-true.gif" alt="It's True. It's on Wikipedia." width="500"/>
