import unittest
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import helpers_P as hp
import time


class PositiveTest(unittest.TestCase):

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
        # get URL of the website
        driver.get(hp.URL)
        # function to hover on API so I can see the submodules of API
        hp.hover_over_element(driver, By.XPATH, hp.API_LOCATOR)
       # checking visibility of Pricing submodule
        hp.wait_for_element(driver, By.XPATH, hp.CAPABILITIES_LOCATOR)

        # Assert that all three locators are present by using loop
        # list of locators to check
        locators = [
            ("CAPABILITIES_LOCATOR", hp.CAPABILITIES_LOCATOR),
            ("PRICING_LOCATOR", hp.PRICING_LOCATOR),
            ("DOCUMENTATION_LOCATOR", hp.DOCUMENTATION_LOCATOR)
        ]

        # Assert that all locators are present
        for name, locator in locators:
            assert hp.is_element_present(driver, By.XPATH, locator), f"{name} is not present!"


        time.sleep(5)


    def test_017(self):

        driver = self.driver
        print("Positive test case 017")
        # Navigate to the website
        driver.get(hp.URL)

        # Hover over the API element to reveal submodules
        hp.hover_over_element(driver, By.XPATH, hp.API_LOCATOR)

        # Wait for the PRICING_LOCATOR element to become visible
        hp.wait_for_element(driver, By.XPATH, hp.PRICING_LOCATOR)

        # Click on the PRICING_LOCATOR element
        hp.click_on_elem(driver, By.XPATH, hp.PRICING_LOCATOR)

        # Verify that the URL changes to the pricing page
        expected_url = "https://x.ai/api#pricing"
        hp.check_url(driver, expected_url)

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
        print("Positive test case 018")
        driver.get(hp.URL)

        # Hover over the API element to reveal submodules
        hp.hover_over_element(driver, By.XPATH, hp.API_LOCATOR)

        hp.click_on_elem(driver, By.XPATH, hp.CAPABILITIES_LOCATOR)

        hp.hover_over_element(driver, By.XPATH, hp.API_LOCATOR)

        hp.click_on_elem(driver, By.XPATH, hp.PRICING_LOCATOR)

        hp.hover_over_element(driver, By.XPATH, hp.API_LOCATOR)

        hp.click_on_elem(driver, By.XPATH, hp.DOCUMENTATION_LOCATOR)


    def test_019_P(self):
        driver = self.driver
        print("Positive test case 019")
        driver.get(hp.URL)

        # Hover over the API element to reveal submodules
        hp.hover_over_element(driver, By.XPATH, hp.API_LOCATOR)

        hp.click_on_elem(driver, By.XPATH, hp.DOCUMENTATION_LOCATOR)
        hp.switch_to_new_tab(driver, hp.EXP_DOC_TITLE)
        time.sleep(3)
        hp.click_on_elem(driver, By.XPATH, hp.SEARCH_BAR)
        time.sleep(3)
        hp.check_element_present(driver, By.XPATH, hp.SEARCH_BAR_2)
        hp.enter_data(driver, By.XPATH, hp.SEARCH_BAR_2, "Billing", timeout=10)
        time.sleep(5)


    def test_020_P(self):

        # list of module URLs to test
        modules = [
            hp.CAP_URL,
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


if __name__ == "__main__":
    unittest.main()