from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Webdriver Destination Folder
path = "D:\Akash\Documents\Recover\MY NOTES\web scraping\chromedriver_win32\chromedriver.exe"

# Setting up the Driver
# Setting Up options to avoid opening separate chrome instance.
options = webdriver.ChromeOptions().add_argument('headless')
driver = webdriver.Chrome(path, options = options) 
driver.set_window_size(1120, 1000)

url = "https://techwithtim.net"

driver.get(url)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)


#driver.close()
time.sleep(2)
driver.quit()


