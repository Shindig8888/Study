from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()
url = r"https://www.linkedin.com/jobs/search/?currentJobId=3812096086&f_AL=true&keywords=python%20developers&origin=JOB_SEARCH_PAGE_JOB_FILTER&sortBy=R"
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-webrtc")
chrome_options.add_argument("--force-webrtc-ip-handling-policy=disable_non_proxied_udp")
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(chrome_options)
driver.maximize_window()

driver.get(url)
login_button = driver.find_element(By.CSS_SELECTOR, value=".nav__cta-container .nav__button-secondary")
login_button.click()

email_input = driver.find_element(By.XPATH, value='//*[@id="username"]')
email_input.send_keys(EMAIL)
password_input = driver.find_element(By.XPATH, value='//*[@id="password"]')
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

time.sleep(6)

job_list = driver.find_elements(By.CSS_SELECTOR, value=".job-card-list__entity-lockup a")
job_list = job_list[0:5]

for job in job_list:
    job.click()
    save_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-save-button")
    save_button.click()
    time.sleep(1)


driver.quit()