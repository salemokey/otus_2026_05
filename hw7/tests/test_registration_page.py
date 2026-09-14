from pom.page.registration_page import RegistrationPage


def test_login_page(browser, base_url):
    registration_page = RegistrationPage(browser, base_url)
    registration_page.open()

    title_registration_page = registration_page.displayed_title_registration_page()
    gender_btns = registration_page.displayed_gender_btn()
    first_name = registration_page.displayed_firstname()
    last_name = registration_page.displayed_lastname()

    assert title_registration_page.is_displayed()
    assert title_registration_page.text == "Create an account", "Error"
    assert gender_btns == 2, "Error"
    assert first_name.is_displayed()
    assert last_name.is_displayed()
