import time
import os
from selenium.webdriver.common.keys import Keys # para ito sa site na may login
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By # don't know what this is for yet

options = webdriver.ChromeOptions()

blogURL = "https://www.lambdatest.com/blog/"

driver = webdriver.Chrome()
driver.get(blogURL )
time.sleep(1) # let he user actually see something!

searchBarXPath = "/html[1]/body[1]/section[1]/div[1]/form[1]/label[1]/input[1]"
textbox = driver.find_element(By.XPATH, searchBarXPath)
textbox.send_keys("topic")
textbox.send_keys(Keys.ENTER)

source = driver.page_source # this is a string

time.sleep(1)
driver.quit()
