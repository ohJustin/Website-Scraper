# Reddit Website Scraper ....
# *e.g link* https://www.reddit.com/r/funny/comments/16brnzb/self_aware/
import sys
import requests


URL = sys.argv[1]

file = open("content.txt", "w")
page_to_scrape = requests.get(URL)


file.write(page_to_scrape.text)

file.close()
print("Scraper Ran ...")