from selenium import webdriver
from selenium.webdriver.common.by import By
import time

name = "Gunjan"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR,"#alertbtn  ").click()
time.sleep(5)


# Use below to switch from alert (from javascript alert to webdriver)

alert = driver.switch_to.alert
print(alert.text)
alert.accept()
