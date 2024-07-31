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

assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
discountAmt = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert discountAmt < totalAmount

prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
summation = 0
for price in prices:
    summation = summation + int(price.text)

print(summation)


assert summation == totalAmount





