# creating CSS locators and registration strategies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Step 1 get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# Step 2 create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


# Step 3 open the url
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%2F%3F_encoding%3DUTF8%26crid%3D28AXJJ8ZHMJR6%26k%3Dno%2520shave%2520november%26ref%3Dnb_sb_ss_ts-doa-p_2_8%26sprefix%3Dno%2520shave%252Caps%252C174%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')


# create a css locator for the amazon logo
driver.find_element(By.CSS_SELECTOR, "i[class='a-icon a-icon-logo']")

# create a css locator for Create account text
driver.find_element(By.CSS_SELECTOR, "h1[class='a-spacing-small']")

# create a css locator for  name input
driver.find_element(By.CSS_SELECTOR, "input[placeholder='First and last name']")

# create a css locator for mobile number or email
driver.find_element(By.CSS_SELECTOR, "input[type='email']")

# create a css locator for the password input
driver.find_element(By.CSS_SELECTOR, "input[id='ap_password']")

# create a css locator for Passwords must be at least 6 char
driver.find_element(By.CSS_SELECTOR, "div[class='a-alert-content']")

# create a css locator for re-enter password
driver.find_element(By.CSS_SELECTOR, "input[id='ap_password_check']")

# create a css locator for the continue button
driver.find_element(By.CSS_SELECTOR, "input[class='a-button-input']")

# create a css locator for conditions of use
driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")

# create a css locator for privacy notice
driver.find_element(By.CSS_SELECTOR, "a[href*='privacy_notice']")

# create a css locator for sign in link
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?']")

sleep(4)
