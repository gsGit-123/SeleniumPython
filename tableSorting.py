from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on coloum header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

#collect veggies name (browser sorted names)
vegwebelements = driver.find_elements(By.XPATH,"//tr/td[1]")