def test_login_page(main_page):
    login_page = main_page.click_on_login()

    assert login_page.displayed_title_login_page()
    assert login_page._is_login_url()
    assert login_page.displayed_btn_submit()
    assert login_page.displayed_login_form()
    assert login_page.displayed_reg_btn()
    assert "Log in to your account" in login_page.title_login_page()
