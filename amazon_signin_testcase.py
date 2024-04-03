# creating locators and search strategies
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
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%3Fk%3Dno%2Bshave%2Bnovember%26crid%3D28AXJJ8ZHMJR6%26sprefix%3Dno%2Bshave%252Caps%252C174%26ref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Step 4 create a locator for the Amazon logo
driver.find_element(By.XPATH, "//a[@class='a-link-nav-icon']")

# Step 5 create a locator for the email field
driver.find_element(By.XPATH, "//input[@type='email']")

# Step 6 create a locator for the continue button
driver.find_element(By.XPATH, "//input[@class='a-button-input']")

# Step 7 create a locator for the Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# Step 8 create a locator for the Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# Step 9 create a locator for the Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Step 10 create a locator for forgot your password link
driver.find_element(By.XPATH, "//a[@class='a-link-normal']")

# Step 11 create a locator for Other issues with Sign-In Link
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")

# Step 12 create a locator for creating your Amazon account
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")
sleep(8)
