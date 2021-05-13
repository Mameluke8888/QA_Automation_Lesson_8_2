from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select

# imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import time

# Exercise #1
#
# Add code for Registration Page that will:
# -Select your state from the Region/State dropdown
# -Check “I have read and agree to the Privacy Policy”
# -Select “No” in the subscription

# May 12th, 2021
# student Evgeny Abdulin

# driver = webdriver.Chrome(executable_path='drivers/chromedriver')
# to start Firefox use the line below
driver = webdriver.Firefox(executable_path='drivers/geckodriver')
# driver = webdriver.Firefox(executable_path=r'drivers/geckodriver/geckodriver')
driver.get("https://techskillacademy.net/brainbucket/index.php?route=account/login")

driver.maximize_window()  # maximizing the browser window

# sending a password to a login page
password_login_input = driver.find_element_by_id("input-password")
password_login_input.clear()
password_login_input.send_keys("password")

# clicking a button to go to the registration page, waiting until clickable
# new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")
new_registrant_btn = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH,
                                                                                 "//a[contains(text(), 'Continue')]")))
new_registrant_btn.click()

# checking if title Register Account is visible
register_title = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h1")))


# filling fields/checking 'required' on the registration page
def filling_field(f_xpath, f_id, f_keys, assert_needed=False):
    if assert_needed:
        field = driver.find_element_by_xpath(f_xpath)
        field_class = field.get_attribute("class")
        assert "required" in field_class
    f_input = driver.find_element_by_id(f_id)
    f_input.clear()
    f_input.send_keys(f_keys)


fields = [
    ("input-firstname", "//fieldset/div[2]", "Evgeny", True),
    ("input-lastname", "//fieldset/div[3]", "Abdulin", True),
    ("input-email", "//fieldset/div[4]", "abdulin.evgeny@gmail.com", True),
    ("input-telephone", "//fieldset/div[5]", "512-888-8888", True),
    ("input-fax", "", "512-999-9999", False),
    ("input-company", "", "Texas State University", False),
    ("input-address-1", "//fieldset[2]/div[2]", "601 University Drive", True),
    ("input-address-2", "", "Apt X", False),
    ("input-city", "//fieldset[2]/div[4]", "San Marcos", True),
    ("input-postcode", "", "78666-4684", False),
    ("input-password", "//fieldset[3]/div[1]", "superpassword", True),
    ("input-confirm", "//fieldset[3]/div[2]", "superpassword", True)]

for field in fields:
    filling_field(field[1], field[0], field[2], field[3])

# Exercise #1

# selecting region/state
state_dropdown = driver.find_element_by_id("input-zone")
state_dropdown_select = Select(state_dropdown)
state_dropdown_select.select_by_visible_text("Texas")

# agree to privacy policy
agree_btn = driver.find_element_by_xpath("//input[@name='agree']")
if not agree_btn.is_selected():
    agree_btn.click()

# NO to subscription
subscribe_btn = driver.find_element_by_xpath("//input[@name='newsletter' and @value='0']")
if not subscribe_btn.is_selected():
    subscribe_btn.click()

continue_btn = driver.find_element_by_xpath("//input[@value='Continue']")

# getting the background color of Continue button
background_color = continue_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'

# add some sleep time to be able to see the result
time.sleep(5)

driver.quit()
