from pom.page.cart_page import CartPage


def test_currency_cart(browser, base_url):
    cart_page = CartPage(browser, base_url)
    cart_page.open_from_modal()

    cart_page.change_currency_to_usd()

    product_discount = cart_page.product_discount()
    price = cart_page.product_discount()
    product_price = cart_page.product_price()
    subtotal = cart_page.subtotal()
    shipping = cart_page.shipping()
    total = cart_page.total()

    assert "$" in subtotal, "Error"
    assert "$" in shipping, "Error"
    assert "$" in total, "Error"
    assert "$" in price, "Error"
    assert "$" in product_discount, "Error"
    assert "$" in product_price, "Error"
