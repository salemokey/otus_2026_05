import allure

def test_new_user_reg(registration_page):
    with allure.step("Шаг 1: Выбор пола пользователя"):
        registration_page.click_gender_btn(1)

    with allure.step("Шаг 2: Заполнение полей формы регистрации"):
        registration_page.input_values()

    with allure.step("Шаг 3: Согласие с условиями (отметка чекбоксов)"):
        registration_page.click_all_checkboxes()

    with allure.step("Шаг 4: Отправка формы регистрации"):
        registration_page.click_save_btn()