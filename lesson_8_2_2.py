from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select

# imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import time

# Exercise #2
#
# Add code for 'My Account' in the top menu that will:
# -Verify that you are able to land on the Registration form after selecting the ‘Register’ option.
# -Select the ‘Login’ option and verify that you are able to land on the login page.

# May 12th, 2021
# student Evgeny Abdulin

# driver = webdriver.Chrome(executable_path='drivers/chromedriver')
# to start Firefox use the line below
driver = webdriver.Firefox(executable_path='drivers/geckodriver')
# driver = webdriver.Firefox(executable_path=r'drivers/geckodriver/geckodriver')
driver.get("https://techskillacademy.net/brainbucket/")

driver.maximize_window()  # maximizing the browser window

# going to Registration form
account_link = WebDriverWait(driver, 10).\
    until(ec.element_to_be_clickable((By.XPATH, "//span[contains(.,'My Account')]")))
account_link.click()
register_link = WebDriverWait(driver, 10).\
    until(ec.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Register')]")))
register_link.click()
# checking if title Register Account is visible
register_title = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h1")))

# back to Home page with some delay to be able to see what was done on the page
time.sleep(2)
driver.back()

# going to Login form
account_link = WebDriverWait(driver, 10).\
    until(ec.element_to_be_clickable((By.XPATH, "//span[contains(.,'My Account')]")))
account_link.click()
login_link = WebDriverWait(driver, 10).\
    until(ec.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Login')]")))
login_link.click()
# checking if title Register Account is visible
login_title = WebDriverWait(driver, 10).\
    until(ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Returning Customer')]")))

# add some sleep time to be able to see the result
time.sleep(5)

driver.quit()
