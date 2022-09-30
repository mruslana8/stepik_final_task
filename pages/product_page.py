from .base_page import BasePage
from ..locators import ProductPageLocators

class ProductPage(BasePage):

    # возвращать объект ключ, значение вместо переменных в классе
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_info(self):
        product_info = {
            'name': self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text,
            'price': self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        }
        return product_info

    def should_be_product_in_basket(self, product_info):
        self.should_be_added_product_name(product_info)
        self.should_be_added_product_price(product_info)

    def should_be_added_product_name(self, product_info):
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert added_product_name == product_info['name'], "Added product's name is wrong"

    def should_be_added_product_price(self, product_info):
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
        assert added_product_price == product_info['price'], "Added product's price is wrong"
