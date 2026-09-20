def test_check_main(main_page):

    assert main_page.displayed_title(), "Error"
    assert main_page.displayed_carousel(), "Error"
    assert main_page.displayed_user_info(), "Error"
    assert main_page.displayed_products(), "Error"
    assert main_page.displayed_popular_title(), "Error"
