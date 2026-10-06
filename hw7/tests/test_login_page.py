import allure

def test_login_page(main_page):
    
    with allure.step("Переход на страницу авторизации"):
        login_page = main_page.click_on_login()

    with allure.step("Проверка наличия основных элементов формы входа"):
        assert login_page.displayed_title_login_page(), "Заголовок страницы входа не отображается"
        assert login_page.displayed_btn_submit(), "Кнопка 'Войти' не найдена"
        assert login_page.displayed_login_form(), "Форма входа отсутствует на странице"
        assert login_page.displayed_reg_btn(), "Кнопка перехода к регистрации не видна"
    
    with allure.step("Проверка заголовка"):
        assert "Log in to your account" in login_page.title_login_page()
