from bs4 import BeautifulSoup
from requests_cache import CachedSession
session = CachedSession()

my_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36", 
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }
sampleURL = "https://dataquestio.github.io/web-scraping-pages/simple.html"
tierListURL = "https://axie.zone/card-tier-list"
tdsURL = "https://communityfoundations.ca/find-a-community-foundation/"

# with session.cache_disabled():
#     session.get(sampleURL, headers=my_headers)
# sampleResponse = session.get(sampleURL, headers=my_headers) # everything in the page is now in this object
tierListResponse = session.get(tierListURL, headers=my_headers)

# sample_soup = BeautifulSoup(sampleResponse.text, 'html.parser') # this is when you can actually read the object
tierList_soup = BeautifulSoup(tierListResponse.text, 'html.parser')

# print(sample_soup.prettify())
# print(tierList_soup.prettify())

with open("output.html", "w") as file:
    file.write(str(tierList_soup))