from config import PASSWORD, USERNAME
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_standard_user_can_login(driver):
    LoginPage(driver).open().login(USERNAME, PASSWORD)

    products = ProductsPage(driver)

    assert products.get_title() == "Products"
    assert len(products.get_product_names()) == 6
