from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from pprint import pprint
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import requests
import json

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
address_cluster = "상도동"

class RoomCapture():
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.url_list = []
        self.address_list = []
        self.price_per_month_list = []

    def login(self):
        self.driver.get("https://www.dabangapp.com/")
        
        login_button = self.driver.find_element(By.XPATH, '//*[@id="gnb-content"]/div/div[2]/button[1]')
        login_button.click()
        time.sleep(1)

        login_by_email_button = self.driver.find_element(By.XPATH, '//*[@id="content"]/section/div/div[3]/button[2]')
        login_by_email_button.click()
        time.sleep(1)

        email_input = self.driver.find_element(By.XPATH, '//*[@id="content"]/section/div/form/div[1]/div/div/div/input')
        email_input.send_keys(EMAIL)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="content"]/section/div/form/div[2]/div/div/div/input')
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(2)

    def favorite_collector(self):

        self.driver.get("https://www.dabangapp.com/")
        address_input = self.driver.find_element(By.XPATH, value='//*[@id="content"]/div[1]/div/div/label/input')
        address_input.send_keys(address_cluster)
        time.sleep(1)

        find_address_button = self.driver.find_element(By.CSS_SELECTOR, value='.styled__RegionBtn-jva10k-2')
        time.sleep(0.5)
        find_address_button.click()
        time.sleep(1)

        filter_button = self.driver.find_element(By.XPATH, value='//*[@id="content"]/div[1]/div[2]/div[2]/button')
        filter_button.click()

        trade_checkbox = self.driver.find_element(By.XPATH, value='//*[@id="content"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div/label[3]/input')
        trade_checkbox.click()        
        lease_checkbox = self.driver.find_element(By.XPATH, value='//*[@id="content"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div/label[2]/input')
        lease_checkbox.click()
        time.sleep(1)

        last_page= self.driver.find_element(By.XPATH, value='//*[@id="content"]/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div/button[9]')
        last_page.click()
        time.sleep(0.5)
        pages = self.driver.find_elements(By.CSS_SELECTOR, value='.styled__PageBtn-d24fjp-2')
        full_length = int(pages[-1].text)
        print(full_length)
        time.sleep(0.5)
        first_page = self.driver.find_element(By.XPATH, value='//*[@id="content"]/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div/button[1]')
        first_page.click()
        time.sleep(1)


        for page_number in range(1,full_length+1):
            time.sleep(0.5)
            favorite_rooms = self.driver.find_elements(By.CSS_SELECTOR, 'button.styled__LikeBtn-jmubsw-1')
            pprint(favorite_rooms)
            for room in favorite_rooms:
                room.click()
                time.sleep(0.2)
            if page_number==full_length-1:
                last_page= self.driver.find_element(By.XPATH, value='//*[@id="content"]/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div/button[9]')
                last_page.click()
                continue
            elif page_number==full_length:
                break
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.styled__PageBtn-d24fjp-2')))
            button_clicker = self.driver.find_element(By.XPATH, value=f'//button[text()="{page_number+1}"]')
            button_clicker.click()

        time.sleep(0.5)

    def url_collector(self):
        self.driver.get("https://www.dabangapp.com/favorite/recent-room")
        time.sleep(1)
        favorites = self.driver.find_element(By.XPATH, value='//*[@id="content"]/header[2]/div/ul/li[2]/a')
        favorites.click()
        time.sleep(0.3)

        last_page= self.driver.find_element(By.XPATH, value='//*[@id="content"]/div/div/div[2]/button[9]')
        last_page.click()
        time.sleep(0.5)
        pages = self.driver.find_elements(By.CSS_SELECTOR, value='.styled__PageBtn-d24fjp-2')
        full_length = int(pages[-1].text)

        first_page = self.driver.find_element(By.XPATH, value='//*[@id="content"]/div/div/div[2]/button[1]')
        first_page.click()
        time.sleep(1)

        room_url_list = []
        for page_number in range(1,full_length+1):
            rooms = self.driver.find_elements(By.CSS_SELECTOR, value='.styled__Card-lyqclu-0 a')
            
            room_url_list += [str(url.get_attribute('href')) for url in rooms]

            if page_number==full_length:
                break
            time.sleep(0.5)

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[2]/button[8]')))
            button_clicker = self.driver.find_element(By.XPATH, value=f'//button[text()="{page_number+1}"]')
            button_clicker.click()
            time.sleep(0.5)
        self.url_list = room_url_list

    def collecting_information(self):
        timeout_urls = []
        for url in self.url_list:
            try:
                self.driver.get(f"{url}")
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'styled__ListContent-mttebe-1')))
                # time.sleep(0.7)
                price = self.driver.find_element(By.CSS_SELECTOR, value='.styled__ListContent-mttebe-1').text
                print(price)
                self.price_per_month_list.append(price)
                address = self.driver.find_element(By.CSS_SELECTOR, value='.styled__Address-ze8x26-1').text
                self.address_list.append(address)
            except TimeoutException:
                timeout_urls.append(url)

        for url in timeout_urls:
            self.url_list.remove(url)

    def to_spread_sheet(self):
        with open('data.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        price_list = data['price']
        address_list = data['address']
        url_list = data['url']

        for n in range(0, len(price_list)-1):
            self.driver.get("https://forms.gle/UxQYHY3AGaDPyRUW7")
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')))
            
            price_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
            price_input.send_keys(price_list[n])

            address_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
            address_input.send_keys(address_list[n])
            
            url_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
            url_input.send_keys(url_list[n])

            submit_button = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            submit_button.click()


        

room_finder = RoomCapture()



room_finder.login()
room_finder.favorite_collector()
room_finder.url_collector()
room_finder.collecting_information()
pprint(room_finder.url_list)
pprint(room_finder.address_list)
pprint(room_finder.price_per_month_list)


pprint(len(room_finder.url_list))
pprint(len(room_finder.address_list))
pprint(len(room_finder.price_per_month_list))


data = {
    "address" : room_finder.address_list,
    "price" : room_finder.price_per_month_list,
    "url" : room_finder.url_list
}

with open ("data.json", 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)


room_finder.to_spread_sheet()
