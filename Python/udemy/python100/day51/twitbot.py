from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized") 

class InternetSpeedTwitterBot():
    def __init__(self) -> None:
        self.driver = uc.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0
        self.wait = WebDriverWait(self.driver, 20)

    def get_internet_speed(self):
        self.driver.maximize_window()
        
        self.driver.get("https://www.speedtest.net/")

        run_botton = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        run_botton.click()
        time.sleep(1)
        cash_button = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        cash_button.click()

        self.driver.refresh()
        time.sleep(5)
        run_botton = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        run_botton.click()

        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(self.up)
        print(self.down)

        self.driver.close()
    
    def tweet_at_provider(self, email, password):
        self.driver.get("https://x.com/")
        time.sleep(5)
        login_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a')
        login_button.click()

        time.sleep(5)

        email_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)

        time.sleep(5)
        
        password_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

        time.sleep(3)

        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        post_button.click()
        
        
        

        time.sleep(1000000)

        
            
    
        
