from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("headless")
driver = webdriver.Chrome(options=chromeOptions)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")
time.sleep(5)