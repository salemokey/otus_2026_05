from pom.page.login_page import LoginPage


def test_login_page(browser, base_url):
    login_page = LoginPage(browser, base_url)
    login_page.open()

    current_url = browser.current_url

    title_login_page = login_page.displayed_title_login_page()
    login_form = login_page.displayed_login_form()
    btn_submit = login_page.displayed_btn_submit()

    assert title_login_page.text == "Log in to your account"
    assert "login?" in current_url, "Error"
    assert login_form.is_displayed()
    assert btn_submit.is_displayed()
