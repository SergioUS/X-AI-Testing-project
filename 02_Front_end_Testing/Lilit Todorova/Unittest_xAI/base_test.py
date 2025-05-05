import os
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

from helpers import get_driver, close_driver, delay, scroll_and_delay, wait_for_element
from locators import CareersLocators, ApplicationLocators


class BaseTest(unittest.TestCase):
    def setUp(self):
        # Pick up BROWSER and HEADLESS from env, default to Chrome
        self.browser = os.getenv("BROWSER", "chrome").lower()
        print(f"\n=== Starting tests on: {self.browser.upper()} ===")
        self.driver = get_driver()
        self.base_url = "https://x.ai"

    def tearDown(self):
        close_driver(self.driver)

    def _open_application_form(self, timeout=15):
        # 1) Navigate to Open Roles and click first AI Engineer & Researcher link
        self.driver.get(f"{self.base_url}/careers/open-roles")
        delay(2, 3)
        element = wait_for_element(self.driver, CareersLocators.AI_ENGINEER_RESEARCHER, timeout)
        scroll_and_delay(self.driver, element)
        href = element.get_attribute("href")
        self.driver.get(href)

        # 2) Wait for Greenhouse URL
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.current_url.startswith("https://job-boards.greenhouse.io")
        )

        # 3) Click "Apply" reliably (handles stale references)
        apply_locator = (
            By.XPATH,
            "//button[contains(text(),'Apply') or contains(text(),'Apply Now')]"
        )
        # wait until clickable
        apply_btn = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(apply_locator)
        )
        # scroll into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            apply_btn
        )
        # attempt click, retry if stale
        try:
            apply_btn.click()
        except StaleElementReferenceException:
            apply_btn = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(apply_locator)
            )
            apply_btn.click()

        # 4) Wait for the form’s work-experience textarea to confirm load
        wait_for_element(self.driver, ApplicationLocators.WORK_EXPERIENCE_TEXTAREA, timeout)
