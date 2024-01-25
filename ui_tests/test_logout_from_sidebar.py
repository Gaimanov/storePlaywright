import allure

from pages.LoginPage import LoginPage
from pages.MainPage import MainPage


@allure.feature("logout")
@allure.story("logout from sidebar menu")
@allure.description("Logging out of app through the burger menu on the main page")
@allure.link("https://saucedemo.atlassian.net/browse/PRD-126")
def test_logout_from_sidebar_menu(driver):
    """
    Test logs in, opens a burger menu, clicks logout option and verifies it is back on login page
    """
    _ = LoginPage(driver)
    page = MainPage(driver)
    page.open_burger_menu()
    page.click(page.SIDEBAR_LOGOUT)
    with allure.step("logout successful"):
        assert page.is_element_present(LoginPage.LOGIN_BUTTON), f"Element {LoginPage.LOGIN_BUTTON} was not found"
