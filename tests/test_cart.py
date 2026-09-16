"""
Test suite: Cart
Covers manual test cases TC-CART-01 .. TC-CART-03 (see /test-cases portfolio).
"""
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.smoke
def test_added_item_appears_in_cart(logged_in_driver):
    """TC-CART-01: an item added on the catalog page is present in the cart with the same name."""
    inventory = InventoryPage(logged_in_driver)
    inventory.add_item_to_cart_by_name("Sauce Labs Bike Light")
    inventory.go_to_cart()

    cart = CartPage(logged_in_driver)
    assert "Sauce Labs Bike Light" in cart.get_cart_item_names()


@pytest.mark.regression
def test_remove_item_from_cart_page(logged_in_driver):
    """TC-CART-02: removing an item from the cart page itself empties the cart list."""
    inventory = InventoryPage(logged_in_driver)
    inventory.add_item_to_cart_by_name("Sauce Labs Bike Light")
    inventory.go_to_cart()

    cart = CartPage(logged_in_driver)
    cart.remove_item_by_name("Sauce Labs Bike Light")
    assert cart.get_cart_item_names() == []


@pytest.mark.regression
def test_continue_shopping_returns_to_inventory(logged_in_driver):
    """TC-CART-03: 'Continue Shopping' from the cart returns the user to the catalog page."""
    inventory = InventoryPage(logged_in_driver)
    inventory.go_to_cart()

    cart = CartPage(logged_in_driver)
    cart.continue_shopping()
    assert "inventory.html" in inventory.current_url()
