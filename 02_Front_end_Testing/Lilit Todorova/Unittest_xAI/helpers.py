#helpers.py
import time
import random
import warnings
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Suppress specific warnings (DeprecationWarnings and ResourceWarnings)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=ResourceWarning)


def get_driver():
    """Sets up and returns a Chrome WebDriver with undetected chromedriver."""

    # Set up Chrome options to make the driver look like a human user
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    options.add_argument("--disable-infobars")  # Disable 'Chrome is being controlled' notification

    # Initialize undetected chromedriver
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    # Set implicit wait for all elements (so it can wait for elements without needing explicit delays in your tests)
    driver.implicitly_wait(10)

    return driver


def wait_for_element(driver, locator, timeout=20):
    """Waits for an element to be present on the page."""
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))


def wait_for_elements(driver, locator, timeout=20):
    """Waits for multiple elements to be present on the page."""
    return WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(locator))


def delay(min_sec=1, max_sec=3):
    """Introduces a random delay between min_sec and max_sec."""
    time.sleep(random.uniform(min_sec, max_sec))


def take_screenshot(driver, name="screenshot.png"):
    """Takes a screenshot and saves it with the given name."""
    driver.save_screenshot(name)
    print(f"Screenshot saved: {name}")


def scroll_and_delay(driver, element, min_delay=1, max_delay=2):
    """Scrolls to the element and introduces a delay."""
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    delay(min_delay, max_delay)


# Close WebDriver resources explicitly to avoid unclosed file warnings
def close_driver(driver):
    """Close the WebDriver session gracefully."""
    driver.quit()