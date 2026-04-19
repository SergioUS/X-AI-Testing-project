import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
import undetected_chromedriver as uc
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# =============== DRIVERS ===============

def create_driver(browser: str = "chrome"):
    b = (browser or "chrome").lower()

    if b == "chrome":
        # UNDTECTED CHROME (replaces regular Chrome)
        options = uc.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")

        driver = uc.Chrome(
            options=options,
            use_subprocess=False,
            version_main=146  # match your Chrome major version
        )



# def create_driver(browser: str = "chrome"):
#     b = (browser or "chrome").lower()
#
#     if b == "chrome":
#         options = webdriver.ChromeOptions()
#         options.add_argument("--window-size=1920,1080")
#
#         #options.add_argument("--headless")
#         options.page_load_strategy = "eager"
#         options.add_argument("--disable-blink-features=AutomationControlled")
#         driver = webdriver.Chrome(
#             service=ChromeService(ChromeDriverManager().install()),
#             options=options
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

# =============== FUNCTIONS ===============

def wait_link_text(driver, text, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.LINK_TEXT, text))
    )


def wait_title_contains(driver, text, timeout=10):
    WebDriverWait(driver, timeout).until(
        lambda d: text in d.title
    )

def wait_element_name(driver, name, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.NAME, name))
    )


def wait_element_xpath(driver, xpath, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )

def wait_element_css(driver, css, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css))
    )



def wait_url_contains(driver, text, timeout=10):
    WebDriverWait(driver, timeout).until(lambda d: text in d.current_url)


def wait_body(driver, timeout = 10):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

# Scroll function
def scroll_page(driver, x=0, y=0, timeout=1):
    driver.execute_script("window.scrollBy(arguments[0], arguments[1]);", x, y)
    time.sleep(timeout)

# def scroll_and_delay(driver, element, min_delay=1, max_delay=2):
#     """Scrolls to the element and introduces a delay."""
#     driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
#     delay(min_delay, max_delay)


# Click canvas point function

def click_if_text_match(text, texts, driver):
    if text in texts:
        ActionChains(driver).pause(0.3).click().perform()
        return True
    return False

def click_canvas_point(driver, canvas, x, y):
    driver.execute_script("""
        const canvas = arguments[0];
        const rect = canvas.getBoundingClientRect();
        const clickX = rect.left + arguments[1];
        const clickY = rect.top + arguments[2];

        canvas.dispatchEvent(new MouseEvent('click', {
            clientX: clickX,
            clientY: clickY,
            bubbles: true
        }));
    """, canvas, x, y)

# Pause canvas animation function
def pause_canvas_animation(driver, seconds=3):
    driver.execute_script("""
        if (!window.__canvasAnimControl) {
            window.__canvasAnimControl = { paused: false };
            window.__origRAF = window.requestAnimationFrame;

            window.requestAnimationFrame = function(callback) {
                if (window.__canvasAnimControl.paused) {
                    return 0;
                }
                return window.__origRAF(callback);
            };
        }

        window.__canvasAnimControl.paused = true;
    """)

    time.sleep(seconds)

    driver.execute_script("""
        if (window.__canvasAnimControl) {
            window.__canvasAnimControl.paused = false;
        }
    """)
#Slow down
def slow_canvas_animation(driver, delay_ms=200):
    driver.execute_script("""
        const delay = arguments[0];

        if (!window.__canvasAnimSlow) {
            window.__canvasAnimSlow = true;
            window.__origRAF = window.requestAnimationFrame;

            window.requestAnimationFrame = function(callback) {
                return setTimeout(() => window.__origRAF(callback), delay);
            };
        }
    """, delay_ms)


