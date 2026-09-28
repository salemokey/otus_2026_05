def test_main_currency(main_page):

    main_page.change_currency_to_usd()

    assert "$" in main_page.get_updated_price()
