from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://www.google.com")
driver.maximize_window()
print(driver.current_url)
print(driver.title)






#time.sleep(2)