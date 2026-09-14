from pom.page.cart_page import CartPage


def test_remove_from_cart(browser, base_url):
    cart_page = CartPage(browser, base_url)
    cart_page.open_from_modal()

    initial_count = cart_page.count_cart_items()

    assert initial_count > 0

    cart_page.remove_product()

    no_items_title = cart_page.no_items_title()

    assert no_items_title.is_displayed()
