from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=4DC3J2RVS6HW&sprefix=laptop%2Caps%2C224&ref=nb_sb_noss_2")

elem=driver.find_element(By.CLASS_NAME,"puis-card-container")
print(elem.get_attribute("outerHTML"))
time.sleep(2)
driver.close()