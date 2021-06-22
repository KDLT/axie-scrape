html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

sampleURL = "https://dataquestio.github.io/web-scraping-pages/simple.html"
tierListURL = "https://axie.zone/card-tier-list"

from bs4 import BeautifulSoup as bs
import requests
import re # regex

#soup = bs(html_doc, 'html.parser')

#print(page.status_code) # 200 means success, starts with 2 is good, 4 or 5 may error
#print(page.content) # ugly single line version

page = requests.get(sampleURL) # object, not string
#page = requests.get(page.content)

#print(page.conteint)

soup = bs(page.content, 'html.parser')
#print(soup.prettify())

print(soup.p.string)

# pageSouped = BeautifulSoup(page.content, 'html.parser')
# print(pageSouped.prettify)

# print(soup.prettify())
# print(soup.title) # kasama dito 'yung </> wrappers
# print(soup.title.name) # title 'yung name??!
# print(soup.title.string) # ito 'yung nasa loob ng class title
# print(soup.title.parent.name) # head
# print(soup.p) # unang <p> element
# print(soup.p['class']) # ['title'] ang class, weird may brackets
# print(soup.a) # like p, ang output ay 'yung unang instance, this case elsie ta's buong line kasama </>
# print(soup.find_all('a')) # very intuitive, lahat ng <a> ang output
# print(soup.find(id='link3')) # buong </> ang output

# for link in soup.find_all('a'): # get all links in soup
#     print(link.get('href'))

#for sister in soup.find_all('a', {'class': 'sister'}): # or
# for sister in soup.find_all('a', class_='sister'): # css search using trailing underscore
#      print(sister.string)

# for tag in soup.find_all(re.compile('^ti')): # regex leading "ti" so title
#     print(tag.name)