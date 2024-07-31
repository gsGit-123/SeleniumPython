import timer
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#you can find elements using ID, classname, name, Xpath, CSSSelector, linkText

# xath syntax: //tagname[@attribute='value] -> eg. //input[@type='submit']
# CSSSelector syntax: tagname[@attribute='value] -> eg. //input[@type='submit']
# shortcut for css  using id then just write #id
# shortcut for css  using id then just write .class

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
#driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("Hello@123")

driver.find_element(By.XPATH,"//input[@type= 'submit']").click()
time.sleep(5)