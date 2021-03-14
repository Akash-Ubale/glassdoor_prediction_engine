## Selenium Official Doc - https://selenium-python.readthedocs.io/navigating.html

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
options = webdriver.ChromeOptions().add_argument('headless') ### Setting Up options to avoid opening separate chrome instance.
driver = webdriver.Chrome(path, options = options) 
driver.set_window_size(1120, 1000)

# It's our Test Targert URL.
url = "https://techwithtim.net"

# Sending a getb request through aour web driver.
driver.get(url)

# In the HTML page the name for the search box is 's' 
search = driver.find_element_by_name("s")

# type in 'test' in that box
search.send_keys("test")

# hit ENTER, Original name of Enter key is 'Return'.
search.send_keys(Keys.RETURN)



# This block makes program wait untill the website fully gets loaded.
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )  ### Wait for 10 Secs until the elementb presentes whose ID is 'main'.
    #print(main.text) ### print text inside main.
    
    # We are trying to get all the articles from the page.
    articles = main.find_elements_by_tag_name("article")
    
    for article in articles:
        summary = article.find_elements_by_class_name("entry-summary")
        print(summary.txt)
finally:
    driver.quit()  ### if even after 10 secs we couldn't find the element then quit.
    


# driver.close() ### its used to close the particular tab of the browser window
# time.sleep(2) ### Wait for 2 seconds.

driver.quit() ### Quits/closes the Entire Browser window.


# print(driver.page_source)  ### Prints the Entire source code of the webpage.


