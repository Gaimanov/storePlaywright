from typing import Union, Any

from pages.MainPage import MainPage


class ProductPage(MainPage):

    BACK_TO_PRODUCTS = "#back-to-products"
    PRODUCT_NAME = '[class="inventory_details_name large_size"]'
    PRODUCT_DESCRIPTION = '[class="inventory_details_desc large_size"]'
    PRODUCT_PRICE = '[class="inventory_details_price"]'

    def __init__(self, driver: Any):
        super().__init__(driver)
        self.page = driver

    def get_product_name(self) -> str:
        name = self.page.locator(self.PRODUCT_NAME).text()
        return name

    def get_product_description(self) -> str:
        desc = self.page.locator(self.PRODUCT_DESCRIPTION).text()
        return desc

    def get_product_price(self, price_type: Union[str, int] = str) -> Union[str, int]:
        price = self.page.locator(self.PRODUCT_DESCRIPTION).text()
        if callable(price_type):
            return price_type(price)
        else:
            raise TypeError("price_type must be callable")

    def back_to_products(self) -> None:
        self.page.locator(self.BACK_TO_PRODUCTS).click()

    def add_to_cart(self) -> None:
        self.page.locator(self.ADD_TO_CART_BUTTON).click()
