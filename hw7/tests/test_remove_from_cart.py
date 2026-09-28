def test_remove_from_cart(cart_page):

    assert cart_page.count_cart_items() > 0

    cart_page.remove_product()

    assert cart_page.no_items_title()
