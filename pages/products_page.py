from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import TIMEOUT


class ProductsPage:
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    PRODUCT_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    BACKPACK_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def get_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.TITLE)).text

    def get_product_names(self):
        self.wait.until(EC.visibility_of_element_located(self.TITLE))
        return [element.text for element in self.driver.find_elements(*self.PRODUCT_NAMES)]

    def add_backpack_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.BACKPACK_ADD_TO_CART_BUTTON)).click()

    def get_cart_badge_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.CART_BADGE)).text

    def remove_backpack_from_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_BACKPACK_BUTTON)).click()

    def is_cart_badge_gone(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(self.CART_BADGE))
            return True
        except TimeoutException:
            return False