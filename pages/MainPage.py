from typing import Any

from pages.BasePage import BasePage


class MainPage(BasePage):
    LOGO = ".app_logo"
    BURGER_BUTTON = '#react-burger-menu-btn'
    CART_BUTTON = '#shopping_cart_container'
    SORTING_BUTTON = ".product_sort_container"
    SORTING_CONTAINER = '[data-test="product_sort_container"]'
    SIDEBAR_ALL_ITEMS = "#inventory_sidebar_link"
    SIDEBAR_ABOUT = "#about_sidebar_link"
    SIDEBAR_LOGOUT = "#logout_sidebar_link"
    SIDEBAR_RESET_APP = "#reset_sidebar_link"
    PRODUCT_TILE = '[class="inventory_item"]'
    ADD_TO_CART_BUTTON = '[id*="add-to-cart"]'
    REMOVE_FROM_CART_BUTTON = '[id*="remove-"]'
    ACTIVE_SORTING = '[class="active_option"]'
    SORT_OPTIONS = {
        ("name", "az"): (0, "Name (A to Z)"),
        ("name", "za"): (1, "Name (Z to A)"),
        ("price", "lh"): (2, "Price (low to high)"),
        ("price", "hl"): (3, "Price (high to low)")
    }

    def __init__(self, driver: Any):
        super().__init__(driver)
        self.page = driver

    def sort_goods(self, sort_by: str, param: str) -> None:
        self.page.locator(self.SORTING_BUTTON).click()
        self.page.wait_for_selector(self.SORTING_CONTAINER, state="visible")
        option = self.SORT_OPTIONS.get((sort_by, param))
        if option:
            # Type the arrow down key x times
            for _ in range(option[0]):
                self.page.keyboard.press("ArrowDown")
            # Press the Enter key
            self.page.keyboard.press("Enter")
            # Verifying sorting was successful
            element = self.page.locator(self.ACTIVE_SORTING).inner_text()
            assert element == option[1], f"Expected sorting: '{option[1]}', Actual sorting: '{element}'"
        else:
            raise ValueError(f"Invalid sort_by and param combination: {sort_by}, {param}")

    def add_product_to_cart(self, product_index: int) -> None:
        tile = self.page.locator(f'{self.PRODUCT_TILE}:nth-of-type({product_index})')
        tile.locator(self.ADD_TO_CART_BUTTON).click()

    def goto_product_details(self, name: str) -> None:
        self.click(f'//div[@class="inventory_item_name" and text()="{name}"]')

    def goto_cart(self) -> None:
        self.click(self.CART_BUTTON)

    def open_burger_menu(self) -> None:
        self.click(self.BURGER_BUTTON)
        self.page.wait_for_selector('.bm-menu-wrap[aria-hidden="false"]')

    def goto_all_items(self) -> None:
        self.open_burger_menu()
        self.click(self.SIDEBAR_ALL_ITEMS)

    def goto_about(self) -> None:
        self.open_burger_menu()
        self.click(self.SIDEBAR_ABOUT)

    def logout(self) -> None:
        self.open_burger_menu()
        self.click(self.SIDEBAR_LOGOUT)

    def reset_app_state(self) -> None:
        self.open_burger_menu()
        self.click(self.SIDEBAR_ALL_ITEMS)
