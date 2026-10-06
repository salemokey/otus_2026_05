import allure

def test_currency_cart(cart_page):

    with allure.step("Шаг 1: Смена валюты на USD в корзине"):
        cart_page.change_currency_cart_page()

    with allure.step("Шаг 2: Проверка отображения всех сумм в долларах ($)"):
        assert "$" in cart_page.product_discount()
        assert "$" in cart_page.product_price()
        assert "$" in cart_page.subtotal()
        assert "$" in cart_page.shipping()
        assert "$" in cart_page.total()
