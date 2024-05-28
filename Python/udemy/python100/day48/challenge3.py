from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME, value="fName")
first_name_input.send_keys("Calix")

last_name_input = driver.find_element(By.NAME, value="lName")
last_name_input.send_keys("Shindig")

email_input = driver.find_element(By.NAME, value="email")
email_input.send_keys("aaa@gmail.com")
email_input.send_keys(Keys.ENTER)

time.sleep(5)

driver.quit()