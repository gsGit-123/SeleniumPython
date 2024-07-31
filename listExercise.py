from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(5)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)

productValues = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
productName = []

for result in results:
   productName.append(result.find_element(By.XPATH,"h4").text)
   result.find_element(By.XPATH, "div/button").click()
   #productName.append(result.text)

print(productName)
assert productName == productValues