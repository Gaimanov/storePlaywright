from builder.ProductBuilder import ProductBuilder
from pages.LoginPage import LoginPage
import allure


@allure.feature("purchase")
@allure.story("end-to-end purchase flow")
@allure.description("Purchase end-to-end flow starting on the main page, ending with 'Order successful' message")
@allure.link("https://saucedemo.atlassian.net/browse/PRD-173")
def test_end_to_end_purchase(driver):
    """
    Test goes through the end-to-end flow by applying sorting on the main page, entering product details page,
    adding it to the cart, going through the checkout process and asserting that order was accepted successfully
    """
    _ = LoginPage(driver)
    builder = ProductBuilder(driver)

    builder \
        .apply_sorting_on_main_page("price", "hl") \
        .add_product_to_cart('Sauce Labs Backpack') \
        .proceed_to_checkout() \
        .fill_out_checkout('John Doe', 'johndoe@example.com', '123 Main St') \
        .submit_order()

    with allure.step("order successful"):
        assert builder.check_order_success()
