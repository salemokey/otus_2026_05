def test_product_page(product_page):

    assert product_page.displayed_product_name()
    assert product_page.displayed_add_to_cart_btn()
    assert product_page.displayed_description()
    assert product_page.displayed_comments()
    assert product_page.displayed_wish_btn()
