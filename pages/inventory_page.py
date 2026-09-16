"""Page Object for the SauceDemo product catalog (inventory) page."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart_by_name(self, item_name: str):
        button_id = "add-to-cart-" + item_name.lower().replace(" ", "-")
        self.click((By.ID, button_id))
        return self

    def remove_item_from_cart_by_name(self, item_name: str):
        button_id = "remove-" + item_name.lower().replace(" ", "-")
        self.click((By.ID, button_id))
        return self

    def sort_by(self, option_value: str):
        """option_value: 'az' | 'za' | 'lohi' | 'hilo'"""
        from selenium.webdriver.support.ui import Select
        Select(self.find(self.SORT_DROPDOWN)).select_by_value(option_value)
        return self

    def get_item_names(self) -> list[str]:
        return [el.text for el in self.find_all(self.ITEM_NAMES)]

    def get_item_prices(self) -> list[float]:
        return [float(el.text.replace("$", "")) for el in self.find_all(self.ITEM_PRICES)]

    def get_cart_count(self) -> int:
        return int(self.get_text(self.CART_BADGE)) if self.is_visible(self.CART_BADGE) else 0

    def go_to_cart(self):
        self.click(self.CART_LINK)
        return self
