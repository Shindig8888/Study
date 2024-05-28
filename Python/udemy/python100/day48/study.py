from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


# driver.get("https://www.amazon.com/Pattern-Fashion-Packable-Outdoor-Fisherman/dp/B098QT3TMB/ref=sr_1_7?crid=DEPYYJ6MRH0Y&dib=eyJ2IjoiMSJ9.vDXQXv6BjkZ7E1uLCu9yv-1e0iQ5xVvBlYCKIlZEiNoCd8eCUegLnpt-9d05fwhBj8cygrnoq7lU_0DOyo_WJJW80kfZGXZ7J7Kd4gO0hYgTAEsympbNV8W_odQCJS4OFAuAvMX0b7Kghv3Cjx8RimolIEO1uiNBHoTmkvCwGacHB0Uj-Mb2e4SnN9qXfCsI4Ip3IK_DvEcy2cm3T4zcL27ucYsA-crquWFA2xvhl48Zgdit_Wg2ia-EyrEas_9TSFP7ZB8GGln5aUKwQvZSgvZ2_Hc-fCsBf7Sg_bGDGZI.uAL9VPeQ4JeeN_DMVJgNW-huLlKU2C_wTltMAJqTegM&dib_tag=se&keywords=duck&qid=1716779984&sprefix=du%2Caps%2C327&sr=8-7")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

# print(price_dollar)
# print(price_cents)

driver.get("https://python.org/")

# search_bar = driver.find_element(By.NAME, value="q")
# button = driver.find_element(By.ID, value="submit")
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

print(bug_link.text)


driver.quit()