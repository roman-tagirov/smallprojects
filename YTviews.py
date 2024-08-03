import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument("--window-size=483,376")

driver = webdriver.Chrome(options=options)

driver.get('https://www.youtube.com/watch?v=S**********')
time.sleep(3)
but = driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[6]/button')
but.click()
time.sleep(30)
while True:
    driver.get('https://www.youtube.com/watch?v=S**********')
    time.sleep(32)
