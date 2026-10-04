import allure


def test_check_main(main_page):
    with allure.step("Шаг 1: Проверка заголовка и карусели"):
        assert main_page.displayed_title(), "Заголовок страницы не отображается"
        assert main_page.displayed_carousel(), "Карусель товаров не найдена"

    with allure.step("Шаг 2: Проверка пользовательского интерфейса"):
        assert main_page.displayed_user_info(), "Иконка пользователя отсутствует"

    with allure.step("Шаг 3: Проверка контента страницы"):
        assert main_page.displayed_products(), "Список продуктов не загружен"
        assert main_page.displayed_popular_title(), "Блок 'Популярное' не виден"
