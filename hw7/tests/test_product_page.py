import allure

def test_product_page(product_page):
    with allure.step("Проверка наличия основных элементов страницы товара"):
        assert product_page.displayed_product_name(), "Название товара не отображается"
        assert product_page.displayed_add_to_cart_btn(), "Кнопка 'Добавить в корзину' не найдена"
        assert product_page.displayed_description(), "Описание товара отсутствует"
        assert product_page.displayed_comments(), "Список комментариев не загружен"
        assert product_page.displayed_wish_btn(), "Кнопка 'В избранное' не видна"