import unittest  # Python's built-in unit testing framework
import time      # For time-related functions
import random
import os        # For operating-system-related operations
# import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait
import Helpers as HP
from selenium import webdriver

# Load driver managers:
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Load services for Chrome, Edge, and Firefox:
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

# Load testing tools:
from selenium.webdriver.common.by import By  # Locator strategies
from selenium.webdriver.common.keys import Keys  # Keyboard keys simulation
from selenium.webdriver.common.action_chains import ActionChains  # Complex mouse/keyboard actions
from selenium.common import WebDriverException as WDE, NoSuchElementException  # Exception handling
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # Wait conditions
from faker import Faker

# # patcher.py
# from packaging.version import Version
#
# def version_check(version_1, version_2):
#     return Version(version_1) < Version(version_2)

def delay():
    time.sleep(random.randint(2,4))


class ChromePositiveTestes(unittest.TestCase):
        def setUp(self):
            options = webdriver.ChromeOptions()
            #options.add_argument('--ignore-certificate-errors')
            #options.page_load_strategy = 'eager'
            options.add_argument("--disable-blink-features=AutomationControlled")
            #options.add_argument('--headless')
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            self.driver.maximize_window()

        def test_TC_P_006(self):
            #driver = self.driver=uc.Chrome()
            print("TC_P_006")
            driver = self.driver

            #  1. Navigate to x.AI homepage
            driver.get(HP.colossus_url)
            delay()

            # wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@height,'534')]")))

            # 2. Observe the browser title bar, verify <title> and title bar match

            # 3. Navigate to x.ai/colossus

            # 4. Observe the browser title bar, verify <title> and title bar match
            self.assertEqual(self.title, "Colossus | xAI")

        def test_TC_P_007(self):
            driver = self.driver
            print("TC_P_007")

            # 1. Set browser resolution to 1920x1080 (desktop view)
            driver.set_window_size(1920, 1080)
            print("Set resolution to 1920x1080")

            # 2. Navigate to the Colossus page
            self.driver.get(HP.colossus_url)

            # 3. Verify layout or elements (example check)
            self.assertIn("Colossus", driver.title)
            print(f"Title verified for 1920x1080: {driver.title}")

            # 4. Set browser resolution to 768x1024 (tablet view)
            driver.set_window_size(768, 1024)
            print("Set resolution to 768x1024")

            # 5. Reload Colossus page
            self.driver.refresh()

            # 6. Verify layout (example check)
            self.assertIn("Colossus", driver.title)
            print(f"Title verified for 768x1024: {driver.title}")

            # 7. Set browser resolution to 375x667 (mobile view)
            driver.set_window_size(375, 667)
            print("Set resolution to 375x667")

            # 8. Reload Colossus page
            self.driver.refresh()

            # 9. Verify layout (example check)
            self.assertIn("Colossus", driver.title)
            print(f"Title verified for 375x667: {driver.title}")
