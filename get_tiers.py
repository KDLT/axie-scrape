import time
import os
from selenium.webdriver.common.keys import Keys # para ito sa site na may login
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By # used for locating Elements By.XPATH for instance

options = webdriver.ChromeOptions()

tierListURL = "https://axie.zone/card-tier-list"
blogURL = "https://www.lambdatest.com/blog/"

driver = webdriver.Chrome()
driver.get(tierListURL)
time.sleep(1) # let he user actually see something!

classes = [
    'cfall', 'cfaquatic', 
    'cfbeast', 'cfbird', 'cfbug', 
    'cfplant', 'cfreptile', 'cfmech', 'cfdawn', 'cfdusk'
    ]

# card_container 'yung id ngayon sa axie zone, PWEDS mag-iba eventually
cardsID = "card_container"

for name in classes:
    radio = driver.find_element(By.ID, name)
    radio.click()

    source = driver.page_source # ito na 'yung text form, string na
    tierSoup = bs(source, 'html.parser') # this gets the ENTIRE page
    # print(tierSoup.prettify())
    # print(tierSoup.find(id=cardsID).prettify())

    ## This doesn't work
    # container = driver.find_element(By.ID, cardsID)
    # containerSoup = bs(container, 'html.parser')
    # print(containerSoup.prettify())
    
    filename = name[2:] + ".html"
    with open("scraped_html/" + filename, "w") as file:
        file.write(str(tierSoup.find(id=cardsID).prettify()))

time.sleep(1)
driver.quit()

# print(soup.find(id='link3')) # buong </> ang output