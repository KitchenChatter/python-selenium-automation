from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@then('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "span[class*='styles__LinkText']").click()


@when('Open navigation menu, click Sign in')
def open_navigation_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()


@then('Verify Sign into your Target account')
def verify_signin_into_account(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading']").text
    assert 'Sign into your Target account' in actual_text, (f'Error! Text Sign into your Target account not in '
                                                            f'{actual_text}')


sleep(6)
