# Reddit Website Scraper ....
# *e.g link* https://www.reddit.com/r/funny/comments/16brnzb/self_aware/
from bs4 import BeautifulSoup
import requests


page_to_scrape = requests.get("https://www.reddit.com/r/funny/comments/16brnzb/self_aware/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")


#Search for <> tags ?
#comments = ?

#Search for ...