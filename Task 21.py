from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the Sauce Demo website
driver.get("https://www.saucedemo.com/")

sleep(3)
# Display cookies before login
print("Cookies before login:")
for cookie in driver.get_cookies():
    print(cookie)

# Perform login
username_input = driver.find_element(By.XPATH,value="//*[@id='user-name']")
password_input = driver.find_element(By.XPATH,value="//*[@id='password']")
login_button = driver.find_element(By.XPATH,value="//*[@id='login-button']")

username_input.send_keys("visual_user")
password_input.send_keys("secret_sauce")
login_button.click()

sleep(3)
# Display cookies after login
print("\nCookies after login:")
for cookie in driver.get_cookies():
    print(cookie)

# Perform logout
logout_button = driver.find_element(By.XPATH, value="//*[@id='react-burger-menu-btn']")
logout_button.click()
sleep(3)
logout_link = driver.find_element(By.XPATH, value="//*[@id='logout_sidebar_link']")
logout_link.click()

# Close the browser
driver.quit()

"""
Output- 
Cookies before login:

Cookies after login:
{'domain': 'www.saucedemo.com', 'expiry': 1711298816, 'httpOnly': False, 'name': 'session-username', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'visual_user'}
"""
