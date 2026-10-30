# tests/test_cart.py
import pytest

from config import PASSWORD, USERNAME
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_add_backpack_to_cart(driver):
    LoginPage(driver).open().login(USERNAME, PASSWORD)
    products = ProductsPage(driver)
    assert products.get_title() == "Products"  # каталог загрузился

    products.add_backpack_to_cart()

    assert products.get_cart_badge_text() == "1"



@pytest.mark.parametrize("username", [
    pytest.param("standard_user", id="standard_user-control"),
    pytest.param(
        "problem_user",
        id="problem_user-defect",
        marks=pytest.mark.xfail(
            reason="Дефект problem_user: Remove у Sauce Labs Backpack не удаляет товар из корзины",
            strict=True,
        ),
    ),
])
def test_remove_backpack_from_cart(driver, username):
    LoginPage(driver).open().login(username, PASSWORD)
    products = ProductsPage(driver)
    assert products.get_title() == "Products"

    products.add_backpack_to_cart()
    assert products.get_cart_badge_text() == "1"  # предусловие: товар добавлен

    products.remove_backpack_from_cart()

    assert products.is_cart_badge_gone(), "Бейдж корзины не исчез после Remove"