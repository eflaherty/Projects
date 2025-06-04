import os
import csv
import time
from selenium import webdriver
# import packages

# open the file
with open('Test Accounts.csv') as infile:
    # read the file as a dictionary for each row ({header : value})
    reader = csv.DictReader(infile)
    data = {}
    for row in reader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]

# extract the variables you want
emails = data['Email Address']
passwords = data['Password']


# when chromedriver.exe in a folder with a script
dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
# driver.maximize_window()

# iterate over users
for i in range(len(emails)):

    # Navigate to the application home page
    driver.get("https://www.skrapp.io/login")

    # wait some time
    time.sleep(1)

    # find input fields
    inputs = driver.find_elements_by_tag_name('input')

    # clear and enter email
    inputs[0].clear()
    inputs[0].send_keys(emails[i])

    # clear and enter password
    inputs[1].clear()
    inputs[1].send_keys(passwords[i])

    # enter submit
    inputs[2].click()

    # wait a little
    time.sleep(3)

    # find buttons
    buttons = driver.find_element_by_class_name('list-actions').find_elements_by_tag_name('button')

    # and click on export
    driver.execute_script("arguments[0].click();", buttons[1])

    # wait a little
    time.sleep(1)

    # find checkbox
    checkbox = driver.find_element_by_class_name('dropdown-checkbox').find_element_by_tag_name('input')

    # and click on it
    driver.execute_script("arguments[0].click();", checkbox)

    # wait some time
    time.sleep(1)

    # find a list
    tags = driver.find_element_by_class_name('open').find_element_by_tag_name('ul').find_elements_by_tag_name('a')

    # and click on export xlsx
    driver.execute_script("arguments[0].click();", tags[1])

    # wait to download it
    time.sleep(10)

    # find account settings
    account = driver.find_element_by_class_name('account').find_element_by_class_name('header-actions').find_element_by_tag_name('a')

    # click on it
    driver.execute_script("arguments[0].click();", account)

    # wait
    time.sleep(1)

    # find logout
    logout = driver.find_element_by_class_name('cog-box').find_elements_by_tag_name('a')

    # click on it
    driver.execute_script("arguments[0].click();", logout[4])

    # wait
    time.sleep(1)
    
# close chrome
driver.close()


