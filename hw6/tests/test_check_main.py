from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def test_check_main(browser, base_url):
    browser.get(base_url)

    wait = WebDriverWait(driver=browser, timeout=10)

    header_element = browser.find_element(by=By.TAG_NAME, value="h1")
    carousel_element = browser.find_element(by=By.ID, value="carousel")
    user_info_element = browser.find_element(by=By.CLASS_NAME, value="user-info")
    popular_title = browser.find_element(
        by=By.CSS_SELECTOR, value="h2.products-section-title"
    )
    products_row = browser.find_element(By.CLASS_NAME, "products.row")

    wait.until(expected_conditions.visibility_of(header_element))
    wait.until(expected_conditions.visibility_of(carousel_element))
    wait.until(expected_conditions.visibility_of(user_info_element))
    wait.until(expected_conditions.visibility_of(popular_title))
    wait.until(expected_conditions.visibility_of(products_row))

    assert header_element.is_displayed(), "Error"
    assert carousel_element.is_displayed(), "Error"
    assert user_info_element.is_displayed(), "Error"
    assert popular_title.is_displayed(), "Error"
    assert products_row.is_displayed(), "Error"


def test_check_page_art(browser, base_url):
    browser.get(base_url)

    wait = WebDriverWait(driver=browser, timeout=10)

    link = wait.until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a.dropdown-item[href*="/9-art"]')
        )
    )
    link.click()

    wait.until(expected_conditions.url_contains("/9-art"))

    assert browser.current_url.endswith("/9-art")

    category_description = browser.find_element(By.ID, "category-description")
    category_top_menu = browser.find_element(By.CLASS_NAME, "category-top-menu")
    img_art = browser.find_element(By.CSS_SELECTOR, "img[alt='Art']")
    product_mininature = browser.find_element(By.CLASS_NAME, "product-miniature")
    search_filters = browser.find_element(By.ID, "search_filters")

    wait.until(expected_conditions.visibility_of(category_description))
    wait.until(expected_conditions.visibility_of(category_top_menu))
    wait.until(expected_conditions.visibility_of(img_art))
    wait.until(expected_conditions.visibility_of(product_mininature))
    wait.until(expected_conditions.visibility_of(search_filters))

    assert category_description.is_displayed(), "Error"
    assert category_top_menu.is_displayed(), "Error"
    assert img_art.is_displayed(), "Error"
    assert product_mininature.is_displayed(), "Error"
    assert search_filters.is_displayed(), "Error"


def test_check_product_page(browser, base_url):
    browser.get(base_url)

    wait = WebDriverWait(driver=browser, timeout=10)

    product_card = wait.until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, ".h3.product-title")
        )
    )

    product_name = product_card.text.upper()

    product_card.click()

    assert (
        product_name
        == wait.until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.col-md-6 > h1")
            )
        ).text
    ), "Error"

    add_to_cart_btn = wait.until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, "button.add-to-cart")
        )
    )

    assert add_to_cart_btn.is_displayed(), "Error"

    product_description = wait.until(
        expected_conditions.visibility_of_element_located((By.ID, "description"))
    )

    assert product_description.is_displayed(), "Error"

    comments_list = wait.until(
        expected_conditions.visibility_of_element_located(
            (By.ID, "product-comments-list-header")
        )
    )

    assert comments_list.is_displayed()

    wish_btn = wait.until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "wishlist-button-add")
        )
    )

    assert wish_btn.is_displayed(), "Error"


def test_check_login(browser, base_url):
    browser.get(base_url)

    wait = WebDriverWait(driver=browser, timeout=10)

    login_btn = wait.until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, "user-info"))
    )

    assert login_btn.is_displayed(), "Error"

    login_btn.click()

    title_login_page = wait.until(
        expected_conditions.visibility_of_element_located((By.TAG_NAME, "h1"))
    )

    assert title_login_page.text == "Log in to your account", "Error"

    assert "login?" in browser.current_url, "Error"

    login_form = wait.until(
        expected_conditions.visibility_of_element_located((By.ID, "login-form"))
    )

    assert login_form.is_displayed(), "Error"

    btn_sumbit = wait.until(
        expected_conditions.visibility_of_element_located((By.ID, "submit-login"))
    )

    assert btn_sumbit.is_displayed(), "Error"


def test_check_registration(browser, base_url):
    browser.get(base_url)

    wait = WebDriverWait(driver=browser, timeout=10)

    wait.until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, "user-info"))
    ).click()

    wait.until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, "no-account"))
    ).click()

    title_registration = wait.until(
        expected_conditions.visibility_of_element_located((By.TAG_NAME, "h1"))
    )

    assert title_registration.is_displayed(), "Error"
    assert title_registration.text == "Create an account", "Error"

    radio_btn_gender = wait.until(
        expected_conditions.presence_of_all_elements_located((By.NAME, "id_gender"))
    )

    assert len(radio_btn_gender) == 2, "Error"

    firstname = wait.until(
        expected_conditions.visibility_of_element_located((By.NAME, "firstname"))
    )

    assert firstname.is_displayed(), "Error"

    lastname = wait.until(
        expected_conditions.visibility_of_element_located((By.NAME, "lastname"))
    )

    assert lastname.is_displayed(), "Error"


def test_login_user(browser, base_url):
    browser.get(base_url)

    wait = WebDriverWait(driver=browser, timeout=10)

    login_btn = wait.until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, "user-info"))
    )

    assert login_btn.is_displayed(), "Error"

    login_btn.click()

    email_input = wait.until(
        expected_conditions.visibility_of_element_located((By.NAME, "email"))
    )
    password_input = wait.until(
        expected_conditions.visibility_of_element_located((By.NAME, "password"))
    )

    email_input.send_keys("test@test.com")
    password_input.send_keys("NewPassword123!")

    sign_btn = wait.until(
        expected_conditions.element_to_be_clickable((By.ID, "submit-login"))
    )

    sign_btn.click()

    user_name = wait.until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.user-info  a[title*='View my customer account']")
        )
    )

    assert user_name.is_displayed()

    user_name.click()

    title_account_page = wait.until(
        expected_conditions.visibility_of_element_located((By.TAG_NAME, "h1"))
    )

    assert title_account_page.text == "Your account"

    wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".logout"))
    ).click()

    wait.until(
        expected_conditions.invisibility_of_element_located(
            (By.CSS_SELECTOR, "div.user-info  a[title*='View my customer account']")
        )
    )

    logout_name = browser.find_elements(
        By.CSS_SELECTOR, "a[title*='View my customer account']"
    )

    assert len(logout_name) == 0, "Выход не произошел"


def test_check_currency(browser, base_url):
    browser.get(base_url)

    wait = WebDriverWait(driver=browser, timeout=10)

    current_price = wait.until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "price"))
    ).text

    dropdown_currency = wait.until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.currency-selector > button.hidden-sm-down")
        )
    )

    dropdown_currency.click()

    if "€" in current_price:
        dropdown_option = wait.until(
            expected_conditions.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "ul.dropdown-menu li a.dropdown-item[title*='US Dollar']",
                )
            )
        )

        dropdown_option.click()

        wait.until(
            expected_conditions.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.currency-selector .expand-more"), "USD $"
            )
        )

        updated_price = wait.until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "price"))
        ).text

        wait.until(expected_conditions.url_contains("id_currency=2"))

        assert "$" in updated_price, "error current price"


def test_check_add_product_and_currency_cart(browser, base_url):
    browser.get(base_url)

    wait = WebDriverWait(driver=browser, timeout=10)

    wait.until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, "h3.product-title")
        )
    ).click()

    wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart"))
    ).click()

    wait.until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, ".cart-content-btn .btn.btn-primary")
        )
    ).click()

    added_product = wait.until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, "li.cart-item")
        )
    )

    assert added_product.is_displayed()

    wait.until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.currency-selector > button.hidden-sm-down")
        )
    ).click()

    wait.until(
        expected_conditions.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "ul.dropdown-menu li a.dropdown-item[title*='US Dollar']",
            )
        )
    ).click()

    product_discount = wait.until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "regular-price")
        )
    ).text

    price = wait.until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "price"))
    ).text

    product_price = wait.until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "product-price")
        )
    ).text

    subtotal = wait.until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, "#cart-subtotal-products .value")
        )
    ).text

    shipping = wait.until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, "#cart-subtotal-shipping .value")
        )
    ).text

    total = wait.until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, ".cart-total .value")
        )
    ).text

    wait.until(expected_conditions.url_contains("id_currency=2"))

    assert "$" in subtotal, "Error"
    assert "$" in shipping, "Error"
    assert "$" in total, "Error"
    assert "$" in price, "Error"
    assert "$" in product_discount, "Error"
    assert "$" in product_price, "Error"
