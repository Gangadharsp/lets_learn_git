import time

import selenium
from _cffi_backend import string
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://www.google.com/search?client=firefox-b-d&q=facebook")
title=driver.title
print(driver.title)
assert title== "facebook - Google Search"