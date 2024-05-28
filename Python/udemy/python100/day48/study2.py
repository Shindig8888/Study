from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get(r"https://en.wikipedia.org/wiki/Main_Page")

# number_of_article = driver.find_element(By.LINK_TEXT, value="MediaWiki")
# number_of_article.click()

search = driver.find_element(By.ID, value="searchInput")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

time.sleep(3)

driver.quit()


