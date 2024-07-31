from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pickle

browser = webdriver.Firefox()
browser.implicitly_wait(5)

# Opening Instagram
try:
    browser.get("https://www.instagram.com/accounts/login/?hl=en")
    print("Opened Instagram.")

    browser.implicitly_wait(5)

    # login credentials
    print("finding login credentials")
    username_input = browser.find_element(By.NAME, "username")
    password_input = browser.find_element(By.NAME, "password")

    print("sending login credentials")
    username_input.send_keys("alguitarmailbox@gmail.com")
    password_input.send_keys("Guitar123456")

    # Finding Login button
    try:
        login_link = browser.find_element(By.XPATH, "//button/div[text()='Log in']")
    except Exception as e:
        print("Error finding login button:", repr(e))

    # Clicking on Login button
    print("clicking login button")
    try:
        login_link.click()
    except Exception as e:
        print("Error clicking login button:", repr(e))

    # Wait for 2FA to load
    while True:
        if "two_factor" not in browser.current_url:
            print("waiting for 2FA to load...")
            sleep(1)
        else:
            break

    # 2FA
    print(browser.current_url)
    if "two_factor" in browser.current_url:
        print("Two factor authentication required.")
        while True:
            # Await Two factor authentication
            if "two_factor" not in browser.current_url:
                break
            else:
                print("waiting...")
                sleep(1)
    sleep(1)

    # Unneeded code
    # # Don't Save login info
    # try:
    #     dont_save_login_info = browser.find_element(By.XPATH, "//div[text()='Not now']")
    #     dont_save_login_info.click()
    # except Exception as e:
    #     print("Error while clicking dont save login info:", repr(e))

    # # Don't turn on notifications
    # while True:
    #     try:
    #         dont_turn_on_notifications = browser.find_element(
    #             By.XPATH, "//button[text()='Not Now']"
    #         )
    #         dont_turn_on_notifications.click()
    #         break
    #     except Exception as e:
    #         print("Error while clicking dont turn on notifications:", repr(e))

    # Opening Post
    try:
        post_url = "https://www.instagram.com/p/C-BfopEy9j8/"
        browser.get(post_url)
        print("Opened post.")
    except Exception as e:
        print("Error opening post:", repr(e))

    # getting all comments
    try:
        comment_classes = "x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"
        comments = browser.find_elements(
            By.CSS_SELECTOR, f"div[class*='{comment_classes}']"
        )
        print("Found comments:", len(comments))
        with open("data/comments.txt", "w", encoding="utf-8") as f:
            for comment in comments:
                f.write(comment.text + "\n")
    except Exception as e:
        print("Error finding comments:", repr(e))

except Exception as e:
    print("Error opening Instagram:", repr(e))

# sleep(10)
# browser.close()
# print("Browser closed.")

quit()
