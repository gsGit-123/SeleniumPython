from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

#you can find elements using ID, classname, name, Xpath, CSSSelector, linkText

# xath syntax: //tagname[@attribute='value] -> eg. //input[@type='submit']
# CSSSelector syntax: tagname[@attribute='value] -> eg. //input[@type='submit']
# shortcut for css  using id then just write #id
# shortcut for css  using id then just write .class

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
#driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

# Static dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(0)
# Static dropdown

#message = driver.find_element(By.CLASS_NAME,"alert-success").text
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("g")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("gvs@gamil.com")
#driver.find_element(By.CSS_SELECTOR,"input[id='exampleInputPassword1']").send_keys("456123")
driver.find_element(By.XPATH,"//input[@id= 'inlineRadio2']").click()

driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("123546789")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
#print(message)

#assert "Success" in message



time.sleep(100)