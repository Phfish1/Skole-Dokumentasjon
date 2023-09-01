from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

### Webdriver configuration
driver = webdriver.Firefox()
#driver.maximize_window()


### Login RB
driver.get("https://www.aid.no/aid/logg_inn/www.rb.no?context=ego_top&requestedUrl=https%3A%2F%2Fwww.aid.no%2Faid%2Flogg_inn%2Fwww.rb.no%2Fforbered_lokal_sesjon%3Fcontext%3Dego_top%26requestedUrl%3Dhttps%253A%252F%252Fwww.aid.no%252Faid%252Flogg_inn%252Fwww.rb.no%252Flogg_inn_ferdig%253Fcontext%253Dego_top%2526intent_id%253Dd3c0da87-45cb-40d7-90ad-a8cd711b5ec0%2526intent_type%253Dlogin%2526requestedUrl%253Dhttps%25253A%25252F%25252Fwww.rb.no%25252F&ts=1693506908")
rb_tlf = driver.find_element(By.CSS_SELECTOR, "div.svelte-j0jdnu:nth-child(6) > label:nth-child(1) > input:nth-child(3)")
rb_tlf.send_keys("")

rb_login_button = driver.find_element(By.CSS_SELECTOR, ".prio > button:nth-child(1)")
rb_login_button.click()

rb_password = driver.find_element(By.CSS_SELECTOR, "div.svelte-j0jdnu:nth-child(7) > label:nth-child(1) > input:nth-child(3)")
rb_password.send_keys("")
rb_login_button.click()

### Login Instagram
body = driver.find_element(By.CSS_SELECTOR, "#frontpage")
body.send_keys(Keys.LEFT_CONTROL + "t")
#driver.get("https://instagram.com")

