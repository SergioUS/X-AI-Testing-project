import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from helper import Helper
import allure
import HtmlTestRunner

SHOP_URL     = "https://shop.x.com"
TIMEOUT      = 5
LONG_TIMEOUT = 10


class NegativeTests(unittest.TestCase):

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
    # ===== INVALID URL =====

    def test_TC_N_026_nonexistent_path_does_not_show_homepage(self):
        """Non-existent x.ai path does not show homepage content"""
        self.driver.get("https://x.ai/page-does-not-exist-99999")
        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        if "does-not-exist" in self.driver.current_url:
            hero = self.driver.find_elements(*self.helper.HERO_HEADING)
            self.assertEqual(len(hero), 0)

    # ===== CHATBOT =====

    def test_TC_N_027_enter_on_empty_input_does_not_navigate(self):
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        input_field = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(self.helper.CHAT_INPUT)
        )
        input_field.clear()
        input_field.send_keys(Keys.RETURN)
        self.assertIn("x.ai", self.helper.get_current_url())

    def test_TC_N_028_very_long_input_does_not_crash_ui(self):
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        self.helper.type_message("A" * 5000)
        self.assertTrue(self.helper.is_visible(self.helper.CHAT_INPUT))

    def test_TC_N_029_shift_enter_only_does_not_submit(self):
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        input_field = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(self.helper.CHAT_INPUT)
        )
        input_field.clear()
        for _ in range(5):
            input_field.send_keys(Keys.SHIFT + Keys.ENTER)
        self.assertIn("x.ai", self.helper.get_current_url())

    def test_TC_N_030_special_characters_do_not_break_input(self):
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        self.helper.type_message('"\'\\  /|<>&;--')
        self.assertTrue(self.helper.is_visible(self.helper.CHAT_INPUT))
        self.driver.find_element(*self.helper.CHAT_INPUT).clear()
        self.assertEqual(self.helper.get_chat_input_value(), "")

    def test_TC_N_031_whitespace_only_message_not_accepted(self):
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        input_field = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(self.helper.CHAT_INPUT)
        )
        input_field.clear()
        input_field.send_keys(" ")
        input_field.send_keys(Keys.RETURN)
        try:
            WebDriverWait(self.driver, LONG_TIMEOUT).until(
                EC.visibility_of_element_located(self.helper.CHAT_RESPONSE)
            )
            response = self.driver.find_element(*self.helper.CHAT_RESPONSE)
            self.fail(
                "BUG CONFIRMED: Whitespace-only message was accepted and "
                f"chatbot responded. Response: '{response.text[:200]}'"
            )
        except TimeoutException:
            pass
        self.assertIn("x.ai", self.helper.get_current_url())

    def test_TC_N_032_numeric_only_input_send_button_active(self):
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        self.helper.type_message("12345")
        disabled = self.helper.is_button_disabled(self.helper.CHAT_SEND_BTN)
        visible  = self.helper.is_visible(self.helper.CHAT_SEND_BTN)
        self.assertTrue(visible and not disabled)

    def test_TC_N_033_page_refresh_during_response_does_not_crash(self):
        if self.helper.is_visible(self.helper.ERROR_MESSAGE):
            self.skipTest("Message limit reached")
        input_field = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(self.helper.CHAT_INPUT)
        )
        input_field.send_keys("tell me story about Earth with 1000 worlds")
        input_field.send_keys(Keys.RETURN)
        self.driver.refresh()
        response = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.visibility_of_element_located(self.helper.CHAT_RESPONSE)
        )
        self.assertIsNotNone(response)
        current = self.helper.get_current_url()
        self.assertTrue("x.ai" in current or "grok.com" in current)

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

    def _dismiss_dialog_if_present(self):
        from selenium.common.exceptions import StaleElementReferenceException as Stale
        try:
            ok_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.helper.SHOP_BTN)
            )
            ok_btn.click()
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(self.helper.SHOP_BTN)
            )
        except (TimeoutException, Stale):
            pass

    def _set_qty_and_update(self, value):
        from selenium.webdriver.common.action_chains import ActionChains
        WebDriverWait(self.driver, TIMEOUT).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        self._dismiss_dialog_if_present()
        qty = WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable(self.helper.SHOP_QTY)
        )
        ActionChains(self.driver).double_click(qty).send_keys(value).perform()
        self._dismiss_dialog_if_present()
        update_btn = WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable(self.helper.SHOP_UPDATE_BTN)
        )
        update_btn.click()
        WebDriverWait(self.driver, TIMEOUT).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def test_TC_N_034_nonexistent_product_url_returns_404(self):
        self._switch_to_shop()
        self.driver.get(f"{SHOP_URL}/products/this-product-does-not-exist-xyz")
        WebDriverWait(self.driver, TIMEOUT).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        page = self.driver.page_source.lower()
        self.assertTrue("404" in page or "not found" in page or "page not found" in page)

    def test_TC_N_035_empty_cart_has_no_items(self):
        self._switch_to_shop()
        self.driver.get(f"{SHOP_URL}/cart")
        WebDriverWait(self.driver, TIMEOUT).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        self.assertEqual(len(self.driver.find_elements(*self.helper.SHOP_QTY)), 0)

    def test_TC_N_036_checkout_without_cart_does_not_show_payment(self):
        self._switch_to_shop()
        self.driver.get(f"{SHOP_URL}/checkout")
        WebDriverWait(self.driver, TIMEOUT).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        url  = self.driver.current_url.lower()
        page = self.driver.page_source.lower()
        self.assertTrue("cart" in url or "cart" in page or "empty" in page)

    def test_TC_N_037_cart_quantity_zero_shows_empty_cart(self):
        self._switch_to_shop()
        first = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.element_to_be_clickable(self.helper.SHOP_FIRST_PRODUCT)
        )
        first.click()
        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.element_to_be_clickable(self.helper.SHOP_ADD_TO_CART)
        ).click()
        WebDriverWait(self.driver, LONG_TIMEOUT).until(lambda d: "/cart" in d.current_url)
        self._dismiss_dialog_if_present()
        self._set_qty_and_update("0")
        self._dismiss_dialog_if_present()
        page = self.driver.page_source.lower()
        self.assertTrue(
            "your cart is empty" in page or "cart is empty" in page or
            len(self.driver.find_elements(*self.helper.SHOP_QTY)) == 0
        )

    def test_TC_N_038_cart_quantity_100_causes_422_bug(self):
        self._switch_to_shop()
        first = WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.element_to_be_clickable(self.helper.SHOP_FIRST_PRODUCT)
        )
        first.click()
        WebDriverWait(self.driver, LONG_TIMEOUT).until(
            EC.element_to_be_clickable(self.helper.SHOP_ADD_TO_CART)
        ).click()
        WebDriverWait(self.driver, LONG_TIMEOUT).until(lambda d: "/cart" in d.current_url)
        self._dismiss_dialog_if_present()
        self._set_qty_and_update("100")
        self._dismiss_dialog_if_present()
        page = self.driver.page_source.lower()
        if "422" in page or "isn't working" in page or "http error 422" in page:
            self.fail("BUG CONFIRMED: qty=100 causes HTTP ERROR 422 — page crashed")


# ===== GENERATE 2 BROWSER CLASSES =====
class NegativeTestsChrome(NegativeTests):
    browser = "chrome"

class NegativeTestsEdge(NegativeTests):
    browser = "edge"

del NegativeTests


if __name__ == "__main__":
    unittest.main(allure)
"""if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))"""