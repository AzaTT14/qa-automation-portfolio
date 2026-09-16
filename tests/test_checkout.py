"""
Test suite: Checkout
Covers manual test cases TC-CHK-01 .. TC-CHK-04 (see /test-cases portfolio).
"""
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
def test_full_checkout_flow_completes_successfully(logged_in_driver):
    """TC-CHK-01: end-to-end purchase — add item, checkout, fill info, finish, confirm."""
    inventory = InventoryPage(logged_in_driver)
    inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory.go_to_cart()

    CartPage(logged_in_driver).checkout()

    checkout = CheckoutPage(logged_in_driver)
    checkout.fill_information("Aigerim", "Tolegenova", "010000")
    checkout.continue_to_overview()
    checkout.finish_order()

    assert "Thank you" in checkout.get_confirmation_header()


@pytest.mark.regression
@pytest.mark.negative
def test_checkout_requires_first_name(logged_in_driver):
    """TC-CHK-02: leaving First Name empty blocks progress with a field-specific error."""
    inventory = InventoryPage(logged_in_driver)
    inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory.go_to_cart()
    CartPage(logged_in_driver).checkout()

    checkout = CheckoutPage(logged_in_driver)
    checkout.fill_information("", "Tolegenova", "010000")
    checkout.continue_to_overview()

    assert "First Name is required" in checkout.get_error_message()


@pytest.mark.regression
@pytest.mark.negative
def test_checkout_requires_postal_code(logged_in_driver):
    """TC-CHK-03: leaving Zip/Postal Code empty blocks progress."""
    inventory = InventoryPage(logged_in_driver)
    inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory.go_to_cart()
    CartPage(logged_in_driver).checkout()

    checkout = CheckoutPage(logged_in_driver)
    checkout.fill_information("Aigerim", "Tolegenova", "")
    checkout.continue_to_overview()

    assert "Postal Code is required" in checkout.get_error_message()


@pytest.mark.regression
def test_order_total_equals_subtotal_plus_tax(logged_in_driver):
    """TC-CHK-04: the displayed total on the overview page equals subtotal + tax (financial sanity check)."""
    inventory = InventoryPage(logged_in_driver)
    inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory.go_to_cart()
    CartPage(logged_in_driver).checkout()

    checkout = CheckoutPage(logged_in_driver)
    checkout.fill_information("Aigerim", "Tolegenova", "010000")
    checkout.continue_to_overview()

    subtotal = float(checkout.get_text(checkout.ITEM_TOTAL).split("$")[1])
    tax = float(checkout.get_text(checkout.TAX_LABEL).split("$")[1])
    total = float(checkout.get_text(checkout.TOTAL_LABEL).split("$")[1])

    assert round(subtotal + tax, 2) == round(total, 2)
