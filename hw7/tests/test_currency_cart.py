def test_currency_cart(cart_page):

    cart_page.change_currency_to_usd()

    assert "$" in cart_page.product_discount()
    assert "$" in cart_page.product_discount()
    assert "$" in cart_page.product_price()
    assert "$" in cart_page.subtotal()
    assert "$" in cart_page.shipping()
    assert "$" in cart_page.total()
