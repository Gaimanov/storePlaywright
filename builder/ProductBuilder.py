from typing import Any

from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.ProductPage import ProductPage
from pages.CheckOutPage import CheckOutPage
from pages.SubmitPage import SubmitPage


class ProductBuilder:
    def __init__(self, driver: Any):
        self.page = driver
        self.main_page = MainPage(driver)
        self.product_page = ProductPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckOutPage(driver)
        self.submit_page = SubmitPage(driver)

    def apply_sorting_on_main_page(self, sort_by: str, param: str) -> "ProductBuilder":
        self.main_page.sort_goods(sort_by, param)
        return self

    def add_product_to_cart(self, product_name: str) -> "ProductBuilder":
        self.main_page.goto_product_details(product_name)
        self.product_page.add_to_cart()
        return self

    def proceed_to_checkout(self) -> "ProductBuilder":
        self.main_page.goto_cart()
        self.cart_page.go_to_checkout()
        return self

    def fill_out_checkout(self, first_name: str, last_name: str, zip_code: str) -> "ProductBuilder":
        self.checkout_page.fill_out_checkout_form(first_name, last_name, zip_code)
        self.checkout_page.click_continue()
        return self

    def submit_order(self) -> None:
        self.submit_page.finish_checkout()

    def check_order_success(self) -> bool:
        thanks_text = "Thank you for your order!"
        success_text = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
        try:
            assert self.page.is_element_present('[class="pony_express"]')
            assert self.page.is_text_present('[class="complete-header"]', thanks_text)
            assert self.page.is_text_present('[class="complete-text"]', success_text)
            return True
        except AssertionError:
            return False
