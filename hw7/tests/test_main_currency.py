from pom.page.main_page import MainPage


def test_check_main(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open()

    header = main_page.displayed_title()
    carousel = main_page.displayed_carousel()
    user_info = main_page.displayed_user_info()
    popular_title = main_page.displayed_popular_title()
    products = main_page.displayed_products()

    assert header.is_displayed(), "Error"
    assert carousel.is_displayed(), "Error"
    assert user_info.is_displayed(), "Error"
    assert popular_title.is_displayed(), "Error"
    assert products.is_displayed(), "Error"
