from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import data
from data import PHONE_NUMBER
from data import CARD_NUMBER
from data import CARD_CODE
from data import MESSAGE_FOR_DRIVER
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    # Localizadores como atributos de classe
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Personal"]')
    CALL_TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Chamar um taxi"]')
    COMFORT_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Comfort"]')

# Campo Telefone
    PHONE_FIELD_LOCATOR = (By.XPATH, '//div[text()="Número de telefone"]')
    PHONE_INPUT_LOCATOR = (By.ID, 'phone')
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Próximo"]')
    SMS_CODE_INPUT_LOCATOR = (By.XPATH, '//button[text()="Inserir o código"]')
    CONFIRM_SMS_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Confirmar"]')

# Campo Cartão
    PAYMENT_METHOD_BUTTON = (By.XPATH, '//div[text()="Método de Pagamento"]')
    ADD_CARD_BUTTON = (By.XPATH, '//button[text()="Adicionar cartão"]')
    CARD_NUMBER_INPUT = (By.ID, 'number')
    CARD_CODE_INPUT = (By.XPATH, '//div[@class="card-code-input"]//input[@id="code"]')
    ADD_PAYMENT_METHOD_BUTTON = (By.XPATH, '//button[text()="Adicionar"]')
    CLOSE_POPUP_BUTTON = (By.CSS_SELECTOR, 'button.close-button.section-close')

# Comentário para o motorista
    MESSAGE_FIELD = (By.XPATH, '//button[text()= "Enviar mensagem ao motorista..."]')

# Pedir um cobertor e lençóis
    BLANKET_TOGGLE_LOCATOR = (By.CSS_SELECTOR, '.r-sw .slider.round')
    BLANKET_TOGGLE_CHECKBOX = (By.CSS_SELECTOR, '.r-sw .switch-input')

# Pedir 2 sorvetes
    ICE_CREAM_BUTTON_LOCATOR = (By.XPATH, '//div[text()="Sorvete"]/..//div[@class="counter"]')
    ICE_CREAM_PLUS_BUTTON = (By.XPATH, '//div[text()="Sorvete"]/..//div[@class="counter-plus"]')
    ICE_CREAM_VALUE = (By.XPATH, '//div[text()="Sorvete"]/..//div[@class="counter-value"]')

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_personal_option(self):
        personal_button = self.driver.find_element(*self.PERSONAL_OPTION_LOCATOR)
        if not personal_button.is_selected():
            personal_button.click()

    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON_LOCATOR).click()

    def click_comfort_button(self):
        comfort_option = self.driver.find_element(*self.COMFORT_BUTTON_LOCATOR)
        if not comfort_option.is_selected():
            comfort_option.click()

    def click_phone_field(self):
        self.driver.find_element(*self.PHONE_FIELD_LOCATOR).click()

    def click_phone_input(self):
        self.driver.find_element(*self.PHONE_INPUT_LOCATOR).click()

    def fill_phone_input(self, phone_number):
        self.driver.find_element(*self.PHONE_INPUT_LOCATOR).send_keys(PHONE_NUMBER)

    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    def click_sms_code_input(self):
        self.driver.find_element(*self.SMS_CODE_INPUT_LOCATOR).click()

    def fill_sms_code_input(self, sms_code):
        sms_code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.SMS_CODE_INPUT_LOCATOR).send_keys(sms_code)

    def click_confirm_sms_button(self):
        self.driver.find_element(*self.CONFIRM_SMS_BUTTON_LOCATOR).click()

    def click_payment_method_button(self):
        self.driver.find_element(*self.PAYMENT_METHOD_BUTTON).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.ADD_CARD_BUTTON).click()

    def fill_card_number(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(CARD_NUMBER)

    def fill_card_code_and_blur(self, card_code_input):
        code_field = self.driver.find_element(*self.CARD_CODE_INPUT)
        code_field.send_keys(CARD_CODE)
        code_field.send_keys(Keys.TAB)

    def click_message_field (self):
        self.driver.find_element(*self.MESSAGE_FIELD).click()

    def fill_message_field(self, message_for_driver):
        self.driver.find_element(*self.MESSAGE_FIELD).send_keys(MESSAGE_FOR_DRIVER)

    def click_blanket_toggle(self):
        toggle = self.driver.find_element(*self.BLANKET_TOGGLE_LOCATOR)
        toggle_checkbox = self.driver.find_element(*self.BLANKET_TOGGLE_CHECKBOX)
        if not toggle_checkbox.is_selected():
            toggle.click()

    def add_ice_cream(self, quantity=2):
        ice_cream = self.driver.find_element(*self.ICE_CREAM_BUTTON_LOCATOR)
        plus_button = self.driver.find_element(*self.ICE_CREAM_PLUS_BUTTON)
        for _ in range(quantity):
           plus_button.click()

    def get_ice_cream_count(self):
        return int(self.driver.find_element(*self.ICE_CREAM_VALUE).text)