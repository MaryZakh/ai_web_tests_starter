# pages/login_page.py
from config import BASE_URL, PASSWORD, TIMEOUT
from pages.products_page import ProductsPage
from pages.login_page import LoginPage


class LoginPage_1(LoginPage):
    # ... локаторы, __init__, open(), login(), get_error_text() без изменений

    def open_products(self, username, password=PASSWORD):
        """Открывает сайт, логинится и возвращает ProductsPage."""
        self.open().login(username, password)
        return ProductsPage(self.driver)