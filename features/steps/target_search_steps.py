from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when("Search for 'ipad'")
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('ipad')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)


@then('Verify search results are shown')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert 'ipad' in actual_text, f'Error! Text ipad not in {actual_text}'