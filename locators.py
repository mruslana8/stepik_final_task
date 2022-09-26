from selenium.webdriver.common.by import By

# теперь каждый селектор — это пара: как искать и что искать
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gbx/accounts/login/"
   # LOGIN_URL = (BY.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
