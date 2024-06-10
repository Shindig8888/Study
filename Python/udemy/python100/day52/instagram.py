from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import pprint
from selenium.common.exceptions import ElementClickInterceptedException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.follower_list = []

    def login(self, email, password):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        id_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        id_input.send_keys(email)
        
        password_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)

        login_button = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

        time.sleep(5)


    def find_followers(self):
        self.driver.get("https://www.instagram.com/ssoyang84/")
        time.sleep(5)

        followers_button = self.driver.find_element(By.XPATH, value=f"//*[contains(text(), '팔로워 ')]")
        followers_button.click()

        time.sleep(3)

        last_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll = 0
        fBody  = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')

        while scroll < 5: # scroll 5 times
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            time.sleep(2)
            scroll += 1

        self.follower_list = self.driver.find_elements(by=By.CSS_SELECTOR, value='._acan')
        pprint.pprint(self.follower_list)
        time.sleep(1)

    def follow(self):
        for button in self.follower_list:
            try:
                button.click()
            except ElementClickInterceptedException:
                pass
            finally:
                time.sleep(1.2)