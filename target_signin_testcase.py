# Test Case: User can navigate to the signin page
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

#  open the url
driver.get('https://www.target.com')

# Click SignIn button
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

# Click SignIn from side navigation
driver.find_element(By.XPATH, "//span[contains(@class, 'ListItemText') and text()='Sign in']")

# Verify SignIn page opened: “Sign in to your Target account” text is shown,
driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")


driver.find_element(By.ID, 'login')
sleep(8)
