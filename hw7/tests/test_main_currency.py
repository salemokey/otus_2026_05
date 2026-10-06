import allure

def test_main_currency(main_page):

    with allure.step("Шаг 1: Смена валюты на USD"):
        main_page.change_currency_to_usd()

    with allure.step("Шаг 2: Проверка отображения цены в долларах"):
        assert "$" in main_page.get_updated_price()
