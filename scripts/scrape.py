from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


def scrape(email_login, password_login, post_url):

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
        username_input.send_keys(email_login)
        password_input.send_keys(password_login)

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

        # Opening Post
        try:
            post_url = post_url
            browser.get(post_url)
            print("Opened post.")
        except Exception as e:
            print("Error opening post:", repr(e))

        # getting all comments
        try:
            comment_classes = "x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli x1q0g3np xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"
            comments = browser.find_elements(
                By.CSS_SELECTOR, f"div[class*='{comment_classes}']"
            )
            print("Found elements:", len(comments))
            # saving comments
            data = []
            for comment in comments:
                data.append(comment.text)
            df = pd.DataFrame(data, columns=["Comments"])
            df = df.drop(index=0)
            df = df['Comments'].str.split('\n', expand=True)
            df.to_csv("data/comments.csv", index=False)

        except Exception as e:
            print("Error finding comments:", repr(e))

    except Exception as e:
        print("Error opening Instagram:", repr(e))

    browser.close()
    print("Browser closed.")

    quit()


email = "alguitarmailbox@gmail.com"
password = "Guitar123456"
post_url = "https://www.instagram.com/p/C-HPL2mSrFV/"

scrape(email, password, post_url)
