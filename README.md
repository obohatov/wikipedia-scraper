# Wikipedia Scraper

## Description
This project aims to create a web scraper that gathers information from a specific [API](https://country-leaders.onrender.com/docs) and scrapes data from Wikipedia. This application is designed to assist in accumulating a list of countries and their past political leaders' short bio. We leveraged the knowledge of creating a self-contained development environment, retrieving data from an API, scraping a website, and storing the output for later use.

The information is initially obtained by querying an API for a list of countries and their previous political leaders. Subsequently, the scraper scans and sanitizes their brief biography from Wikipedia, finally storing the acquired data on a local disk. The software employs Python's venv for environment isolation, the requests library for API calls, and BeautifulSoup to extract text from HTML.

This application primarily involves the following technical aspects:
<ul>
  <li>Retrieval of information from an API.</li>
  <li>Web scraping from Wikipedia pages.</li>
  <li>Application of regular expressions tools to sanitize text data.</li>
  <li>Creation of self-contained development environment.</li>
  <li>Implementation of object-oriented programming (Python).</li>
  <li>Handling of JSON objects.</li>
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
  <li>Using this list, for each country, the WikipediaScraper.get_leaders(country) method extracts the data of each leader.</li>
  <li>For each leader, the method WikipediaScraper.get_first_paragraph(wikipedia_url) navigates to the provided leader's Wikipedia page and scrapes data from it. The scraped data is then added to the WikipediaScraper.leaders_data JSON object.</li>
  <li>Finally, the JSON object is saved into a the leaders_data.json file using WikipediaScraper.to_json_file(filepath) method.</li>
</ol>

Now you have a JSON file <b>leaders_data.json</b> which includes crucial data about political leaders of different countries. This data is ready to be used for analysis or any other purpose.

## Visuals
![It's True. It's on Wikipedia.](<div class="tenor-gif-embed" data-postid="6138435" data-share-method="host" data-aspect-ratio="1" data-width="100%"><a href="https://tenor.com/view/its-on-wikipedia-true-wikipedia-unreliable-gif-6138435">Its On Wikipedia True GIF</a>from <a href="https://tenor.com/search/its+on+wikipedia-gifs">Its On Wikipedia GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>)
