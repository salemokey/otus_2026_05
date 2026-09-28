from selenium.webdriver.common.by import By


class CartPageLocators:
    ADDED_PRODUCT = (By.CSS_SELECTOR, "li.cart-item")
    PRODUCT_DISCOUNT = (By.CLASS_NAME, "regular-price")
    PRICE = (By.CLASS_NAME, "price")
    PRODUCT_PRICE = (By.CLASS_NAME, "product-price")
    SUBTOTAL = (By.CSS_SELECTOR, "#cart-subtotal-products .value")
    SHIPPING = (By.CSS_SELECTOR, "#cart-subtotal-shipping .value")
    TOTAL = (By.CSS_SELECTOR, ".cart-total .value")
    REMOVE_BTN = (By.CSS_SELECTOR, "a.remove-from-cart")
    CART_ITEMS = (By.CSS_SELECTOR, "li.cart-item")
    NO_ITEMS_TITLE = (By.CSS_SELECTOR, "span.no-items")
