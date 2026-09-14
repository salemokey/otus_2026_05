from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    TITLE_RERISTRATION_PAGE = (By.TAG_NAME, "h1")
    GENDER_BTN = (By.NAME, "id_gender")
    FIRSTNAME = (By.NAME, "firstname")
    LASTNAME = (By.NAME, "lastname")
    GENDER_BTN_TEMPLATE = (By.XPATH, '//label[@for="field-id_gender-{}"]')
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    BIRTHDAY = (By.NAME, "birthday")
    CHECKBOX_OPTIN = (By.XPATH, "//input[@name='optin']/..")
    CHECKBOX_PSGDPR = (By.XPATH, "//input[@name='psgdpr']/..")
    CHECKBOX_NEWSLETTER = (By.XPATH, "//input[@name='newsletter']/..")
    CHECKBOX_CUSTOMER_PRIVACY = (By.XPATH, "//input[@name='customer_privacy']/..")
    SAVE_BTN = (By.XPATH, "//button[@data-link-action='save-customer']")

    ALL_CHECKBOXES = [
        CHECKBOX_OPTIN,
        CHECKBOX_PSGDPR,
        CHECKBOX_NEWSLETTER,
        CHECKBOX_CUSTOMER_PRIVACY,
    ]
