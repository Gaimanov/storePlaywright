from typing import Any

from pages.MainPage import MainPage


class CheckOutPage(MainPage):
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE = "#continue"

    def __init__(self, driver: Any):
        super().__init__(driver)
        self.page = driver

    def fill_in_first_name(self, first_name: str) -> None:
        self.page.locator(self.FIRST_NAME).type(first_name)

    def fill_in_last_name(self, last_name: str) -> None:
        self.page.locator(self.LAST_NAME).type(last_name)

    def fill_in_zip_code(self, zip_code: str) -> None:
        self.page.locator(self.POSTAL_CODE).type(zip_code)

    def click_continue(self) -> None:
        self.page.locator(self.CONTINUE).click()

    def fill_out_checkout_form(self,
                               first_name: str,
                               last_name: str,
                               zip_code: str,
                               click_continue: bool = False) -> None:
        self.fill_in_first_name(first_name)
        self.fill_in_last_name(last_name)
        self.fill_in_zip_code(zip_code)
        if click_continue:
            self.click_continue()



