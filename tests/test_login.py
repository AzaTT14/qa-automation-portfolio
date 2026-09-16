"""
Test suite: Login
Covers manual test cases TC-LOGIN-01 .. TC-LOGIN-06 (see /test-cases portfolio).
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_login_with_valid_credentials(driver):
    """TC-LOGIN-01: standard_user logs in successfully and lands on the inventory page."""
    login_page = LoginPage(driver).open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert "inventory.html" in inventory_page.current_url()
    assert inventory_page.get_text(inventory_page.PAGE_TITLE) == "Products"


@pytest.mark.regression
@pytest.mark.negative
def test_login_locked_out_user_is_blocked(driver):
    """TC-LOGIN-02: locked_out_user sees a clear lockout error, not a generic failure."""
    login_page = LoginPage(driver).open()
    login_page.login("locked_out_user", "secret_sauce")

    assert login_page.is_error_displayed()
    assert "locked out" in login_page.get_error_message().lower()


@pytest.mark.regression
@pytest.mark.negative
def test_login_with_invalid_password(driver):
    """TC-LOGIN-03: valid username + wrong password is rejected with a generic error."""
    login_page = LoginPage(driver).open()
    login_page.login("standard_user", "wrong_password")

    assert login_page.is_error_displayed()
    assert "do not match" in login_page.get_error_message().lower()


@pytest.mark.regression
@pytest.mark.negative
def test_login_with_empty_username(driver):
    """TC-LOGIN-04: empty username is rejected before hitting the backend."""
    login_page = LoginPage(driver).open()
    login_page.login("", "secret_sauce")

    assert login_page.is_error_displayed()
    assert "username is required" in login_page.get_error_message().lower()


@pytest.mark.regression
@pytest.mark.negative
def test_login_with_empty_password(driver):
    """TC-LOGIN-05: empty password is rejected with a field-specific message."""
    login_page = LoginPage(driver).open()
    login_page.login("standard_user", "")

    assert login_page.is_error_displayed()
    assert "password is required" in login_page.get_error_message().lower()


@pytest.mark.regression
def test_login_error_banner_is_dismissible(driver):
    """TC-LOGIN-06: the error banner's close (X) button clears the error state."""
    login_page = LoginPage(driver).open()
    login_page.login("standard_user", "wrong_password")
    assert login_page.is_error_displayed()

    login_page.click(login_page.ERROR_CLOSE_BUTTON)
    assert not login_page.is_error_displayed()
