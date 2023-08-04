import time

import selenium
from _cffi_backend import string
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://www.facebook.com/login/")
title=driver.title
print(driver.title)
print("new added for git")

assert title== "Log in to Facebook"

driver.find_element(By.XPATH, "//input[@id='email']").send_keys("123")

