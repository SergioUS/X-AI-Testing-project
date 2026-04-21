import os
import time
import random
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# import undetected_chromedriver as uc

# ----------------------------
# Drivers
# ----------------------------

def create_driver(browser: str = "chrome"):
    b = (browser or "chrome").lower()

    if b == "chrome":
        options = webdriver.ChromeOptions()
        options.page_load_strategy = "eager"
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

# def create_driver(browser: str = "chrome"):
#     b = (browser or "chrome").lower()
#
#     if b == "chrome":
#         # UNDTECTED CHROME (replaces regular Chrome)
#         options = uc.ChromeOptions()
#         options.add_argument("--start-maximized")
#         options.add_argument("--disable-blink-features=AutomationControlled")
#         options.add_argument("--window-size=1920,1080")
#
#         driver = uc.Chrome(
#             options=options,
#             use_subprocess=False,
#             version_main=146   # match your Chrome major version
#         )
    elif b == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    elif b == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Edge(
            service=EdgeService("/usr/local/bin/msedgedriver"),
            options=options
        )

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    return driver



# ----------------------------
# Simple helpers
# ----------------------------
def delay(min_s=2, max_s=5):
    time.sleep(random.randint(min_s, max_s))


def take_screenshot(driver, folder="screenshots_Wiki"):
    os.makedirs(folder, exist_ok=True)
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    path = f"{folder}/error_{now}.png"
    driver.save_screenshot(path)
    print(f"Screenshot saved to {path}")
    return path


def size25_percent(driver):
    driver.execute_script("document.body.style.zoom='25%'")


# ----------------------------
# Wait helpers (replace sleep)
# ----------------------------
def wait_body(driver, timeout=15):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


def wait_url_contains(driver, part, timeout=15):
    WebDriverWait(driver, timeout).until(lambda d: part in d.current_url)


def wait_url_starts(driver, expected_url, timeout=15):
    WebDriverWait(driver, timeout).until(lambda d: d.current_url.startswith(expected_url))


def wait_clickable(driver, locator, timeout=15):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def wait_visible(driver, locator, timeout=15):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))


def wait_present(driver, locator, timeout=15):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))


# ----------------------------
# Cookies (keyboard)
# ----------------------------
def accept_cookies_with_keyboard(driver, timeout=7):
    wait_body(driver, timeout=timeout)

    # focus on page
    driver.find_element(By.TAG_NAME, "body").click()

    # TAB TAB TAB ENTER
    driver.switch_to.active_element.send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER)


# ----------------------------
# Common actions (re-used in tests)
# ----------------------------

def scroll_to_bottom(driver):
    """Used in TC_P_011: scroll to the footer (bottom of the page)."""
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def fill_input(driver, locator, text, timeout=15):
    """
    Used in TC_P_015: common pattern for inputs (click -> clear -> send_keys).
    Use this instead of repeating the same block for every field.
    """
    el = wait_clickable(driver, locator, timeout)
    el.click()
    el.clear()
    el.send_keys(text)
    return el


def shadow_click(driver, css_selector):
    """
    Used in TC_P_011..TC_P_014: click an element even if it is inside shadow DOM.
    Returns True if clicked, False if not found.
    """
    script = """
        const sel = arguments[0];

        function findAndClick(root) {
            const el = root.querySelector(sel);
            if (el) { el.click(); return true; }

            for (const node of root.querySelectorAll("*")) {
                if (node.shadowRoot) {
                    if (findAndClick(node.shadowRoot)) return true;
                }
            }
            return false;
        }

        return findAndClick(document);
    """
    return driver.execute_script(script, css_selector)


def shadow_click_and_return_href(driver, css_selector):
    """
    Used in TC_P_014: click a link in shadow DOM and return its href (useful for logs/verification).
    Returns href string or None.
    """
    script = """
        const sel = arguments[0];

        function findAndClick(root) {
            const el = root.querySelector(sel);
            if (el) {
                const href = el.getAttribute("href") || "";
                el.click();
                return href || null;
            }

            for (const node of root.querySelectorAll("*")) {
                if (node.shadowRoot) {
                    const found = findAndClick(node.shadowRoot);
                    if (found) return found;
                }
            }
            return null;
        }

        return findAndClick(document);
    """
    return driver.execute_script(script, css_selector)


def shadow_find(driver, css_selector):
    """
    Used in TC_P_015: find an element inside shadow DOM and return it as a WebElement.
    Returns WebElement or None.
    """
    script = """
        const sel = arguments[0];

        function findInShadows(root) {
            const el = root.querySelector(sel);
            if (el) return el;

            for (const node of root.querySelectorAll("*")) {
                if (node.shadowRoot) {
                    const found = findInShadows(node.shadowRoot);
                    if (found) return found;
                }
            }
            return null;
        }

        return findInShadows(document);
    """
    return driver.execute_script(script, css_selector)


def wait_shadow(driver, css_selector, timeout=15, poll=0.2):
    """
    Replaces time.sleep() for shadow DOM elements.
    Waits until an element appears inside shadow DOM and returns it.
    """
    end = time.time() + timeout
    last = None

    while time.time() < end:
        try:
            el = shadow_find(driver, css_selector)
            if el:
                return el
        except Exception as e:
            last = e
        time.sleep(poll)

    raise TimeoutError(f"Shadow element not found: {css_selector}. Last error: {last}")


def keyboard_select_next_option(driver):
    """
    Used in TC_P_015: TAB + SPACE + DOWN + ENTER to select an option via keyboard (accessibility style).
    """
    driver.switch_to.active_element.send_keys(Keys.TAB, Keys.SPACE, Keys.ARROW_DOWN, Keys.ENTER)


def keyboard_tab_times_then_space(driver, times=5):
    """
    Used in TC_P_015: press TAB N times, then SPACE (example: captcha focus attempt).
    """
    keys = [Keys.TAB] * times + [Keys.SPACE]
    driver.switch_to.active_element.send_keys(*keys)

def keyboard_tab(driver, times=1):
    driver.switch_to.active_element.send_keys(*([Keys.TAB] * times))

def keyboard_activate(driver):
    # Enter usually works; Space is fallback for buttons
    driver.switch_to.active_element.send_keys(Keys.ENTER)


def get_shadow(driver, element):
    return driver.execute_script("return arguments[0].shadowRoot", element)
