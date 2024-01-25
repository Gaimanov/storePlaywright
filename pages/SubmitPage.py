from typing import Any

from pages.MainPage import MainPage


class SubmitPage(MainPage):
    FINISH = "#finish"
    CANCEL = "#cancel"

    def __init__(self, driver: Any):
        super().__init__(driver)
        self.page = driver

    def finish_checkout(self) -> None:
        self.page.locator(self.FINISH).click()
