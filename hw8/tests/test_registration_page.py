import allure


def test_registration_page(login_page):
    with allure.step("Переход на страницу регистрации"):
        registration_page = login_page.click_registration()

    with allure.step("Проверка наличия основных элементов формы регистрации"):
        assert registration_page.displayed_title_registration_page(), "Заголовок страницы регистрации не отображается"
        assert registration_page.displayed_gender_btn(), "Кнопки выбора пола отсутствуют"
        assert registration_page.displayed_firstname(), "Поле 'Имя' не найдено"
        assert registration_page.displayed_lastname(), "Поле 'Фамилия' не найдено"

    with allure.step("Проверка корректности заголовка страницы"):
        actual_title = registration_page.title_registration_page()
        expected_text = "Create an account"
        assert expected_text in actual_title, f"Ожидался текст '{expected_text}', но получен: '{actual_title}'"