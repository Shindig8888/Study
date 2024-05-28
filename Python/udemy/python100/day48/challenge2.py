from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(r"https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EB%8C%80%EB%AC%B8")

how_many = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/div[1]/div/p[2]/span/a[1]/abbr/span/b').text
print(how_many)




driver.quit()