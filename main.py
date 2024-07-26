from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Firefox()
browser.implicitly_wait(5)

# Opening Instagram
try:
    browser.get("https://www.instagram.com/")
    print("Opened Instagram.")

    browser.implicitly_wait(5)

    # login credentials
    username_input = browser.find_element(By.NAME, "username")
    password_input = browser.find_element(By.NAME, "password")

    username_input.send_keys("alguitarmailbox@gmail.com")
    password_input.send_keys("Guitar123456")

    # Finding Login button
    try:
        login_link = browser.find_element(By.XPATH, "//button/div[text()='Log in']")
    except Exception as e:
        print("Error finding login button:", repr(e))

    # Clicking on Login button
    try:
        login_link.click()
    except Exception as e:
        print("Error clicking login button:", repr(e))


except Exception as e:
    print("Error opening Instagram:", repr(e))

sleep(2)
browser.close()
print("Browser closed.")

quit()
