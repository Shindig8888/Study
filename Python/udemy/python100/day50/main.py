from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
from dotenv import load_dotenv
import os
import undetected_chromedriver as uc

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")  # 전체화면으로 시작

driver = uc.Chrome(options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://tinder.com/")
time.sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[@id="q-766335200"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

time.sleep(2)
iframe_element = driver.find_element(By.XPATH, '//iframe[@title="Google 계정으로 로그인 버튼"]')
driver.switch_to.frame(iframe_element)

driver.get(iframe_element.get_attribute("src"))

# 다시 메인 프레임으로 전환
driver.switch_to.default_content()


# facebook_login_button = driver.find_element(By.XPATH, '//*[@id="q1800251020"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
# time.sleep(2)
# facebook_login_button.click()

# base_window = driver.window_handles[0]
# facebook_login_window = driver.window_handles[1]
# driver.switch_to.window(facebook_login_window)

# time.sleep(2)


# email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
# email_input.send_keys(EMAIL)
# password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pass"]')))
# password_input.send_keys(PASSWORD)
# password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pass"]')))
# password_input.send_keys(Keys.ENTER)

# time.sleep(10)

# facebook_final_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".select")))
# time.sleep(10)
# facebook_final_button.click()

# time.sleep(10)

# driver.switch_to.window(base_window)



# location_confirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q1800251020"]/div/div[1]/div/div/div[3]/button[1]')))
# location_confirm.click()

# time.sleep(2000000000)


