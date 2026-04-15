from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions

class Helper:
    def make_driver(browser: str):
        b = browser.lower()

        if b == "chrome":
            options = uc.ChromeOptions()
            driver = uc.Chrome(options=options, use_subprocess=False, version_main=146)
            driver.set_window_size(1920, 1024)
            return driver

        if b == "edge":
            options = EdgeOptions()
            driver = webdriver.Edge(options=options)
            driver.set_window_size(1920, 1024)
            return driver

        raise ValueError(f"Unsupported browser: '{browser}'. Use chrome / edge.")

    URL = "https://x.ai"

    # ===== MENU =====
    GROK = (By.XPATH, "//nav//a[@href='/grok']")
    API = (By.XPATH, "//nav//a[@href='/api']")
    COMPANY = (By.XPATH, "//nav//a[@href='/company']")
    COLOSSUS = (By.XPATH, "//nav//a[@href='/colossus']")
    CAREERS = (By.XPATH, "//nav//a[@href='/careers']")
    NEWS = (By.XPATH, "//nav//a[@href='/news']")
    SHOP = (By.XPATH, "//nav//a[@href='https://shop.x.ai']")
    SPACEX = (By.XPATH, "//nav//a[contains(@href, 'spacex')]")
    X_LINK = (By.XPATH, "//nav//a[@href='https://x.com']")
    TRY_GROK = (By.XPATH, "//a[contains(., 'Try Grok')]")

    # ===== SECTION MENU =====
    HERO_HEADING = (By.XPATH, "//h1[contains(., 'AI for all humanity')]")
    UNDERSTAND_UNIVERSE = (By.XPATH, "//canvas[@data-engine]")
    SECTION_GROK = (By.XPATH, "//h3[contains(text(), 'Grok') and contains(@class, 'group-hover')]")
    SECTION_API = (By.XPATH, "//h3[contains(text(), 'API') and contains(@class, 'group-hover')]")
    SECTION_DEVELOPER_DOCS = (By.XPATH, "//*[contains(text(), 'Developer Docs')]")
    SUPERGROK = (By.XPATH, "//*[contains(text(), 'SuperGrok')]")
    LATEST_NEWS = (By.XPATH, "//*[contains(., 'Latest news')]")

    # ===== BTN SECTION =====
    BTN_USE_NOW = (By.XPATH, " //button[contains(text(), 'Use now')]")
    BTN_BUILD_NOW = (By.XPATH, " //button[contains(text(), 'Build now')]")
    BTN_LEARN_MORE = (By.XPATH, " //button[contains(text(), 'Learn more')]")
    BTN_SIGN_UP_NOW = (By.XPATH, "//a[contains(text(), 'Sign up now')]")
    BTN_EXPLORE_MORE = (By.XPATH, "//a[contains(text(), 'Explore more')]")

    # ===== FOOTER =====
    FOOTER = (By.XPATH, "//*[contains(@style, 'footer')]")

    # TRY GROK ON
    FOOTER_TRY_GROK_ON = (By.XPATH, "//span[contains(text(), 'Try Grok On')]")
    FOOTER_WEB = (By.XPATH, "//a[@href='https://grok.com']")
    FOOTER_IOS = (By.XPATH, "//a[contains(@href, 'apps.apple.com')]")
    FOOTER_ANDROID = (By.XPATH, "//a[contains(@href, 'play.google.com')]")
    FOOTER_GROK_ON_X = (By.XPATH, "//a[@href='https://x.com/i/grok']")

    # PRODUCTS
    FOOTER_PRODUCTS = (By.XPATH, "//span[contains(text(), 'Products') and contains(@class, 'text')]")
    FOOTER_GROK = (By.XPATH, "//a[@href='/grok' and not(ancestor::header)]")
    FOOTER_GROKIPEDIA = (By.XPATH, "//a[contains(@href, 'grokipedia')]")

    # API
    FOOTER_API = (By.XPATH, "//span[contains(text(), 'API') and contains(@class, 'text')]")
    FOOTER_API_OVERVIEW = (By.XPATH, "//a[@href='/api/voice']")
    FOOTER_API_PRICING = (By.XPATH, "//a[contains(@href, 'pricing')]")
    FOOTER_API_DOCS = (By.XPATH, "//a[contains(@href, 'docs.x.ai') and contains(text(), 'Documentation')]")

    # COMPANY
    FOOTER_COMPANY = (By.XPATH, "//span[contains(text(), 'Company') and contains(@class, 'text')]")
    FOOTER_CONTACT = (By.XPATH, "//a[contains(@href, '/contact')]")
    FOOTER_CAREERS = (By.XPATH, "//a[contains(@href, '/careers') and not(ancestor::header)]")

    # RESOURCES
    FOOTER_RESOURCES = (By.XPATH, "//span[contains(text(), 'Resources') and contains(@class, 'text')]")
    FOOTER_PRIVACY_POLICY = (By.XPATH, "//a[contains(@href, '/privacy-policy')]")
    FOOTER_SECURITY = (By.XPATH, "//a[contains(@href, '/security')]")
    FOOTER_LEGAL = (By.XPATH, "//a[contains(@href, '/legal')]")
    FOOTER_STATUS = (By.XPATH, "//a[contains(@href, 'status.')]")

    # ===== SHOP =====
    SHOP_LOGO = (By.XPATH, "//*[@href='/']")
    SHOP_COLLECTION = (By.XPATH, "//*[contains(., 'Collection')]")
    SHOP_PRODUCT_CARD = (By.XPATH, "//*[@class='product-card']")
    SHOP_FIRST_PRODUCT = (By.XPATH, "//*[@class='product-card'][1]")
    SHOP_PRODUCT_LIST = (By.XPATH, "//*[contains(@class, 'product-list')]")
    SHOP_ADD_TO_CART = (By.XPATH, "//*[contains(text(), 'Add To Cart')]")
    SHOP_CART_BODY = (By.XPATH, "//*[@class='order-summary__body']")
    SHOP_QTY = (By.XPATH, "(//input[@name='updates[]'])[1]")
    SHOP_UPDATE_BTN = (By.XPATH, "//button[contains(text(), 'needs to be updated')]")
    SHOP_CHECKOUT_BTN = (By.XPATH, "//button[@name='checkout']")
    SHOP_CHECKOUT_H1 = (By.XPATH, "//strong[contains(text(), 'Information')]")
    SHOP_EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    SHOP_SHIPPING_HEADER = (By.XPATH, "//h2[@id='deliveryAddress']")
    SHOP_BREADCRUMB = (By.XPATH, "//*[contains(., 'Cart') and contains(., 'Shipping')]")
    SHOP_BTN = (By.XPATH, "//button[contains(@class,'minmaxify-ok')]")

    # ===== CHATBOT =====
    CHAT_INPUT = (By.XPATH, "//textarea")
    CHAT_INPUT_GROK = (By.XPATH, "//*[@data-placeholder]")
    CHAT_SEND_BTN = (By.XPATH, "//button[@type='submit']")
    CHAT_RESPONSE = (By.XPATH, "//p[contains(@class, 'last')]")
    ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'limit reached')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.wait_long = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def is_visible(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except Exception:
            return False

    def is_clickable(self, locator):
        try:
            def _has_clickable(d):
                elements = d.find_elements(*locator)
                for element in elements:
                    try:
                        if not element.is_displayed():
                            continue
                        if element.get_attribute("disabled") is not None:
                            continue
                        if element.get_attribute("aria-disabled") == "true":
                            continue
                        return True
                    except StaleElementReferenceException:
                        continue
                return False

            self.wait.until(_has_clickable)
            return True
        except Exception:
            return False

    def is_button_disabled(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            disabled = element.get_attribute("disabled")
            aria_disabled = element.get_attribute("aria-disabled")
            return disabled is not None or aria_disabled == "true"
        except Exception:
            return False

    def click(self, locator):
        current_url = self.driver.current_url
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)
        try:
            self.wait.until(lambda d: d.current_url != current_url)
        except Exception:
            self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def get_href(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).get_attribute("href")

    def get_current_url(self):
        return self.driver.current_url

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_by(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

        # ===== SHOP =====

    def add_first_product_to_cart(self, shop_url="https://shop.x.com"):
        self.driver.get(shop_url)
        self.wait_long.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        first_product = self.wait_long.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@class='product-card'][1]//a")
            )
        )
        first_product.click()
        self.wait_long.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        add_btn = self.wait_long.until(
            EC.element_to_be_clickable(self.SHOP_ADD_TO_CART)
        )
        add_btn.click()
        self.wait_long.until(
            lambda d: "/cart" in d.current_url
        )

    # ===== CHAT =====
    def type_message(self, text):
        input_field = self.wait.until(EC.visibility_of_element_located(self.CHAT_INPUT))
        input_field.clear()
        input_field.send_keys(text)

    def send_message_by_button(self):
        self.click(self.CHAT_SEND_BTN)

    def send_message_by_enter(self, text):
        input_field = self.wait.until(EC.visibility_of_element_located(self.CHAT_INPUT))
        input_field.clear()
        input_field.send_keys(text)
        input_field.send_keys(Keys.RETURN)

    def get_chat_input_value(self):
        try:
            input_field = self.wait.until(EC.visibility_of_element_located(self.CHAT_INPUT))
            return input_field.get_attribute("value") or ""
        except TimeoutException:
            return ""

    def wait_for_response(self):
        return self.wait_long.until(EC.visibility_of_element_located(self.CHAT_RESPONSE))

    def page_has_no_crash(self):
        title = self.driver.title.lower()
        return "500" not in title and "404" not in title and "error" not in title