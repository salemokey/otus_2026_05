from pom.page.product_page import ProductPage


def test_product_open(browser, base_url):
    product_page = ProductPage(browser, base_url)

    product_element_title = product_page.open()

    product_card_title = product_page.displayed_product_title()
    add_to_cart_btn = product_page.displayed_add_to_cart_btn()
    product_description = product_page.displayed_description()
    comments_list = product_page.displayed_comments()
    wish_button = product_page.displayed_wish_btn()

    assert product_element_title == product_card_title.text
    assert add_to_cart_btn.is_displayed()
    assert product_description.is_displayed()
    assert comments_list.is_displayed()
    assert wish_button.is_displayed()
