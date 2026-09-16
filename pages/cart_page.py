"""Page Object for the SauceDemo cart page."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def get_cart_item_names(self) -> list[str]:
        return [el.text for el in self.find_all(self.ITEM_NAMES)]

    def remove_item_by_name(self, item_name: str):
        button_id = "remove-" + item_name.lower().replace(" ", "-")
        self.click((By.ID, button_id))
        return self

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        return self

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        return self
