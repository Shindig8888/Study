from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://python.org/")

upcoming_event_time = driver.find_elements(By.CSS_SELECTOR, value='.list-widgets .last .shrubbery .menu li time')
upcoming_event_name = driver.find_elements(By.CSS_SELECTOR, value='.list-widgets .last .shrubbery .menu li a')

event_time_list = [item.get_attribute("datetime").split("T")[0] for item in upcoming_event_time]
event_name_list = [name.text for name in upcoming_event_name]

dic = {str(n): {'time': event_time_list[n], 'name': event_name_list[n]} for n in range(0, len(event_name_list)-1)}

pprint(dic)




driver.quit()