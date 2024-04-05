from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@then("Search for 'Click on cart icon'")
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('cart icon')
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='cart 0 items']").click()
    sleep(6)


@then('Verify "Your cart is empty"')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert 'Cart' in actual_text, f'Error! Text ipad not in {actual_text}'
