from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#you can find elements using ID, classname, name, Xpath, CSSSelector, linkText

# xath syntax: //tagname[@attribute='value] -> eg. //input[@type='submit']
# CSSSelector syntax: tagname[@attribute='value] -> eg. //input[@type='submit']
# shortcut for css  using id then just write #id
# shortcut for css  using class then just write .class

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
time.sleep(5)
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        break

radiobuttons = driver.find_elements(By.XPATH,"//input[@type= 'radio']")
print(len(radiobuttons))

for radibutton in radiobuttons:
    if radibutton.get_attribute("value") == "radio2":
        radibutton.click()
        break




