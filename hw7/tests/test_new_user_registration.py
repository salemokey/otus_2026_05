from pom.page.cart_page import CartPage


def test_new_user_reg(browser, base_url):
    cart_page = CartPage(browser, base_url)
    cart_page.open_from_modal()

    title_registration_page = registration_page.displayed_title_registration_page()
    gender_btns = registration_page.displayed_gender_btn()
    first_name = registration_page.displayed_firstname()
    last_name = registration_page.displayed_lastname()
    email = registration_page.displayed_email()

    registration_page.click_gender_btn(1)

    first_name.send_keys("test")
    last_name.send_keys("test")
    email.send_keys("test1@test.com")
    registration_page.displayed_password().send_keys("NewPassword123!")
    registration_page.displayed_birthday().send_keys("03/07/2007")

    registration_page.click_all_checkboxes()
    registration_page.click_save_btn()
