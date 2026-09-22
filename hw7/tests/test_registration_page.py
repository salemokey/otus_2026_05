def test_registration_page(login_page):
    registration_page = login_page.click_registration()

    assert registration_page.displayed_title_registration_page()
    assert registration_page.displayed_gender_btn()
    assert registration_page.displayed_firstname()
    assert registration_page.displayed_lastname()
    assert "Create an account" in registration_page.title_registration_page()
