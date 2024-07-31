from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

#you can find elements using ID, classname, name, Xpath, CSSSelector, linkText

# xath syntax: //tagname[@attribute='value] -> eg. //input[@type='submit']
# CSSSelector syntax: tagname[@attribute='value] -> eg. //input[@type='submit']
# shortcut for css  using id then just write #id
# shortcut for css  using class then just write .class

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()

