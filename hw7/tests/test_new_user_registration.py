def test_new_user_reg(registration_page):

    registration_page.click_gender_btn(1)

    registration_page.input_values()

    registration_page.click_all_checkboxes()
    registration_page.click_save_btn()
