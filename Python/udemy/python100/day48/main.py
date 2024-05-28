from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, value="cookie")


buyCursor = driver.find_element(By.ID, value="buyCursor")
buyGrandma = driver.find_element(By.ID, value="buyGrandma")
buyFactory = driver.find_element(By.ID, value="buyFactory")
buyMine = driver.find_element(By.ID, value="buyMine")
buyShipment = driver.find_element(By.ID, value="buyShipment")
buyAlchemy = driver.find_element(By.ID, value="buyAlchemy lab")
buyPortal = driver.find_element(By.ID, value="buyPortal")
buyTime_machine = driver.find_element(By.ID, value="buyTime machine")
buyElder_Pledge = driver.find_element(By.ID, value="buyElder Pledge")


timeout = time.time()+0.5


while True:
    currenttime = time.time()
    cookie.click()
    money = int(driver.find_element(By.ID, value="money").text)

    if time.time() > timeout:
        try:
            if money >= 123_456_789:
                buyTime_machine.click()
                continue
            elif money >= 1_000_000:
                buyPortal.click()
                continue
            elif money >= 50_000:
                buyAlchemy.click()
                continue
            elif money >= 7_000:
                buyShipment.click()
                continue
            elif money >= 2_000:
                buyMine.click()
                continue
            elif money >= 500:
                buyFactory.click()
                continue
            elif money >= 100:
                buyGrandma.click()
                continue
            elif money >= 15:
                buyCursor.click()
                continue
        except:
            continue
        timeout = time.time() + 0.5
    # time.sleep(0.01)