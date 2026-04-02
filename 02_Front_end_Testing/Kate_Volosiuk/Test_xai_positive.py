import unittest

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import Helper


def make_driver():
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = uc.Chrome(options=options, use_subprocess=False, version_main=146)
    return driver


# ===== 1. PAGE LOAD =====
class TestPageLoad(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = make_driver()
        cls.helper = Helper(cls.driver)
        cls.addClassCleanup(cls.driver.quit)

    def setUp(self):
        self.helper.open()

    def test_TC_P_026_page_open(self):
        """Page x.ai opens successfully"""
        self.assertIn("x.ai", self.helper.get_current_url())

    def test_TC_P_027_page_title_not_empty(self):
        """Page title is not empty"""
        self.assertTrue(len(self.driver.title) > 0)

    def test_TC_P_028_page_title_contains_xai(self):
        """Page title contains xAI"""
        title = self.driver.title.lower()
        self.assertTrue("xai" in title)

    def test_TC_P_029_hero_heading_visible(self):
        """Hero heading AI for all humanity is displayed"""
        self.assertTrue(self.helper.is_visible(self.helper.HERO_HEADING))

    def test_TC_P_030_page_has_no_crash(self):
        """Page returns no 404/500 errors"""
        self.assertTrue(self.helper.page_has_no_crash())


# ===== 2. TOP MENU =====
class TestTopMenu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = make_driver()
        cls.helper = Helper(cls.driver)
        cls.addClassCleanup(cls.driver.quit)

    def setUp(self):
        self.helper.open()

    def test_TC_P_031_menu_grok_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.GROK))

    def test_TC_P_032_menu_api_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.API))

    def test_TC_P_033_menu_company_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.COMPANY))

    def test_TC_P_034_menu_colossus_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.COLOSSUS))

    def test_TC_P_035_menu_careers_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.CAREERS))

    def test_TC_P_036_menu_news_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.NEWS))

    def test_TC_P_037_menu_shop_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.SHOP))

    def test_TC_P_038_menu_spacex_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.SPACEX))

    def test_TC_P_039_try_grok_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.TRY_GROK))

    def test_TC_P_040_grok_clickable(self):
        self.assertTrue(self.helper.is_clickable(self.helper.GROK))

    def test_TC_P_041_api_clickable(self):
        self.assertTrue(self.helper.is_clickable(self.helper.API))

    def test_TC_P_042_company_clickable(self):
        self.assertTrue(self.helper.is_clickable(self.helper.COMPANY))

    def test_TC_P_043_colossus_clickable(self):
        self.assertTrue(self.helper.is_clickable(self.helper.COLOSSUS))

    def test_TC_P_044_careers_clickable(self):
        self.assertTrue(self.helper.is_clickable(self.helper.CAREERS))

    def test_TC_P_045_news_clickable(self):
        self.assertTrue(self.helper.is_clickable(self.helper.NEWS))

    def test_TC_P_046_shop_clickable(self):
        self.assertTrue(self.helper.is_clickable(self.helper.SHOP))

    def test_TC_P_047_spacex_clickable(self):
        self.assertTrue(self.helper.is_clickable(self.helper.SPACEX))

    def test_TC_P_048_try_grok_clickable(self):
        self.assertTrue(self.helper.is_clickable(self.helper.TRY_GROK))

    def test_TC_P_049_grok_has_href(self):
        self.assertTrue(self.helper.get_href(self.helper.GROK))

    def test_TC_P_050_api_has_href(self):
        self.assertTrue(self.helper.get_href(self.helper.API))

    def test_TC_P_051_try_grok_has_href(self):
        self.assertTrue(self.helper.get_href(self.helper.TRY_GROK))

    def test_TC_P_052_careers_has_href(self):
        self.assertTrue(self.helper.get_href(self.helper.CAREERS))

    def test_TC_P_053_news_has_href(self):
        self.assertTrue(self.helper.get_href(self.helper.NEWS))


# ===== 3. NAVIGATION =====
# Same-tab navigation: Grok, API, Company, Colossus, Careers, News
class TestNavigationSameTab(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = make_driver()
        cls.helper = Helper(cls.driver)
        cls.addClassCleanup(cls.driver.quit)

    def setUp(self):
        self.helper.open()

    def test_TC_P_054_click_grok_navigates(self):
        self.helper.click(self.helper.GROK)
        self.assertIn("grok", self.helper.get_current_url().lower())

    def test_TC_P_055_click_api_navigates(self):
        self.helper.click(self.helper.API)
        self.assertIn("api", self.helper.get_current_url().lower())

    def test_TC_P_056_click_company_navigates(self):
        self.helper.click(self.helper.COMPANY)
        self.assertIn("company", self.helper.get_current_url().lower())

    def test_TC_P_057_click_colossus_navigates(self):
        self.helper.click(self.helper.COLOSSUS)
        self.assertIn("colossus", self.helper.get_current_url().lower())

    def test_TC_P_058_click_careers_navigates(self):
        self.helper.click(self.helper.CAREERS)
        self.assertIn("careers", self.helper.get_current_url().lower())

    def test_TC_P_059_click_news_navigates(self):
        self.helper.click(self.helper.NEWS)
        self.assertIn("news", self.helper.get_current_url().lower())

    def test_TC_P_060_back_from_grok(self):
        self.helper.click(self.helper.GROK)
        self.driver.back()
        self.assertIn("x.ai", self.helper.get_current_url())

    def test_TC_P_061_back_from_api(self):
        self.helper.click(self.helper.API)
        self.driver.back()
        self.assertIn("x.ai", self.helper.get_current_url())

    def test_TC_P_062_back_from_news(self):
        self.helper.click(self.helper.NEWS)
        self.driver.back()
        self.assertIn("x.ai", self.helper.get_current_url())


# New-tab navigation: Shop, SpaceX, X
class TestNavigationNewTab(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = make_driver()
        cls.helper = Helper(cls.driver)
        cls.addClassCleanup(cls.driver.quit)

    def setUp(self):
        # Remember main tab and open page
        self.helper.open()
        self.main_handle = self.driver.current_window_handle
        self.addCleanup(self._close_extra_tabs)

    def _close_extra_tabs(self):
        # Close all extra tabs, return to main tab
        for handle in self.driver.window_handles:
            if handle != self.main_handle:
                self.driver.switch_to.window(handle)
                self.driver.close()
        self.driver.switch_to.window(self.main_handle)

    def _click_and_switch_to_new_tab(self, locator):
        """Click, wait for new tab, switch to it"""
        original_handles = set(self.driver.window_handles)
        self.helper.click(locator)
        self._wait_for_new_tab(original_handles)
        new_handle = set(self.driver.window_handles) - original_handles
        self.driver.switch_to.window(new_handle.pop())

    def _wait_for_new_tab(self, original_handles):
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > len(original_handles)
        )

    def test_TC_P_063_click_shop_opens_new_tab(self):
        """Click on Shop opens a new tab"""
        original_handles = set(self.driver.window_handles)
        self.helper.click(self.helper.SHOP)
        self._wait_for_new_tab(original_handles)
        self.assertGreater(len(self.driver.window_handles), len(original_handles))

    def test_TC_P_064_click_shop_navigates(self):
        """Click on Shop navigates to shop page"""
        self._click_and_switch_to_new_tab(self.helper.SHOP)
        self.assertIn("shop", self.helper.get_current_url().lower())

    def test_TC_P_065_click_spacex_opens_new_tab(self):
        """Click on SpaceX opens a new tab"""
        original_handles = set(self.driver.window_handles)
        self.helper.click(self.helper.SPACEX)
        self._wait_for_new_tab(original_handles)
        self.assertGreater(len(self.driver.window_handles), len(original_handles))

    def test_TC_P_066_click_spacex_navigates(self):
        """Click on SpaceX navigates to spacex page"""
        self._click_and_switch_to_new_tab(self.helper.SPACEX)
        self.assertIn("spacex", self.helper.get_current_url().lower())

    def test_TC_P_067_click_x_opens_new_tab(self):
        """Click on X opens a new tab"""
        original_handles = set(self.driver.window_handles)
        self.helper.click(self.helper.X_LINK)
        self._wait_for_new_tab(original_handles)
        self.assertGreater(len(self.driver.window_handles), len(original_handles))

    def test_TC_P_068_click_x_navigates(self):
        """Click on X navigates to x.com or twitter.com"""
        self._click_and_switch_to_new_tab(self.helper.X_LINK)
        url = self.helper.get_current_url().lower()
        self.assertTrue("x.com" in url or "twitter.com" in url)


# ===== 3b. SHOP PAGE =====
class TestShopPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = make_driver()
        cls.helper = Helper(cls.driver)
        # Open x.ai, click Shop, switch to new tab
        cls.helper.open()
        cls.main_handle = cls.driver.current_window_handle
        original_handles = set(cls.driver.window_handles)
        cls.helper.click(cls.helper.SHOP)
        WebDriverWait(cls.driver, 10).until(
            lambda d: len(d.window_handles) > len(original_handles)
        )
        new_handle = set(cls.driver.window_handles) - original_handles
        cls.driver.switch_to.window(new_handle.pop())
        # Wait for Shop to load
        WebDriverWait(cls.driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        cls.addClassCleanup(cls.driver.quit)

    def setUp(self):
        """Return to shop main page before each test"""
        self.driver.get("https://shop.x.com")
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    # ===== BASIC CHECKS =====
    def test_TC_P_069_shop_url(self):
        """URL contains shop.x.com"""
        self.assertIn("shop.x.com", self.driver.current_url.lower())

    def test_TC_P_070_shop_title_not_empty(self):
        """Page title is not empty"""
        self.assertTrue(len(self.driver.title) > 0)

    def test_TC_P_071_shop_logo_visible(self):
        """Shop logo is displayed"""
        logo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.helper.SHOP_LOGO)
        )
        self.assertTrue(logo.is_displayed())

    def test_TC_P_072_shop_collections_visible(self):
        """Collections are visible (X Collection / xAI Collection)"""
        section = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.helper.SHOP_COLLECTION)
        )
        self.assertTrue(section.is_displayed())

    def test_TC_P_073_shop_products_visible(self):
        """Products are visible on page"""
        products = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.helper.SHOP_PRODUCT_CARD)
        )
        self.assertTrue(products.is_displayed())

    def test_TC_P_074_shop_at_least_one_product_card(self):
        """At least one product card is on the page"""
        product_list = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.helper.SHOP_PRODUCT_LIST)
        )
        self.assertTrue(product_list.is_displayed())

    # ===== SCROLL =====
    def test_TC_P_075_shop_scroll_down(self):
        """Page scrolls down and shows more products"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(*self.helper.SHOP_PRODUCT_CARD)) > 0
        )
        cards = self.driver.find_elements(*self.helper.SHOP_PRODUCT_CARD)
        self.assertGreater(len(cards), 0)

    # ===== ADD TO CART =====
    def test_TC_P_076_shop_open_first_product(self):
        """Click on first product opens product detail page"""
        first_product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.helper.SHOP_FIRST_PRODUCT)
        )
        first_product.click()
        WebDriverWait(self.driver, 10).until(
            lambda d: "/products/" in d.current_url
        )
        self.assertIn("/products/", self.driver.current_url)

    def test_TC_P_077_shop_add_to_cart(self):
        """Add product to cart and proceed to checkout"""

        # 1. Click first product
        product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.helper.SHOP_FIRST_PRODUCT)
        )
        product.click()

        # 2. Wait for and click Add To Cart
        add_btn = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.helper.SHOP_ADD_TO_CART)
        )
        self.assertTrue(add_btn.is_displayed())
        add_btn.click()

        # 3. Wait for redirect to /cart (same tab)
        WebDriverWait(self.driver, 10).until(
            lambda d: "/cart" in d.current_url
        )
        self.assertIn("/cart", self.driver.current_url)

        # 4. Verify product is in cart
        product_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.helper.SHOP_CART_BODY)
        )
        self.assertTrue(product_name.is_displayed())

        # 5. Verify quantity = 1
        qty = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.helper.SHOP_QTY)
        )
        self.assertIsNotNone(qty)

        # 6. Click Checkout (same tab)
        checkout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.helper.SHOP_CHECKOUT_BTN)
        )
        checkout_btn.click()

        # 7. Verify redirect to checkout page in same tab
        WebDriverWait(self.driver, 15).until(
            lambda d: "checkout" in d.current_url or "checkouts" in d.current_url
        )
        self.assertTrue(
            "checkout" in self.driver.current_url or
            "checkouts" in self.driver.current_url
        )

        # 8. Verify we are on the Information page
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.helper.SHOP_CHECKOUT_H1)
        )

        # 9. Verify breadcrumb
        breadcrumb = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.helper.SHOP_BREADCRUMB)
        )
        self.assertIsNotNone(breadcrumb)

        # 10. Verify form — Email field and Shipping address
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.helper.SHOP_EMAIL_FIELD)
        )
        self.assertTrue(email_field.is_displayed())

        shipping_header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.helper.SHOP_SHIPPING_HEADER)
        )
        self.assertTrue(shipping_header.is_displayed())


# ===== 4. SCROLL & SECTIONS =====
class TestScrollAndSections(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = make_driver()
        cls.helper = Helper(cls.driver)
        cls.addClassCleanup(cls.driver.quit)

    def setUp(self):
        self.helper.open()

    def test_TC_P_078_scroll_shows_understand_universe(self):
        """Canvas animation (Understand The Universe) is present on page"""
        self.helper.scroll_by(600)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.helper.UNDERSTAND_UNIVERSE)
        )

    def test_TC_P_079_scroll_shows_section_grok(self):
        self.helper.scroll_to_element(self.helper.SECTION_GROK)
        self.assertTrue(self.helper.is_visible(self.helper.SECTION_GROK))

    def test_TC_P_080_scroll_shows_section_api(self):
        self.helper.scroll_to_element(self.helper.SECTION_API)
        self.assertTrue(self.helper.is_visible(self.helper.SECTION_API))

    def test_TC_P_081_scroll_shows_latest_news(self):
        self.helper.scroll_to_element(self.helper.LATEST_NEWS)
        self.assertTrue(self.helper.is_visible(self.helper.LATEST_NEWS))


# ===== 5. FOOTER =====
class TestFooter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = make_driver()
        cls.helper = Helper(cls.driver)
        cls.addClassCleanup(cls.driver.quit)

    def setUp(self):
        # Scroll in each test — more reliable than once in setUpClass
        self.helper.open()
        self.helper.scroll_to_bottom()

    def test_TC_P_082_footer_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER))

    def test_TC_P_083_footer_try_grok_on_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_TRY_GROK_ON))

    def test_TC_P_084_footer_web_link_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_WEB))

    def test_TC_P_085_footer_ios_link_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_IOS))

    def test_TC_P_086_footer_android_link_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_ANDROID))

    def test_TC_P_087_footer_section_products_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_PRODUCTS))

    def test_TC_P_088_footer_section_api_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_API))

    def test_TC_P_089_footer_api_pricing_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_API_PRICING))

    def test_TC_P_090_footer_api_docs_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_API_DOCS))

    def test_TC_P_091_footer_section_company_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_COMPANY))

    def test_TC_P_092_footer_contact_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_CONTACT))

    def test_TC_P_093_footer_section_resources_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_RESOURCES))

    def test_TC_P_094_footer_privacy_policy_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_PRIVACY_POLICY))

    def test_TC_P_095_footer_legal_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_LEGAL))

    def test_TC_P_096_footer_status_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_STATUS))

    def test_TC_P_097_footer_privacy_policy_has_href(self):
        self.assertTrue(self.helper.get_href(self.helper.FOOTER_PRIVACY_POLICY))

    def test_TC_P_098_footer_legal_has_href(self):
        self.assertTrue(self.helper.get_href(self.helper.FOOTER_LEGAL))


# ===== 6. CHATBOT =====
class TestChat(unittest.TestCase):

    def setUp(self):
        # New browser per test — clean session, message limit does not accumulate
        self.driver = make_driver()
        self.helper = Helper(self.driver)
        # addCleanup ensures quit() even if test fails with exception
        self.addCleanup(self.driver.quit)
        self.helper.open()
        # Check message limit — skip test if reached
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached — skipping chat test")

    def test_TC_P_099_chat_input_visible(self):
        self.assertTrue(self.helper.is_visible(self.helper.CHAT_INPUT))

    def test_TC_P_100_chat_input_clickable(self):
        self.assertTrue(self.helper.is_clickable(self.helper.CHAT_INPUT))

    def test_TC_P_101_chat_send_button_visible(self):
        """Send button is visible after typing text"""
        self.helper.type_message("Hello")
        self.assertTrue(self.helper.is_visible(self.helper.CHAT_SEND_BTN))

    def test_TC_P_102_chat_send_button_clickable(self):
        """Send button is clickable after typing text"""
        self.helper.type_message("Hello")
        self.assertTrue(self.helper.is_clickable(self.helper.CHAT_SEND_BTN))

    def test_TC_P_103_chat_input_accepts_text(self):
        self.helper.type_message("Hello")
        self.assertEqual(self.helper.get_chat_input_value(), "Hello")

    def test_TC_P_104_chat_send_by_button(self):
        self.helper.type_message("Hi")
        self.helper.send_message_by_button()
        self.assertEqual(self.helper.get_chat_input_value(), "")

    def test_TC_P_105_chat_send_by_enter(self):
        self.helper.send_message_by_enter("Hello")
        self.assertEqual(self.helper.get_chat_input_value(), "")

    def test_TC_P_106_chat_response_appears(self):
        self.helper.send_message_by_enter("Hello")
        response = self.helper.wait_for_response()
        self.assertIsNotNone(response)
        self.assertTrue(response.is_displayed())

    def test_TC_P_107_chat_response_not_empty(self):
        self.helper.send_message_by_enter("Hello")
        response = self.helper.wait_for_response()
        self.assertTrue(len(response.text) > 0)


if __name__ == "__main__":
    unittest.main()