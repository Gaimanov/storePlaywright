from typing import Any

from pages.MainPage import MainPage


class CartPage(MainPage):

    NAME = '[class="inventory_item_name"]'
    QUANTITY = '[class="cart_quantity"]'
    DESCRIPTION = "#inventory_item_desc"
    PRICE = '[class="inventory_item_price"]'
    CHECKOUT = "#checkout"
    CONTINUE_SHOPPING = "#continue-shopping"

    def __init__(self, driver: Any):
        super().__init__(driver)
        self.page = driver

    def get_product_price(self, index: int) -> str:
        price = self.page.locator(f'{self.PRICE}:nth-of-type({index})').text
        return price

    def get_product_description(self, index: int) -> str:
        desc = self.page.locator(f'{self.DESCRIPTION}:nth-of-type({index})').text
        return desc

    def get_product_quantity(self, index: int) -> str:
        qty = self.page.locator(f'{self.QUANTITY}:nth-of-type({index})').text
        return qty

    def get_product_name(self, index: int) -> str:
        name = self.page.locator(f'{self.NAME}:nth-of-type({index})').text
        return name

    def go_to_checkout(self) -> None:
        self.page.locator(self.CHECKOUT).click()
