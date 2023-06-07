#import requests/beautifulSoup library
"""
Using beautifulSoup4 and requests, GameIdScraper.py will be able to traverse https://j-archive.com/listseasons.php
and retrieve the urls of each season. When it retrieves each url for each sesason, it will be able to 
retrieve the game id, and therefore the url, for each episode. It will then be able to send the game ids
to EpisodeScraping.py
"""
import requests
from bs4 import BeautifulSoup

url = "https://j-archive.com/listseasons.php"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

print(soup.prettify())