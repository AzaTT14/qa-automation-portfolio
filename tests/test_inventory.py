"""
Test suite: Inventory / Product catalog
Covers manual test cases TC-INV-01 .. TC-INV-05 (see /test-cases portfolio).
"""
import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.regression
def test_sort_by_name_a_to_z(logged_in_driver):
    """TC-INV-01: default and explicit A-Z sort returns alphabetically ascending names."""
    page = InventoryPage(logged_in_driver)
    page.sort_by("az")
    names = page.get_item_names()
    assert names == sorted(names)


@pytest.mark.regression
def test_sort_by_name_z_to_a(logged_in_driver):
    """TC-INV-02: Z-A sort reverses the alphabetical order."""
    page = InventoryPage(logged_in_driver)
    page.sort_by("za")
    names = page.get_item_names()
    assert names == sorted(names, reverse=True)


@pytest.mark.regression
def test_sort_by_price_low_to_high(logged_in_driver):
    """TC-INV-03: price low-to-high sort is numerically ascending."""
    page = InventoryPage(logged_in_driver)
    page.sort_by("lohi")
    prices = page.get_item_prices()
    assert prices == sorted(prices)


@pytest.mark.smoke
def test_add_single_item_updates_cart_badge(logged_in_driver):
    """TC-INV-04: adding one item shows a cart badge with count 1."""
    page = InventoryPage(logged_in_driver)
    page.add_item_to_cart_by_name("Sauce Labs Backpack")
    assert page.get_cart_count() == 1


@pytest.mark.regression
def test_remove_item_updates_cart_badge(logged_in_driver):
    """TC-INV-05: removing an item clears the cart badge when the cart becomes empty."""
    page = InventoryPage(logged_in_driver)
    page.add_item_to_cart_by_name("Sauce Labs Backpack")
    assert page.get_cart_count() == 1

    page.remove_item_from_cart_by_name("Sauce Labs Backpack")
    assert page.get_cart_count() == 0
