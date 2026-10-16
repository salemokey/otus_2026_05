from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_ELEMENT = (By.TAG_NAME, "h1")
    CAROUSEL_ELEMENT = (By.ID, "carousel")
    USER_INFO_ELEMENT = (By.CLASS_NAME, "user-info")
    POPULAR_TITLE = (By.CSS_SELECTOR, "h2.products-section-title")
    PRODUCTS_ROW = (By.CLASS_NAME, "products.row")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".h3.product-title")
    LOGIN_BTN = (By.CLASS_NAME, "user-info")
    CURRENT_PRICE = (By.CLASS_NAME, "price")
    DROPDOWN_CURRENCY = (
        By.CSS_SELECTOR,
        "div.currency-selector > button.hidden-sm-down",
    )
    DROPDOWN_OPTION = (
        By.CSS_SELECTOR,
        "ul.dropdown-menu li a.dropdown-item[title*='US Dollar']",
    )
    DROPDOWN_OPTION_DOLLARS = {
        "locator": (By.CSS_SELECTOR, "div.currency-selector .expand-more"),
        "text": "USD $",
    }

    UPDATED_PRICE = (By.CLASS_NAME, "price")

    URL_CURRENCY = "id_currency=2"
