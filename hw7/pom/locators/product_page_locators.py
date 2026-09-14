from selenium.webdriver.common.by import By


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-md-6 > h1")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.add-to-cart")
    PRODUCT_DESCRIPTION = (By.ID, "description")
    COMMENTS_LIST = (By.ID, "product-comments-list-header")
    WISH_BTN = (By.CLASS_NAME, "wishlist-button-add")
    CONTINUE_CART_BTN = (By.CSS_SELECTOR, ".cart-content-btn .btn.btn-primary")
