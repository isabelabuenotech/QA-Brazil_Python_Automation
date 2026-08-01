from selenium.webdriver.chrome import webdriver
from pages import UrbanRoutesPage
import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # o código que você adicionou no sprint anterior
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

        # não modifique, pois precisamos do registro adicional habilitado para recuperar o código de confirmação do telefone
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.routes_page = UrbanRoutesPage(cls.driver)

        def test_set_route(self):
            self.routes_page.enter_from_location(data.ADDRESS_FROM)
            self.routes_page.enter_to_location(data.ADDRESS_TO)

            from_value = self.driver.find_element(*self.routes_page.FROM_LOCATOR).get_attribute('value')
            to_value = self.driver.find_element(*self.routes_page.TO_LOCATOR).get_attribute('value')
            assert from_value == data.ADDRESS_FROM
            assert to_value == data.ADDRESS_TO
            pass

        def test_select_plan(self):
            self.routes_page.click_call_taxi_button()
            self.routes_page.click_comfort_button()
            pass

        def test_fill_phone_number(self):
            self.routes_page.click_phone_field()
            self.routes_page.fill_phone_input(data.PHONE_NUMBER)
            self.routes_page.click_next_button()

            code = helpers.retrieve_phone_code(self.driver)

            self.routes_page.fill_sms_code_input(code)
            self.routes_page.click_confirm_sms_button()
            pass

        def test_fill_card(self):
            self.routes_page.click_payment_method_button()
            self.routes_page.click_add_card_button()
            self.routes_page.fill_card_number(data.CARD_NUMBER)
            self.routes_page.fill_card_code_and_blur(data.CARD_CODE)

            self.routes_page.driver.find_element(*self.routes_page.ADD_PAYMENT_METHOD_BUTTON).click()
            self.routes_page.driver.find_element(*self.routes_page.CLOSE_POPUP_BUTTON).click()
            pass

        def test_comment_for_driver(self):
            self.routes_page.fill_message_field(data.MESSAGE_FOR_DRIVER)
            pass

        def test_order_blanket_and_handkerchiefs(self):
            self.routes_page.click_blanket_toggle()

            is_selected = self.driver.find_element(*self.routes_page.BLANKET_TOGGLE_CHECKBOX).is_selected()
            assert is_selected is True
            pass

        def test_order_2_ice_creams(self):
            self.routes_page.add_ice_cream(2)
            assert self.routes_page.get_ice_cream_count() == 2
            pass

        def test_car_search_model_appears(self):
            self.routes_page.click_call_taxi_button()
            pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
