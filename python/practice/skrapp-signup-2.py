import os
import csv
import time
from selenium import webdriver
# import packages

# open the file
with open('Skrapp Account Creation (Phase 2).csv') as infile:
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
emails = data['Email Id']
passwords = data['Password']
filenames = data['File Name']

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

    # wait a little
    time.sleep(2)

    browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div/div/form/div[3]/div/div/div/button/span').click()

    # wait a little
    time.sleep(3)

    # find New List button
    button = driver.find_element_by_class_name('scroll-sidebar').find_element_by_id('sidebar-list')\
        .find_element_by_tag_name('a')

    # and click on it
    driver.execute_script("arguments[0].click();", button)

    # wait a little
    time.sleep(3)

    # find create list input
    list_input = driver.find_element_by_id('create-list').find_element_by_class_name('input-group-lg')\
        .find_element_by_tag_name('input')

    # clear and enter name
    list_input.clear()
    list_input.send_keys(filenames[i])

    # find create list button
    list_button = driver.find_element_by_id('create-list') \
        .find_element_by_tag_name('button')

    # and click on it
    driver.execute_script("arguments[0].click();", list_button)

    # wait
    time.sleep(5)

    # find account settings
    account = driver.find_element_by_class_name('account').find_element_by_class_name('header-actions').find_element_by_tag_name('a')

    # click on it
    driver.execute_script("arguments[0].click();", account)

    # wait
    time.sleep(1)

    # find logout
    logout = driver.find_element_by_class_name('Logout').find_elements_by_tag_name('a')

    # click on it
    driver.execute_script("arguments[0].click();", logout[4])

    # wait
    time.sleep(1)
    
# close chrome
driver.close()
