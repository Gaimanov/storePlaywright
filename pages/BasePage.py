

class BasePage:

    def __init__(self, driver):
        self.page = driver

    def is_element_present(self, selector: str) -> bool:
        element = self.page.wait_for_selector(selector)
        return element is not None

    def is_text_present(self, selector: str, expected_text: str, equal_or_contains: str = "equal") -> bool:
        actual_text = self.page.wait_for_selector(selector).inner_text()
        if equal_or_contains == "equal":
            return expected_text == actual_text
        else:
            return expected_text in actual_text

    def click(self, element: str) -> None:
        self.page.locator(element).click()

