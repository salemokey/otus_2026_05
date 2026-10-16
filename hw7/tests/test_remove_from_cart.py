import allure

def test_remove_from_cart(cart_page):
    
    with allure.step("Шаг 1: Проверка начального состояния корзины"):
        initial_count = cart_page.count_cart_items()
        assert initial_count > 0, f"Ожидалось наличие товаров в корзине, но найдено {initial_count}"

        allure.attach(
            cart_page._driver.get_screenshot_as_png(), 
            name="Корзина до удаления", 
            attachment_type=allure.attachment_type.PNG
        )


    with allure.step("Удаление товара"):
        cart_page.remove_product()
        

    with allure.step("Финальная проверка"):
        
        assert cart_page.no_items_title()

        allure.attach(
                    cart_page._driver.get_screenshot_as_png(), 
                    name="Корзина после клика", 
                    attachment_type=allure.attachment_type.PNG
                )
