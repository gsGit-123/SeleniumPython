from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(5)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break
else:
    print("not")

#-----------get_attribute-----------

# get_attribute will use to get text which are updated dynamically
# like from dropdown we have selected india. so, to get text in this kind of case use get_attribute
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"

#-----------get_attribute-----------
