import unittest
import undetected_chromedriver as uc

from selenium import webdriver


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

import HtmlTestRunner
#import AllureReports

import helpers_P as hp
import time
from selenium.webdriver.support import expected_conditions as EC


class Chrome_Positive_Test(unittest.TestCase):

    def setUp(self):
        # Configure ChromeOptions for undetected_chromedriver
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection as a bot
        options.add_argument("--start-maximized")  # Start browser maximized
        options.add_argument("--disable-web-security")  # Disable web security
        options.add_argument("--allow-running-insecure-content")  # Allow insecure content
        options.add_argument("--no-sandbox")  # Bypass OS-level restrictions
        options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource issues
        options.add_argument("--disable-gpu")  # Disable GPU acceleration
        options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging

        # Initialize the WebDriver using undetected_chromedriver
        self.driver = uc.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()

    def test_016(self):
        driver = self.driver
        print("Verifying presence of unique elements of API module")
        # Get URL of the website
        driver.get(hp.URL)
        # Function to hover on API so I can see the submodules of API
        hp.hover_over_element(driver, By.XPATH, hp.API_LOCATOR)
        # Checking visibility of Pricing submodule
        hp.wait_for_element(driver, By.XPATH, hp.overview_locator)
        # Assert that all three locators are present by using loop
        # list of locators to check
        locators = [
            ("OVERVIEW_LOCATOR", hp.overview_locator),
            ("PRICING_LOCATOR", hp.PRICING_LOCATOR),
            ("DOCUMENTATION_LOCATOR", hp.DOCUMENTATION_LOCATOR)
        ]
        # Assert that all locators are present
        for name, locator in locators:
            assert hp.is_element_present(driver, By.XPATH, locator), f"{name} is not present!"

        time.sleep(5)

    def test_017(self):

        driver = self.driver
        print("Validate functionality of a calculator field ")
        # Navigate to the website
        driver.get(hp.URL)

        # Hover over the API element to reveal submodules
        hp.hover_over_element(driver, By.XPATH, hp.API_LOCATOR)

        # Wait for the PRICING_LOCATOR element to become visible
        hp.wait_for_element(driver, By.XPATH, hp.overview_locator)

        # Click on the PRICING_LOCATOR element
        hp.click_on_elem(driver, By.XPATH, hp.overview_locator)

        # Verify that the URL changes to the pricing page
        hp.check_url(driver, hp.OVR_URL)

        hp.scroll_down(driver,By.XPATH, hp.COST_CALC_LOCATOR, 5, 10)

        hp.wait_for_element(driver, By.XPATH, hp.COST_CALC_LOCATOR)

        time.sleep(5)

        hp.random_number(driver, By.XPATH,hp.TEXT_INPUT1)
        hp.random_number(driver, By.XPATH, hp.TEXT_INPUT2)
        hp.random_number(driver, By.XPATH, hp.TEXT_INPUT3)

        time.sleep(3)

        hp.click_on_elem(driver, By.XPATH, hp.RESET_BUTTON)

        time.sleep(5)

    def test_018_P(self):
        driver = self.driver
        print("Verify that all tabs in API open ")
        driver.get(hp.URL)

        locators=[
            ("Documentation", hp.DOCUMENTATION_LOCATOR),
            ("Overview", hp.overview_locator),
            ("Pricing", hp.PRICING_LOCATOR)
        ]

        for name, locator in locators:
            print(f"Testing Tab: {name}")
            print(f"Locator Value: {locator}")
            #hovering
            print("Hovering over API menu...")
            hp.hover_over_element(driver, By.XPATH, hp.API_LOCATOR)
            #clicking on every element
            hp.click_on_elem(driver, By.XPATH, locator)
            hp.switch_new_tab(driver, "https://x.ai/", current_url=None)
            print(f"Clicking on '{name}' tab. '{name}' is open")

    def test_019_P(self):
        driver = self.driver
        print("Validate functionality of search bar in Documentations .")
        driver.get(hp.URL)

        # Hover over the API element to reveal submodules
        hp.hover_over_element(driver, By.XPATH, hp.API_LOCATOR)

        hp.click_on_elem(driver, By.XPATH, hp.DOCUMENTATION_LOCATOR)
        hp.switch_to_new_tab(driver, hp.DOC_URL)
        time.sleep(3)
        hp.click_on_elem(driver, By.XPATH, hp.SEARCH_BAR)
        time.sleep(3)
        hp.check_element_present(driver, By.XPATH, hp.SEARCH_BAR_2)
        hp.enter_data(driver, By.XPATH, hp.SEARCH_BAR_2, "Billing", timeout=10)
        time.sleep(5)
        #do I need to assert the entered data?

    def test_020_P(self):
        print("Verify that clicking the logo button on any page of the website navigates the user back to the home page ")

        # list of module URLs to test
        modules = [
            hp.OVR_URL,
            hp.PRC_URL,
            hp.DOC_URL
        ]

        try:
            for module in modules:
                print(f"Testing Home button for module: {module}")
                hp.validate_home_button(self.driver, module, hp.URL)
                print(f"Validation passed for module: {module}")

        except Exception as e:
            # Fail the test if any exception occurs
            self.fail(f"Test failed: {e}")

class Edge_Positive_Test(unittest.TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')  # Ignores SSL certificate errors

        # Initialize Edge WebDriver with service and options
        self.driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_016(self):
        driver = self.driver
        print("Verifying presence of unique elements of API module")
        # Get URL of the website
        driver.get(hp.URL)
        # Function to hover on API so I can see the submodules of API
        hp.hover_over_element(driver, By.XPATH, hp.API_LOCATOR)
        time.sleep(2)
        # Checking visibility of Pricing submodule
        hp.wait_for_element(driver, By.XPATH, hp.overview_locator)
        # Assert that all three locators are present by using loop
        # list of locators to check
        locators = [
            ("OVERVIEW_LOCATOR", hp.overview_locator),
            ("PRICING_LOCATOR", hp.PRICING_LOCATOR),
            ("DOCUMENTATION_LOCATOR", hp.DOCUMENTATION_LOCATOR)
        ]
        # Assert that all locators are present
        for name, locator in locators:
            time.sleep(6)
            assert hp.is_element_present(driver, By.XPATH, locator), f"{name} is not present!"

        time.sleep(5)

    def test_017(self):
        driver = self.driver
        print("Validate functionality of a calculator field ")
        # Navigate to the website
        driver.get(hp.OVR_URL)
        hp.scroll_down(driver,By.XPATH, hp.COST_CALC_LOCATOR, 5, 10)
        # wait for the element to appear
        hp.wait_for_element(driver, By.XPATH, hp.COST_CALC_LOCATOR)
        # gotta imitate human behaviour with this wait
        time.sleep(5)
        #
        hp.random_number(driver, By.XPATH,hp.TEXT_INPUT1)
        hp.random_number(driver, By.XPATH, hp.TEXT_INPUT2)
        hp.random_number(driver, By.XPATH, hp.TEXT_INPUT3)

        time.sleep(3)

        hp.click_on_elem(driver, By.XPATH, hp.RESET_BUTTON)

        time.sleep(5)

    def test_018_P(self):
        driver = self.driver
        print("Verify that all tabs in API open ")
        driver.get(hp.URL)
        time.sleep(2)

        locators=[
            ("Documentation", hp.DOCUMENTATION_LOCATOR),
            ("Overview", hp.overview_locator),
            ("Pricing", hp.PRICING_LOCATOR)
        ]

        for name, locator in locators:
            print(f"Testing Tab: {name}")
            print(f"Locator Value: {locator}")
            #hovering
            print("Hovering over API menu...")
            hp.hover_over_element(driver, By.XPATH, hp.API_LOCATOR)
            time.sleep(2)
            #clicking on every element
            hp.click_on_elem(driver, By.XPATH, locator)
            print(f"Clicking on '{name}' tab. '{name}' is open")

    def test_019_P(self):
        driver = self.driver
        print("Validate functionality of search bar in Documentations .")
        driver.get(hp.DOC_URL)

        # Hover over the API element to reveal submodules
        #hp.hover_over_element(driver, By.XPATH, hp.API_LOCATOR)

        #hp.click_on_elem(driver, By.XPATH, hp.DOCUMENTATION_LOCATOR)
        #hp.switch_to_new_tab(driver, hp.DOC_URL)
        time.sleep(3)
        hp.click_on_elem(driver, By.XPATH, hp.SEARCH_BAR)
        time.sleep(3)
        hp.check_element_present(driver, By.XPATH, hp.SEARCH_BAR_2)
        hp.enter_data(driver, By.XPATH, hp.SEARCH_BAR_2, "Billing", timeout=10)
        time.sleep(5)
        #do I need to assert the entered data?

    def test_020_P(self):
        print("Verify that clicking the logo button on any page of the website navigates the user back to the home page ")

        # list of module URLs to test
        modules = [
            hp.OVR_URL,
            hp.PRC_URL,
            hp.DOC_URL
        ]

        try:
            for module in modules:
                print(f"Testing Home button for module: {module}")
                time.sleep(5)
                hp.validate_home_button(self.driver, module, hp.URL)
                time.sleep(5)
                print(f"Validation passed for module: {module}")

        except Exception as e:
            # Fail the test if any exception occurs
            self.fail(f"Test failed: {e}")

class FireFox_Positive_Test(unittest.TestCase):

    def setUp(self):
        # Configure ChromeOptions for undetected_chromedriver
        options = webdriver.FirefoxOptions()
        # Set up Firefox options
        firefox_options = Options()
        #firefox_options.add_argument("--headless")  # headless mode

        # Optional: Add other useful arguments
        firefox_options.add_argument("--disable-gpu")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--ignore-certificate-errors')
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),
                                        options=options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_016(self):
        driver = self.driver
        print("Verifying presence of unique elements of API module")
        # Get URL of the website
        driver.get(hp.URL)
        # Function to hover on API so I can see the submodules of API
        hp.hover_over_element(driver, By.XPATH, hp.API_LOCATOR)
        time.sleep(2)
        # Checking visibility of Pricing submodule
        hp.wait_for_element(driver, By.XPATH, hp.overview_locator)
        # Assert that all three locators are present by using loop
        # list of locators to check
        locators = [
            ("OVERVIEW_LOCATOR", hp.overview_locator),
            ("PRICING_LOCATOR", hp.PRICING_LOCATOR),
            ("DOCUMENTATION_LOCATOR", hp.DOCUMENTATION_LOCATOR)
        ]
        # Assert that all locators are present
        for name, locator in locators:
            time.sleep(6)
            assert hp.is_element_present(driver, By.XPATH, locator), f"{name} is not present!"

        time.sleep(5)

    def test_017(self):

        driver = self.driver
        print("Validate functionality of a calculator field ")
        # Navigate to the website
        driver.get(hp.OVR_URL)


        hp.scroll_down(driver,By.XPATH, hp.COST_CALC_LOCATOR, 5, 10)

        hp.wait_for_element(driver, By.XPATH, hp.COST_CALC_LOCATOR)

        time.sleep(5)

        hp.random_number(driver, By.XPATH,hp.TEXT_INPUT1)
        hp.random_number(driver, By.XPATH, hp.TEXT_INPUT2)
        hp.random_number(driver, By.XPATH, hp.TEXT_INPUT3)

        time.sleep(3)

        hp.click_on_elem(driver, By.XPATH, hp.RESET_BUTTON)

        time.sleep(5)

    # def test_018_P(self):
    #     driver = self.driver
    #     print("Verify that all tabs in API open ")
    #     driver.get(hp.URL)
    #
    #     home_window = driver.current_window_handle
    #
    #     locators = [
    #         ("Documentation", hp.DOCUMENTATION_LOCATOR),
    #         ("Overview", hp.overview_locator),
    #         ("Pricing", hp.PRICING_LOCATOR)
    #     ]
    #
    #     for name, locator in locators:
    #         elem = WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))
    #         elem.click()
    #         hp.switch_new_tab(driver, "https://x.ai/", current_url=None)
    #         print(f"clicking on '{name}'. It is open in a new tab")

    def test_019_P(self):
        driver = self.driver
        print("Validate functionality of search bar in Documentations .")
        driver.get(hp.DOC_URL)
        hp.wait_for_element(driver, By.XPATH, hp.SEARCH_BAR)
        hp.click_on_elem(driver, By.XPATH, hp.SEARCH_BAR)
        time.sleep(3)
        hp.check_element_present(driver, By.XPATH, hp.SEARCH_BAR_2)
        hp.enter_data(driver, By.XPATH, hp.SEARCH_BAR_2, "Billing", timeout=10)
        time.sleep(5)
        #do I need to assert the entered data?

    def test_020_P(self):
        print("Verify that clicking the logo button on any page of the website navigates the user back to the home page ")

        # list of module URLs to test
        modules = [
            hp.OVR_URL,
            hp.PRC_URL,
            hp.DOC_URL
        ]

        try:
            for module in modules:
                print(f"Testing Home button for module: {module}")
                hp.validate_home_button(self.driver, module, hp.URL)
                print(f"Validation passed for module: {module}")

        except Exception as e:
            # Fail the test if any exception occurs
            self.fail(f"Test failed: {e}")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

