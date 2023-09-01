from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def rb_login(driver): ### PLAN IS TO WAIT FOR USER TO TYPE INPUT, LIKE EXAMPLE WAIT TO BE REDIRECTED BACK TO "https://www.rb.no"
    print("You are entering the RB Login script")
    driver.get("https://www.aid.no/aid/logg_inn/www.rb.no?context=ego_top&requestedUrl=https%3A%2F%2Fwww.aid.no%2Faid%2Flogg_inn%2Fwww.rb.no%2Fforbered_lokal_sesjon%3Fcontext%3Dego_top%26requestedUrl%3Dhttps%253A%252F%252Fwww.aid.no%252Faid%252Flogg_inn%252Fwww.rb.no%252Flogg_inn_ferdig%253Fcontext%253Dego_top%2526intent_id%253Dd3c0da87-45cb-40d7-90ad-a8cd711b5ec0%2526intent_type%253Dlogin%2526requestedUrl%253Dhttps%25253A%25252F%25252Fwww.rb.no%25252F&ts=1693506908")
    rb_tlf = driver.find_element(By.CSS_SELECTOR, "div.svelte-j0jdnu:nth-child(6) > label:nth-child(1) > input:nth-child(3)")
    rb_tlf.send_keys("")

    rb_login_button = driver.find_element(By.CSS_SELECTOR, ".prio > button:nth-child(1)")
    rb_login_button.click()

    rb_password = driver.find_element(By.CSS_SELECTOR, "div.svelte-j0jdnu:nth-child(7) > label:nth-child(1) > input:nth-child(3)")
    rb_password.send_keys("")
    rb_login_button.click()

def instagram_login(driver):
    print("You are entering the Instagram Login script")

    decline_cookies_button = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button._a9--:nth-child(3)"))
        )
    decline_cookies_button.click()

    ### MAKE IT CHANGE THE INSTAGRAM IMAGE TO YOUR OWN CUSTOM HEADER :) EZ...
    instagram_heading = driver.find_element(By.CSS_SELECTOR, ".xseo6mj > div:nth-child(1) > i:nth-child(1)") 
    instagram_heading


def login(url, driver):
    url_name = url.split("//")[1]

    match url_name:
        case "rb.no":
            rb_login(driver)
        case "instagram.com":
            instagram_login(driver)

