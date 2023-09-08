import json
import login_handler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

### Initialize Driver and Database
#options = webdriver.FirefoxOptions()
#options.add_argument("--headless=new")
driver = webdriver.Firefox()

cookies_file = open("egne_prosjekter/web_automation/social_media_checker/cookies.json")
cookies_data = json.load(cookies_file)
css_selector_file = open("egne_prosjekter/web_automation/social_media_checker/css_selectors.json")
css_selector_data = json.load(css_selector_file)

def is_logged_in(css_selector):

    try:
        login_button = WebDriverWait(driver, 0).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )
        login_value = login_button.is_displayed()
        return login_value
    except:
        return False


def open_website(url):
    driver.get(url)
    website_name = url.split("//")[1]
    print(website_name)
    
    try:
        css_selector = css_selector_data[website_name]["loged_in_element"] # This might be added as a parameter or something
        loged_in = is_logged_in(css_selector)
    except:
        print(f"We do not have a CSS_SELECTOR to keep track of on the website {url}\nPlease add a CSS selector to 'css_selector.json'.")
        loged_in = False

    #try:
    #    driver.add_cookie(cookies_data[website_name])
    #except:
    #    print("This is first time login in, DO LOGIN SCRIPT")


    if loged_in:
        print("Nice you are all good :)")
    else:
        login_handler.login(url, driver)

#test = driver.find_element(By.CSS_SELECTOR, ".DUMMY")
#test.

#open_website("https://rb.no")
open_website("https://instagram.com")
    