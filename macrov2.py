import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from MacrosTest import search_queries

driver = webdriver.Chrome()
driver.get('https://youtube.com/')
searchbox = driver.find_element(By.XPATH, '//input[@id="search"]')
searchbox.click()
randomchoice = random.choice(search_queries)
searchbox.send_keys(randomchoice)
searchbutton = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')
searchbutton.click()
time.sleep(4)

while (True):
    pass

