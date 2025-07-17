from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start browser
driver = webdriver.Chrome()

# Go to GitHub login page
driver.get("https://github.com/login")
time.sleep(2)

# Enter username and password
driver.find_element(By.ID, "login_field").send_keys("kumvansh2005")
driver.find_element(By.ID, "password").send_keys("vanshKum")

# Press Enter to log in
driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
time.sleep(20)

# Close browser
driver.quit()
