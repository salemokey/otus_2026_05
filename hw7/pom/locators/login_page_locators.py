from selenium.webdriver.common.by import By


class LoginPageLocators:
    TITLE_LOGIN_PAGE = (By.TAG_NAME, "h1")
    LOGIN_FORM = (By.ID, "login-form")
    BTN_SUBMIT = (By.ID, "submit-login")
    REGISTRATION_BTN = (By.CLASS_NAME, "no-account")
