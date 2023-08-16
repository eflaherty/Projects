from selenium import webdriver

driver_path = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(driver_path)
browser.get('http://selenium.dev/') 
