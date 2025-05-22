# coding=utf8
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

import undetected_chromedriver as uc

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options
#chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
#firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
#helpers
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import helpers_N as hn
import time

#report runners
#import HtmlTestRunner

import AllureReports

class Chrome_Negative_Test(unittest.TestCase):
    def setUp(self):
        # Set up Chrome options for undetected_chromedriver
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")
        #options.add_argument("--headless")

        # Initialize undetected_chromedriver
        self.driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        #self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    def tearDown(self):
        self.driver.quit()

    def test_016_N(self):
        driver = self.driver
        print("Boundary testing of sliders and an input field")
        driver.get(hn.URL)

        # Hover over the API element to reveal submodules
        hn.hover_over_element(driver, By.XPATH, hn.API_LOCATOR)

        # Wait for the PRICING_LOCATOR element to become visible
        hn.wait_for_element(driver, By.XPATH, hn.overview_locator)

        # Click on the PRICING_LOCATOR element
        hn.click_on_elem(driver, By.XPATH, hn.overview_locator)

         #scroll down
        hn.scroll_down(driver, By.XPATH, hn.COST_CALC_LOCATOR)

        hn.boundary_test(driver, By.XPATH, hn.FIELD_INPUT1, 1000000000000, 0)
        hn.boundary_test(driver, By.XPATH, hn.FIELD_INPUT2, 1000000000000,0)
        hn.boundary_test(driver,By.XPATH, hn.FIELD_INPUT3, 1000000000000, 0)

    def test_017_N(self):
        print("Attempt to input invalid symbols or information in  a search tab")
        driver=self.driver
        driver.get(hn.URL)
        hn.hover_over_element(driver, By.XPATH, hn.API_LOCATOR)
        hn.click_on_elem(driver, By.XPATH, hn.DOCUMENTATION_LOCATOR)
        hn.switch_to_new_tab(driver, hn.EXP_DOC_TITLE)
        time.sleep(3)
        hn.is_element_present(driver, By.XPATH, hn.SEARCH_BAR)
        hn.click_on_elem(driver, By.XPATH, hn.SEARCH_BAR)
        time.sleep(3)
        hn.is_element_present(driver, By.XPATH, hn.SEARCH_BAR_2)
        hn.click_on_elem(driver,By.XPATH, hn.SEARCH_BAR_2)
        hn.enter_data(driver, By.XPATH, hn.SEARCH_BAR_2, "$#@$!", timeout=10)
        time.sleep(5)
        try:
            response = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(., 'No results for')]"))
        )
            self.assertTrue(response.is_displayed(), "Expected 'No results for' message to be visible")
        except AssertionError:
            print(f"response not found ")

    def test_018_N(self):
        print("attempting to change URL endpoint")
        driver = self.driver
        driver.get("https://x.ai/apinonexistent")
        time.sleep(2)
        error_element = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(.,'Page not found')]" ))
        )
        # gets the text from the element
        error_text = error_element.text.strip()
        expected_text ="Page not found"
        self.assertEqual(error_text, expected_text)
        print(f"Attempt ot change URL failed:'{error_text}'")

    def test_019_N(self):
        print("Verify API Endpoint Behavior with space entering .")
        driver = self.driver
        driver.get(hn.URL)
        hn.hover_over_element(driver, By.XPATH, hn.API_LOCATOR)
        hn.click_on_elem(driver, By.XPATH, hn.DOCUMENTATION_LOCATOR)
        hn.switch_to_new_tab(driver, hn.EXP_DOC_TITLE)
        time.sleep(3)
        hn.click_on_elem(driver, By.XPATH, hn.SEARCH_BAR)
        time.sleep(3)
        hn.is_element_present(driver, By.XPATH, hn.SEARCH_BAR_2)
        hn.click_on_elem(driver, By.XPATH, hn.SEARCH_BAR_2)
        hn.space_input(driver,By.XPATH, hn.SEARCH_BAR_2,100)

    def test_020_N(self):
        print("Attempt to input a float number into cost calculator")
        driver=self.driver
        driver.get(hn.URL)

        # Hover over the API element to reveal submodules
        hn.hover_over_element(driver, By.XPATH, hn.API_LOCATOR)

        # Wait for the PRICING_LOCATOR element to become visible
        hn.wait_for_element(driver, By.XPATH, hn.overview_locator)

        # Click on the PRICING_LOCATOR element
        hn.click_on_elem(driver, By.XPATH, hn.overview_locator)

        # scroll down
        hn.scroll_down(driver, By.XPATH, hn.COST_CALC_LOCATOR)

        try:
            hn.enter_data(driver, By.XPATH, hn.FIELD_INPUT1, "12" + Keys.LEFT + ".", 10)
            print("trying to move courser to the left in order to make it a float number")
            element = driver.find_element(By.XPATH,hn.FIELD_INPUT1)
            input_info = element.get_attribute("value")
            input_info = float(input_info)
            self.assertTrue(input_info, float(input_info))
            print(f"Float number was accepted:'{input_info}")
        except AssertionError:
            print("float number wasn't accepted")

class Edge_Negative_Test(unittest.TestCase):
    def setUp(self):
        # Configure ChromeOptions for undetected_chromedriver
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')  # Ignores SSL certificate errors
        options.add_argument("--headless")

        # Initialize Edge WebDriver with service and options
        self.driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_016_N(self):
        driver = self.driver
        print("Boundary testing of sliders and an input field")
        driver.get(hn.OVR_URL)

         #scroll down
        hn.scroll_down(driver, By.XPATH, hn.COST_CALC_LOCATOR)

        hn.boundary_test(driver, By.XPATH, hn.FIELD_INPUT1, 1000000000000, 0)
        hn.boundary_test(driver, By.XPATH, hn.FIELD_INPUT2, 1000000000000,0)
        hn.boundary_test(driver,By.XPATH, hn.FIELD_INPUT3, 1000000000000, 0)

    def test_017_N(self):
        print("Attempt to input invalid symbols or information in  a search tab")
        driver=self.driver
        driver.get(hn.DOC_URL)
        time.sleep(3)
        hn.is_element_present(driver, By.XPATH, hn.SEARCH_BAR)
        hn.click_on_elem(driver, By.XPATH, hn.SEARCH_BAR)
        time.sleep(3)
        hn.is_element_present(driver, By.XPATH, hn.SEARCH_BAR_2)
        hn.click_on_elem(driver,By.XPATH, hn.SEARCH_BAR_2)
        hn.enter_data(driver, By.XPATH, hn.SEARCH_BAR_2, "$#@$!", timeout=10)
        time.sleep(5)
        try:
            response = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(., 'No results for')]"))
        )
            self.assertTrue(response.is_displayed(), "Expected 'No results for' message to be visible")
        except AssertionError:
            print(f"response not found ")

    def test_018_N(self):
        print("attempting to change URL endpoint")
        driver = self.driver
        driver.get("https://x.ai/apinonexistent")
        time.sleep(2)
        error_element = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(.,'Page not found')]" ))
        )
        # gets the text from the element
        error_text = error_element.text.strip()
        expected_text ="Page not found"
        self.assertEqual(error_text, expected_text)
        print(f"Attempt ot change URL failed:'{error_text}'")

    def test_019_N(self):
        print("Verify API Endpoint Behavior with space entering .")
        driver = self.driver
        driver.get(hn.DOC_URL)
        time.sleep(3)
        hn.click_on_elem(driver, By.XPATH, hn.SEARCH_BAR)
        time.sleep(3)
        hn.is_element_present(driver, By.XPATH, hn.SEARCH_BAR_2)
        hn.click_on_elem(driver, By.XPATH, hn.SEARCH_BAR_2)
        hn.space_input(driver,By.XPATH, hn.SEARCH_BAR_2,100)

    def test_020_N(self):
        print("Attempt to input a float number into cost calculator")
        driver=self.driver
        driver.get(hn.OVR_URL)
        # scroll down
        hn.scroll_down(driver, By.XPATH, hn.COST_CALC_LOCATOR)

        try:
            hn.enter_data(driver, By.XPATH, hn.FIELD_INPUT1, "12" + Keys.LEFT + ".", 10)
            print("trying to move courser to the left in order to make it a float number")
            element = driver.find_element(By.XPATH,hn.FIELD_INPUT1)
            input_info = element.get_attribute("value")
            input_info = float(input_info)
            self.assertTrue(input_info, float(input_info))
            print(f"Float number was accepted:'{input_info}")
        except AssertionError:
            print("float number wasn't accepted")

class FireFox_Negative_Test(unittest.TestCase):
    def setUp(self):
        # Configure ChromeOptions for undetected_chromedriver
        options = webdriver.FirefoxOptions()
        # Set up Firefox options
        firefox_options = Options()
        firefox_options.add_argument("--headless")  # headless mode

        # Optional: Add other useful arguments
        firefox_options.add_argument("--disable-gpu")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--ignore-certificate-errors')
        options.page_load_strategy = 'eager'
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),
                                        options=options)
        self.driver.maximize_window()

        # Initialize the WebDriver using undetected_chromedriver

    def tearDown(self):
        self.driver.quit()

    def test_016_N(self):
        driver = self.driver
        print("Boundary testing of sliders and an input field")
        driver.get(hn.OVR_URL)

         #scroll down
        hn.scroll_down(driver, By.XPATH, hn.COST_CALC_LOCATOR)

        hn.boundary_test(driver, By.XPATH, hn.FIELD_INPUT1, 1000000000000, 0)
        hn.boundary_test(driver, By.XPATH, hn.FIELD_INPUT2, 1000000000000,0)
        hn.boundary_test(driver,By.XPATH, hn.FIELD_INPUT3, 1000000000000, 0)

    def test_017_N(self):
        print("Attempt to input invalid symbols or information in  a search tab")
        driver=self.driver
        driver.get(hn.DOC_URL)
        time.sleep(3)
        hn.is_element_present(driver, By.XPATH, hn.SEARCH_BAR)
        hn.click_on_elem(driver, By.XPATH, hn.SEARCH_BAR)
        time.sleep(3)
        hn.is_element_present(driver, By.XPATH, hn.SEARCH_BAR_2)
        hn.click_on_elem(driver,By.XPATH, hn.SEARCH_BAR_2)
        hn.enter_data(driver, By.XPATH, hn.SEARCH_BAR_2, "$#@$!", timeout=10)
        time.sleep(5)
        try:
            response = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(., 'No results for')]"))
        )
            self.assertTrue(response.is_displayed(), "Expected 'No results for' message to be visible")
        except AssertionError:
            print(f"response not found ")

    def test_018_N(self):
        print("attempting to change URL endpoint")
        driver = self.driver
        driver.get("https://x.ai/apinonexistent")
        time.sleep(2)
        error_element = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(.,'Page not found')]" ))
        )
        # gets the text from the element
        error_text = error_element.text.strip()
        expected_text ="Page not found"
        self.assertEqual(error_text, expected_text)
        print(f"Attempt ot change URL failed:'{error_text}'")

    def test_019_N(self):
        print("Verify API Endpoint Behavior with space entering .")
        driver = self.driver
        driver.get(hn.DOC_URL)
        time.sleep(3)
        hn.click_on_elem(driver, By.XPATH, hn.SEARCH_BAR)
        time.sleep(3)
        hn.is_element_present(driver, By.XPATH, hn.SEARCH_BAR_2)
        hn.click_on_elem(driver, By.XPATH, hn.SEARCH_BAR_2)
        hn.space_input(driver,By.XPATH, hn.SEARCH_BAR_2,100)

    def test_020_N(self):
        print("Attempt to input a float number into cost calculator")
        driver=self.driver
        driver.get(hn.OVR_URL)
        # scroll down
        hn.scroll_down(driver, By.XPATH, hn.COST_CALC_LOCATOR)

        try:
            hn.enter_data(driver, By.XPATH, hn.FIELD_INPUT1, "12" + Keys.LEFT + ".", 10)
            print("trying to move courser to the left in order to make it a float number")
            element = driver.find_element(By.XPATH,hn.FIELD_INPUT1)
            input_info = element.get_attribute("value")
            input_info = float(input_info)
            self.assertTrue(input_info, float(input_info))
            print(f"Float number was accepted:'{input_info}")
        except AssertionError:
            print("float number wasn't accepted")

if __name__ == "__main__":
    unittest.main(AllureReports)





















