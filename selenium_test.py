import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#visit the website url
driver.get("https://automationplayground.com/crm/login.html")
time.sleep(5)

#Login with a valid email address
driver.find_element(By.ID, "email-id").send_keys("obellotope@gmail.com")
time.sleep(5)

#Enter password
driver.find_element(By.ID,"password").send_keys("Qwerasd12@")
time.sleep(5)

#Click on "remember me"
driver.find_element(By.ID, "remember").click()
time.sleep(5)

#Click the submit button
driver.find_element(By.ID, "submit-id").click()
time.sleep(5)

#Click on "new customers"
driver.find_element(By.ID, "new-customer").click()
time.sleep(5)

#input new customer email address
driver.find_element(By.ID, "EmailAddress").send_keys("sundaynight@gmail.com")
time.sleep(5)

#input first name of customer
driver.find_element(By.ID, "FirstName").send_keys("sunday")
time.sleep(5)

#input last name of the new customer
driver.find_element(By.ID, "LastName").send_keys("night")
time.sleep(5)

#input city
driver.find_element(By.ID, "City").send_keys("Ikeja")
time.sleep(5)

#input state
driver.find_element(By.ID, "StateOrRegion").send_keys("Lagos")
time.sleep(5)

#Select gender type
driver.find_element(By.XPATH,"//*[@id='loginform']/div/div/div/div/form/div[6]/input[2]").click()
time.sleep(5)

#Check the "Add to promotional list" button
driver.find_element(By.XPATH, "//*[@id='loginform']/div/div/div/div/form/div[7]/input").click()
time.sleep(5)

#Click on Submit
driver.find_element(By.XPATH, "//*[@id='loginform']/div/div/div/div/form/button").click()
time.sleep(5)

#Click on sign out
driver.find_element(By.XPATH, "/html/body/nav/ul/li/a").click()
time.sleep(5)