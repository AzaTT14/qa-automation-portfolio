"""Page Object for the SauceDemo checkout flow (info -> overview -> confirmation)."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Step one: information form
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    # Step two: overview
    FINISH_BUTTON = (By.ID, "finish")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    # Step three: confirmation
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_information(self, first_name: str, last_name: str, zip_code: str):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.ZIP_INPUT, zip_code)
        return self

    def continue_to_overview(self):
        self.click(self.CONTINUE_BUTTON)
        return self

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def finish_order(self):
        self.click(self.FINISH_BUTTON)
        return self

    def get_total(self) -> str:
        return self.get_text(self.TOTAL_LABEL)

    def get_confirmation_header(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)
