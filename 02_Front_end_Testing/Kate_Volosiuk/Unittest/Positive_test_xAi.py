import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import Helper
import allure
import HtmlTestRunner

SHOP_URL     = "https://shop.x.com"
TIMEOUT      = 5
LONG_TIMEOUT = 10


class PositiveTests(unittest.TestCase):

    def setUp(self):
        self.driver = Helper.make_driver(self.browser)
        self.helper = Helper(self.driver)
        self.addCleanup(self._quit_driver)
        self.helper.open()

    def _quit_driver(self):
        try:
            self.driver.quit()
        except Exception:
            pass

    # ===== PAGE LOAD =====

    def test_TC_P_026_page_open(self):
        """Page x.ai opens successfully"""
        self.assertIn("x.ai", self.helper.get_current_url())

    def test_TC_P_027_page_title_not_empty(self):
        """Page title is not empty"""
        self.assertTrue(len(self.driver.title) > 0)

    def test_TC_P_028_page_title_contains_xai(self):
        """Page title contains xAI"""
        self.assertTrue("xai" in self.driver.title.lower())

    def test_TC_P_029_hero_heading_visible(self):
        """Hero heading AI for all humanity is displayed"""
        self.assertTrue(self.helper.is_visible(self.helper.HERO_HEADING))

    def test_TC_P_030_page_has_no_crash(self):
        """Page returns no 404/500 errors"""
        self.assertTrue(self.helper.page_has_no_crash())

    # ===== TOP MENU =====

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

    # ===== NAVIGATION — SAME TAB =====

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

    # ===== NAVIGATION — NEW TAB =====

    def _click_and_switch_to_new_tab(self, locator):
        original_handles = set(self.driver.window_handles)
        self.helper.click(locator)
        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            lambda d: len(d.window_handles) > len(original_handles)
        )
        new_handle = set(self.driver.window_handles) - original_handles
        self.driver.switch_to.window(new_handle.pop())

    def test_TC_P_063_click_shop_opens_new_tab(self):
        """Click on Shop opens a new tab"""
        original_handles = set(self.driver.window_handles)
        self.helper.click(self.helper.SHOP)
        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            lambda d: len(d.window_handles) > len(original_handles)
        )
        self.assertGreater(len(self.driver.window_handles), len(original_handles))

    def test_TC_P_064_click_shop_navigates(self):
        """Click on Shop navigates to shop page"""
        self._click_and_switch_to_new_tab(self.helper.SHOP)
        self.assertIn("shop", self.helper.get_current_url().lower())

    def test_TC_P_065_click_spacex_opens_new_tab(self):
        """Click on SpaceX opens a new tab"""
        original_handles = set(self.driver.window_handles)
        self.helper.click(self.helper.SPACEX)
        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            lambda d: len(d.window_handles) > len(original_handles)
        )
        self.assertGreater(len(self.driver.window_handles), len(original_handles))

    def test_TC_P_066_click_spacex_navigates(self):
        """Click on SpaceX navigates to spacex page"""
        self._click_and_switch_to_new_tab(self.helper.SPACEX)
        self.assertIn("spacex", self.helper.get_current_url().lower())

    def test_TC_P_067_click_x_opens_new_tab(self):
        """Click on X opens a new tab"""
        original_handles = set(self.driver.window_handles)
        self.helper.click(self.helper.X_LINK)
        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            lambda d: len(d.window_handles) > len(original_handles)
        )
        self.assertGreater(len(self.driver.window_handles), len(original_handles))

    def test_TC_P_068_click_x_navigates(self):
        """Click on X navigates to x.com or twitter.com"""
        self._click_and_switch_to_new_tab(self.helper.X_LINK)
        url = self.helper.get_current_url().lower()
        self.assertTrue("x.com" in url or "twitter.com" in url)

    # ===== SHOP =====

    def _switch_to_shop(self):
        if len(self.driver.window_handles) == 1:
            if self.browser == "chrome":
                self.helper.open()
                self.helper.click(self.helper.SHOP)
            else:
                self.driver.execute_script(f"window.open('{SHOP_URL}');")
            WebDriverWait(self.driver, LONG_TIMEOUT).until(
                lambda d: len(d.window_handles) > 1
            )
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(SHOP_URL)
        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def test_TC_P_069_shop_url(self):
        """URL contains shop.x.com"""
        self._switch_to_shop()
        self.assertIn("shop.x.com", self.driver.current_url.lower())

    def test_TC_P_070_shop_title_not_empty(self):
        """Page title is not empty"""
        self._switch_to_shop()
        self.assertTrue(len(self.driver.title) > 0)

    def test_TC_P_071_shop_logo_visible(self):
        """Shop logo is displayed"""
        self._switch_to_shop()
        logo = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.visibility_of_element_located(self.helper.SHOP_LOGO)
        )
        self.assertTrue(logo.is_displayed())

    def test_TC_P_072_shop_collections_visible(self):
        """Collections are visible (X Collection / xAI Collection)"""
        self._switch_to_shop()
        section = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.visibility_of_element_located(self.helper.SHOP_COLLECTION)
        )
        self.assertTrue(section.is_displayed())

    def test_TC_P_073_shop_products_visible(self):
        """Products are visible on page"""
        self._switch_to_shop()
        products = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.visibility_of_element_located(self.helper.SHOP_PRODUCT_CARD)
        )
        self.assertTrue(products.is_displayed())

    def test_TC_P_074_shop_at_least_one_product_card(self):
        """At least one product card is on the page"""
        self._switch_to_shop()
        product_list = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.presence_of_element_located(self.helper.SHOP_PRODUCT_LIST)
        )
        self.assertTrue(product_list.is_displayed())

    def test_TC_P_075_shop_scroll_down(self):
        """Page scrolls down and shows more products"""
        self._switch_to_shop()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            lambda d: len(d.find_elements(*self.helper.SHOP_PRODUCT_CARD)) > 0
        )
        self.assertGreater(
            len(self.driver.find_elements(*self.helper.SHOP_PRODUCT_CARD)), 0
        )

    def test_TC_P_076_shop_open_first_product(self):
        """Click on first product opens product detail page"""
        self._switch_to_shop()
        first = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.element_to_be_clickable(self.helper.SHOP_FIRST_PRODUCT)
        )
        first.click()
        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            lambda d: "/products/" in d.current_url
        )
        self.assertIn("/products/", self.driver.current_url)

    def test_TC_P_077_shop_add_to_cart(self):
        """Add product to cart and proceed to checkout"""
        self._switch_to_shop()

        first = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.element_to_be_clickable(self.helper.SHOP_FIRST_PRODUCT)
        )
        first.click()

        add_btn = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.element_to_be_clickable(self.helper.SHOP_ADD_TO_CART)
        )
        self.assertTrue(add_btn.is_displayed())
        add_btn.click()

        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            lambda d: "/cart" in d.current_url
        )
        self.assertIn("/cart", self.driver.current_url)

        product_name = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.visibility_of_element_located(self.helper.SHOP_CART_BODY)
        )
        self.assertTrue(product_name.is_displayed())

        qty = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.visibility_of_element_located(self.helper.SHOP_QTY)
        )
        self.assertIsNotNone(qty)

        checkout_btn = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.element_to_be_clickable(self.helper.SHOP_CHECKOUT_BTN)
        )
        checkout_btn.click()

        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            lambda d: "checkout" in d.current_url or "checkouts" in d.current_url
        )
        self.assertTrue(
            "checkout" in self.driver.current_url or
            "checkouts" in self.driver.current_url
        )

        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.visibility_of_element_located(self.helper.SHOP_CHECKOUT_H1)
        )

        breadcrumb = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.visibility_of_element_located(self.helper.SHOP_BREADCRUMB)
        )
        self.assertIsNotNone(breadcrumb)

        email_field = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.visibility_of_element_located(self.helper.SHOP_EMAIL_FIELD)
        )
        self.assertTrue(email_field.is_displayed())

        shipping_header = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.visibility_of_element_located(self.helper.SHOP_SHIPPING_HEADER)
        )
        self.assertTrue(shipping_header.is_displayed())

    # ===== SCROLL & SECTIONS =====

    def test_TC_P_078_scroll_shows_understand_universe(self):
        """Canvas animation (Understand The Universe) is present on page"""
        self.helper.scroll_by(600)
        WebDriverWait(self.driver, LONG_TIMEOUT).until(
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

    # ===== FOOTER =====

    def test_TC_P_082_footer_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER))

    def test_TC_P_083_footer_try_grok_on_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_TRY_GROK_ON))

    def test_TC_P_084_footer_web_link_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_WEB))

    def test_TC_P_085_footer_ios_link_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_IOS))

    def test_TC_P_086_footer_android_link_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_ANDROID))

    def test_TC_P_087_footer_section_products_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_PRODUCTS))

    def test_TC_P_088_footer_section_api_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_API))

    def test_TC_P_089_footer_api_pricing_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_API_PRICING))

    def test_TC_P_090_footer_api_docs_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_API_DOCS))

    def test_TC_P_091_footer_section_company_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_COMPANY))

    def test_TC_P_092_footer_contact_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_CONTACT))

    def test_TC_P_093_footer_section_resources_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_RESOURCES))

    def test_TC_P_094_footer_privacy_policy_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_PRIVACY_POLICY))

    def test_TC_P_095_footer_legal_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_LEGAL))

    def test_TC_P_096_footer_status_visible(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.is_visible(self.helper.FOOTER_STATUS))

    def test_TC_P_097_footer_privacy_policy_has_href(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.get_href(self.helper.FOOTER_PRIVACY_POLICY))

    def test_TC_P_098_footer_legal_has_href(self):
        self.helper.scroll_to_bottom()
        self.assertTrue(self.helper.get_href(self.helper.FOOTER_LEGAL))

    # ===== CHATBOT =====

    def test_TC_P_099_chat_input_visible(self):
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        self.assertTrue(self.helper.is_visible(self.helper.CHAT_INPUT))

    def test_TC_P_100_chat_input_clickable(self):
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        self.assertTrue(self.helper.is_clickable(self.helper.CHAT_INPUT))

    def test_TC_P_101_chat_send_button_visible(self):
        """Send button is visible after typing text"""
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        self.helper.type_message("Hello")
        self.assertTrue(self.helper.is_visible(self.helper.CHAT_SEND_BTN))

    def test_TC_P_102_chat_send_button_clickable(self):
        """Send button is clickable after typing text"""
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        self.helper.type_message("Hello")
        self.assertTrue(self.helper.is_clickable(self.helper.CHAT_SEND_BTN))

    def test_TC_P_103_chat_input_accepts_text(self):
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        self.helper.type_message("Hello")
        self.assertEqual(self.helper.get_chat_input_value(), "Hello")

    def test_TC_P_104_chat_send_by_button(self):
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        self.helper.type_message("Hi")
        self.helper.send_message_by_button()
        self.assertEqual(self.helper.get_chat_input_value(), "")

    def test_TC_P_105_chat_send_by_enter(self):
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        self.helper.send_message_by_enter("Hello")
        self.assertEqual(self.helper.get_chat_input_value(), "")

    def test_TC_P_106_chat_response_appears(self):
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        self.helper.send_message_by_enter("Hello")
        response = self.helper.wait_for_response()
        self.assertIsNotNone(response)
        self.assertTrue(response.is_displayed())

    def test_TC_P_107_chat_response_not_empty(self):
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        self.helper.send_message_by_enter("Hello")
        response = self.helper.wait_for_response()
        self.assertTrue(len(response.text) > 0)


# ===== GENERATE 2 BROWSER CLASSES =====
class PositiveTestsChrome(PositiveTests):
    browser = "chrome"

class PositiveTestsEdge(PositiveTests):
    browser = "edge"

del PositiveTests


if __name__ == "__main__":
    unittest.main(allure)

"""if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))"""