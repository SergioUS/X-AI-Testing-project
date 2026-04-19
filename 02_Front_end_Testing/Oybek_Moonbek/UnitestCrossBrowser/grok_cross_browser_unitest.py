
import unittest
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilis


class ChromeDriverGrok(unittest.TestCase):

    TEST_TITLES = {
        "test_001_P": "Verify xAI homepage opens and loads correctly",
        "test_002_P": "Verify xAI homepage top navigation and Area text field by hovering on links and button",
        "test_003_P": "Hover  and click on TRY GROK button and verify URL, Title, and Elements on Grok page",
        "test_004_P": "Click on Imagine link and enter text in prompt input field",
        "test_005_P": "Verify by hover at least three tooltip texts appear on canvas",
        "test_001_N": "Invalid URL handling",
        "test_002_N": "Grok link behaviour",
        "test_003_N": "Grok link behavior by focusing and pressing Enter/Return",
        "test_004_N": "Verify AI processes a Latin-letter foreign phrase",
        "test_005_N": "Verify animation response to user interaction after highlighting.",

    }

    def setUp(self):
        test_name = self._testMethodName
        title = self.TEST_TITLES.get(test_name, "Unknown test")

        print("\n" + "=" * 80)
        print(f"START TEST: {test_name} | {title}")
        print("=" * 80)

        # options = Options()
        # options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = utilis.create_driver("chrome")
        # self.driver.maximize_window()

    def tearDown(self):
        print("\n" + "=" * 80)
        print(f"END TEST: {self._testMethodName}")
        print("=" * 80)

        if hasattr(self, "driver"):
            self.driver.quit()
            print("Browser closed successfully")


    # ========= Positive Tests ==========

    # Verify xAI homepage opens and loads correctly
    def test_001_P(self):
        driver = self.driver
        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open homepage: {e}")
        # Wait for page load
        try:
            utilis.wait_body(driver)
            print("Page body loaded successfully")
        except Exception as e:
            raise Exception(f"Failed to load page body: {e}")
        # Verify Title
        try:
            utilis.wait_title_contains(driver, "xAI")
            print("Title verified successfully:", driver.title)
        except Exception as e:
            raise Exception(f"Title verification failed: {e}")
        # Verify homepage
        try:
            utilis.wait_url_contains(driver, "x.ai")
            # self.assertIn("x.ai", driver.current_url)
            print("URL verified successfully", driver.current_url)
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")

    # Verify xAI homepage top navigation and Area text field by hovering on links and button
    def test_002_P(self):
        driver = self.driver

        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            self.fail(f"Failed to open homepage: {e}")

        # Verify top navigation bar, btn links.
        try:
            utilis.wait_element_css(driver, ".flex.items-center.justify-between")
            print("Top navigation bar verified successfully")

            utilis.wait_element_xpath(driver, "//nav[.//a[@aria-label='xAI Homepage']]")
            print("Homepage button link verified successfully")

            utilis.wait_link_text(driver, "Grok")
            print("Grok button link verified successfully")

            utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            print("Try Grok button link verified successfully")
        except Exception as e:
            self.fail(f"Top navigation bar verification failed: {e}")

        # User hover on Navigation bar link and TRY GROK button
        try:
            home_link = utilis.wait_element_css(driver, 'a[href="/"]')
            ActionChains(driver).move_to_element(home_link).perform()
            print("Home link hover successfully")

            grok_link = utilis.wait_element_css(driver, 'a[href="/grok"]')
            ActionChains(driver).move_to_element(grok_link).perform()
            print("Grok link hover successfully")

            api_link = utilis.wait_element_css(driver, 'a[href="/api"]')
            ActionChains(driver).move_to_element(api_link).perform()
            print("API link hover successfully")

            company_link = utilis.wait_element_css(driver, 'a[href="/company"]')
            ActionChains(driver).move_to_element(company_link).perform()
            print("Company link hover successfully")

            colossus_link = utilis.wait_element_css(driver, 'a[href="/colossus"]')
            ActionChains(driver).move_to_element(colossus_link).perform()
            print("Colossus link hover successfully")

            careers_link = utilis.wait_element_css(driver, 'a[href="/careers"]')
            ActionChains(driver).move_to_element(careers_link).perform()
            print("Careers link hover successfully")

            news_link = utilis.wait_element_css(driver, 'a[href="/news"]')
            ActionChains(driver).move_to_element(news_link).perform()
            print("News link hover successfully")

            shop_link = utilis.wait_element_css(driver, 'a[href="https://shop.x.ai"]')
            ActionChains(driver).move_to_element(shop_link).perform()
            print("Shop link hover successfully")

            space_link = utilis.wait_element_css(driver, 'a[href="https://spacex.com/"]')
            ActionChains(driver).move_to_element(space_link).perform()
            print("SpaceX link hover successfully")

            x_link = utilis.wait_element_css(driver, 'a[href="https://x.com"]')
            ActionChains(driver).move_to_element(x_link).perform()
            print("X link hover successfully")

            try_grok_link = utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            ActionChains(driver).move_to_element(try_grok_link).perform()
            print("Try Grok link hover successfully")
        except Exception as e:
            self.fail(f"Homepage verification failed: {e}")

        # Verify Text Area field
        try:
            utilis.wait_element_name(driver, "query")
            print("Text Area field verified successfully")
        except Exception as e:
            self.fail(f"Text Area field verification failed: {e}")

    # Hover  and click on TRY GROK button and verify URL, Title, and Elements on Grok page
    def test_003_P(self):
        driver = self.driver
        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open homepage: {e}")
        # Hover on Try Grok btn and click
        try:
            try_grok_link = utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            ActionChains(driver).move_to_element(try_grok_link).perform()
            time.sleep(1)
            try_grok_link.click()
            print("Try Grok button hover and clicked successfully")
        except Exception as e:
            raise Exception(f"Hover on Try Grok failed: {e}")
        # Verify URL
        try:
            utilis.wait_url_contains(driver, "grok.com")
            # self.assertIn("https://grok.com/?referrer=web", driver.current_url)
            print("URL verified successfully:", driver.current_url)
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")
        time.sleep(5)
        # Verify Title
        try:
            utilis.wait_title_contains(driver, "Grok")
            print("Title verified successfully:", driver.title)
        except Exception as e:
            raise Exception(f"Title verification failed: {e}")
        # Verify Elements on Grok page
        try:
            imagine_link = utilis.wait_element_css(driver, 'a[href="/imagine"]')
            self.assertTrue(imagine_link.is_displayed())
            print("Imagine Link on Grok page verified successfully:", imagine_link.text)
            text_area = utilis.wait_element_css(driver, 'textarea[aria-label="Ask Grok anything"]')
            self.assertTrue(text_area.is_displayed())
            print("Text Area on Grok page verified successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(5)

    # Click on Imagine link and enter text in prompt input field
    def test_004_P(self):
        driver = self.driver
        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open homepage: {e}")
        time.sleep(3)
        # Click on Try Grok btn
        try:
            try_grok_link = utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            time.sleep(1)
            try_grok_link.click()
            print("Try Grok button clicked successfully")
        except Exception as e:
            raise Exception(f"Click on Try Grok failed: {e}")
        time.sleep(3)

        # Click on Imagine link and click back arrow
        try:
            imagine_link = utilis.wait_element_css(driver, 'a[href="/imagine"]')
            imagine_link.click()
            print("Imagine Link on Grok page clicked successfully:")
        except Exception as e:
            raise Exception(f"Click on Imagine link failed: {e}")

        # Verify Imagine URL
        try:
            utilis.wait_url_contains(driver, "https://grok.com/imagine")
            self.assertIn("https://grok.com/imagine", driver.current_url)
            print("URL verified successfully:,", driver.current_url)
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")
        time.sleep(3)
        # Click back arrow
        try:
            time.sleep(2)
            driver.back()
            print("Back button clicked successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(3)
        # Type the Question and click Enter
        try:
            text_area = utilis.wait_element_css(driver, 'textarea[aria-label="Ask Grok anything"]')
            text_area.click()
            text_area.clear()
            text_area.send_keys("What is current Time, Date, and Year NOW?")
            time.sleep(5)
            text_area.send_keys(Keys.ENTER)
            print("Question Entered and submitted successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(5)

    # Verify by hover at least three tooltip texts appear on canvas
    def test_005_P(self):
        driver = self.driver
        expected_texts = {
            "WHAT FUELS THE PULSE OF CREATION?",
            "DOES EXISTENCE HOLD INHERENT MEANING?",
            "DO QUANTUM REALMS DICTATE FATE?",
            "ARE WE ALONE IN ETERNITY’S EXPANSE?",
            "HOW DOES CHAOS BIRTH COSMIC ORDER?",
            "WHAT LIES BEYOND THE OBSERVABLE VOID?",
            "CAN WE TRAVERSE TIME'S ARROW?",
            "WHAT HIDES IN THE UNIVERSE'S SHADOWS?",
            "IS THE UNIVERSE INFINITELY LAYERED?",
            "WHAT SPARKED THE UNIVERSE'S BIRTH?",
            "DO MULTIPLE REALITIES COEXIST?",
            "ARE WE ECHOES OF A GREATER DESIGN?",
            "CAN ENTROPY EVER BE REVERSED?",
            "HOW DO BLACK HOLES RESHAPE REALITY?",
            "HOW DOES CONSCIOUSNESS EMERGE FROM MATTER?",
            "CAN ONE THEORY ENCOMPASS ALL REALITY?",
            "DO OTHER MINDS INHABIT THE STARS?",
            "WHAT DESTINY AWAITS THE COSMOS?"
        }

        found_texts = set()
        minimum_required = 3
        try:
            # Open homepage
            driver.get("https://x.ai/")
            print("Page loaded successfully")
            time.sleep(4)
            # Scroll down
            utilis.scroll_page(driver, y=2000, timeout=5)
            print("Page scrolled successfully")

            # Verify canvas
            canvas = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'canvas[data-engine="three.js r172"]')
                )
            )
            self.assertTrue(canvas.is_displayed(), "Canvas is not visible")
            print("Canvas ready")
            # Start hovering tooltips on canvas
            for x in range(-220, 221, 40):
                for y in range(-220, 221, 40):
                    try:
                        ActionChains(driver).move_to_element_with_offset(canvas, x, y).perform()

                        tooltip_elements = driver.find_elements(
                            By.XPATH, '//div[contains(@class,"bg-background/80")]'
                        )
                        visible_tooltips = [el for el in tooltip_elements if el.is_displayed()]

                        if not visible_tooltips:
                            continue

                        current_text = visible_tooltips[0].text.strip()

                        if current_text in expected_texts and current_text not in found_texts:
                            found_texts.add(current_text)
                            print(f"Found text {len(found_texts)}: {current_text}")

                        if len(found_texts) >= minimum_required:
                            break

                    except StaleElementReferenceException:
                        continue

                if len(found_texts) >= minimum_required:
                    break
            print("\nFound texts:")
            for text in sorted(found_texts):
                print(text)

            missing_texts = expected_texts - found_texts

            self.assertGreaterEqual(
                len(found_texts),
                minimum_required,
                f"Too few texts found. Expected at least {minimum_required}, "
                f"but found {len(found_texts)}. Missing: {missing_texts}"
            )
        except Exception as e:
            raise Exception(f"Canvas hover verification failed: {e}")


 # ========= Negative Tests ==========

    # Check invalid URL handling
    def test_001_N(self):
        driver = self.driver

        # Open invalid URL
        try:
            driver.get("https://x.ai/https:/x.ai")
            print("Invalid URL opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open invalid URL: {e}")

        # Verify invalid page message
        try:
            page_not_found = driver.find_element(By.XPATH, "//h1[text()='Page not found']")
            assert page_not_found.is_displayed(), "Page not found message is not displayed"
            print("Invalid Page Message visible successful")
            driver.save_screenshot("page_not_found.png")
        except Exception as e:
            raise Exception(f"Invalid URL verification failed: {e}")

        # Verify BACK TO HOME button
        try:
            back_to_home = driver.find_element(By.XPATH, "//a[normalize-space()='Back to home']")
            assert back_to_home.is_displayed(), "BACK TO HOME button is not displayed"
            back_to_home.click()
            print("BACK TO HOME button visible successful and Clicked")
            driver.save_screenshot("back_to_home.png")
        except Exception as e:
            raise Exception(f"BACK TO HOME button verification failed: {e}")

        # Verify HOME PAGE URL
        try:
            self.assertIn("https://x.ai/", driver.current_url)
            print(f"URL Home Page verified successfully: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")

    # Check Grok link behaviour
    def test_002_N(self):
        driver = self.driver

        try:
            driver.get("https://x.ai")
            print(f"Valid URL opened successfully: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Failed to open URL: {e}")

        try:
            grok_link = driver.find_element(By.CSS_SELECTOR, "a[href='/grok']")
            current_url_before = driver.current_url

            # Hover over Grok link
            ActionChains(driver).move_to_element(grok_link).perform()
            time.sleep(2)

            # Right-click on Grok link
            ActionChains(driver).context_click(grok_link).perform()
            time.sleep(2)

            # Verify no navigation happened after right-click
            self.assertEqual(current_url_before, driver.current_url)

            # Close context menu
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(3)

            # Press unsupported keys
            ActionChains(driver).send_keys("a").send_keys("5").send_keys("@").send_keys(Keys.SPACE).perform()
            time.sleep(1)

            # Verify no navigation happened
            self.assertEqual(current_url_before, driver.current_url)
            print("Unsupported keys did not open the Grok page")

        except Exception as e:
            raise Exception(f"Failed Grok link negative test: {e}")

    # Check Grok link behavior by focusing and pressing Enter/Return
    def test_003_N(self):
        driver = self.driver

        try:
            driver.get("https://x.ai")
            print(f"Valid URL opened successfully: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Failed to open URL: {e}")

        try:
            grok_link = driver.find_element(By.CSS_SELECTOR, "a[href='/grok']")
            old_url = driver.current_url
            time.sleep(2)
        except Exception as e:
            raise Exception(f"Failed to find Grok link: {e}")

        try:
            # Focus Grok link
            driver.execute_script("arguments[0].focus();", grok_link)
            time.sleep(2)
        except Exception as e:
            raise Exception(f"Failed to find Grok link: {e}")

        try:
            # Press Enter
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            time.sleep(5)
        except Exception as e:
            raise Exception(f"Failed to find Grok link: {e}")

        try:
            # Wait for URL to change
            WebDriverWait(driver, 10).until(lambda d: d.current_url != old_url)
            new_url = driver.current_url

            print(f"Navigation successful. New URL: {new_url}")
            driver.save_screenshot("grok_link.png")
            print("New page screenshot saved successfully")

            # Verify navigation happened
            self.assertIn("/grok", new_url)
            self.assertNotEqual(old_url, new_url)
            print("Enter key opened the Grok page successfully")

        except Exception as e:
            raise Exception(f"Failed Grok link Enter key test: {e}")

    # Verify AI processes a Latin-letter foreign phrase

    def test_004_N(self):
        driver = self.driver
        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open homepage: {e}")
        time.sleep(3)
        # Click on Try Grok btn
        try:
            try_grok_link = utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            time.sleep(1)
            try_grok_link.click()
            print("Try Grok button clicked successfully")
        except Exception as e:
            raise Exception(f"Click on Try Grok failed: {e}")
        time.sleep(3)

        # Click on Imagine link and click back arrow
        try:
            imagine_link = utilis.wait_element_css(driver, 'a[href="/imagine"]')
            imagine_link.click()
            print("Imagine Link on Grok page clicked successfully:")
        except Exception as e:
            raise Exception(f"Click on Imagine link failed: {e}")

        # Verify Imagine URL
        try:
            utilis.wait_url_contains(driver, "https://grok.com/imagine")
            self.assertIn("https://grok.com/imagine", driver.current_url)
            print("URL verified successfully:,", driver.current_url)
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")
        time.sleep(3)
        # Click back arrow
        try:
            time.sleep(2)
            driver.back()
            print("Back button clicked successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(3)
        # Type the Question and click Enter
        try:
            text_area = utilis.wait_element_css(driver, 'textarea[aria-label="Ask Grok anything"]')
            text_area.click()
            text_area.clear()
            text_area.send_keys("nazovi kakoe ceicha chislo, vremya i god na angkiskom")
            time.sleep(5)
            text_area.send_keys(Keys.ENTER)
            print("Question Entered and submitted successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(5)
        # Verify AI processes a Latin-letter foreign phrase
        try:
            phrase = utilis.wait_element_css(driver, 'strong.font-semibold')
            print("Foreign phrase verified successfully:", phrase.text)
        except Exception as e:
            raise Exception(f"Failed text area test: {e}")


    # Verify animation response to user interaction after highlighting.
    def test_005_N(self):
        driver = self.driver
        expected_texts = {
            "WHAT FUELS THE PULSE OF CREATION?",
            "DOES EXISTENCE HOLD INHERENT MEANING?",
            "DO QUANTUM REALMS DICTATE FATE?",
            "ARE WE ALONE IN ETERNITY’S EXPANSE?",
            "HOW DOES CHAOS BIRTH COSMIC ORDER?",
            "WHAT LIES BEYOND THE OBSERVABLE VOID?",
            "CAN WE TRAVERSE TIME'S ARROW?",
            "WHAT HIDES IN THE UNIVERSE'S SHADOWS?",
            "IS THE UNIVERSE INFINITELY LAYERED?",
            "WHAT SPARKED THE UNIVERSE'S BIRTH?",
            "DO MULTIPLE REALITIES COEXIST?",
            "ARE WE ECHOES OF A GREATER DESIGN?",
            "CAN ENTROPY EVER BE REVERSED?",
            "HOW DO BLACK HOLES RESHAPE REALITY?",
            "HOW DOES CONSCIOUSNESS EMERGE FROM MATTER?",
            "CAN ONE THEORY ENCOMPASS ALL REALITY?",
            "DO OTHER MINDS INHABIT THE STARS?",
            "WHAT DESTINY AWAITS THE COSMOS?"
        }

        found_texts = set()
        minimum_required = 3

        try:
            driver.get("https://x.ai/")
            print("Page loaded successfully")
            time.sleep(4)

            utilis.scroll_page(driver, y=2000, timeout=5)
            print("Page scrolled successfully")

            canvas_locator = (By.CSS_SELECTOR, 'canvas[data-engine="three.js r172"]')
            canvas = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(canvas_locator)
            )
            self.assertTrue(canvas.is_displayed(), "Canvas is not visible")
            print("Canvas ready")

            # click on empty space inside canvas
            ActionChains(driver).move_to_element_with_offset(canvas, 5, 5).click().perform()
            time.sleep(0.5)

            # Command + A on macOS
            ActionChains(driver).key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
            time.sleep(1)

            for x in range(-220, 221, 40):
                for y in range(-220, 221, 40):
                    try:
                        canvas = WebDriverWait(driver, 5).until(
                            EC.visibility_of_element_located(canvas_locator)
                        )

                        ActionChains(driver).move_to_element_with_offset(canvas, x, y).perform()
                        time.sleep(0.2)

                        tooltip_elements = driver.find_elements(
                            By.XPATH, '//div[contains(@class,"bg-background/80")]'
                        )

                        visible_tooltips = [
                            el for el in tooltip_elements
                            if el.is_displayed() and el.text.strip()
                        ]

                        if not visible_tooltips:
                            continue

                        current_text = visible_tooltips[0].text.strip()

                        if current_text in expected_texts and current_text not in found_texts:
                            found_texts.add(current_text)
                            print(f"Found text {len(found_texts)}: {current_text}")

                        if len(found_texts) >= minimum_required:
                            break

                    except StaleElementReferenceException:
                        continue

                if len(found_texts) >= minimum_required:
                    break

            print("\nFound texts:")
            for text in sorted(found_texts):
                print(text)

            missing_texts = expected_texts - found_texts

            self.assertGreaterEqual(
                len(found_texts),
                minimum_required,
                f"Too few texts found. Expected at least {minimum_required}, "
                f"but found {len(found_texts)}. Missing: {missing_texts}"
            )

        except Exception as e:
            raise Exception(f"Canvas hover verification failed: {e}")

class EdgeDriverGrok(unittest.TestCase):

    TEST_TITLES = {
        "test_001_P": "Verify xAI homepage opens and loads correctly",
        "test_002_P": "Verify xAI homepage top navigation and Area text field by hovering on links and button",
        "test_003_P": "Hover  and click on TRY GROK button and verify URL, Title, and Elements on Grok page",
        "test_004_P": "Click on Imagine link and enter text in prompt input field",
        "test_005_P": "Verify by hover at least three tooltip texts appear on canvas",
        "test_001_N": "Invalid URL handling",
        "test_002_N": "Grok link behaviour",
        "test_003_N": "Grok link behavior by focusing and pressing Enter/Return",
        "test_004_N": "Verify AI processes a Latin-letter foreign phrase",
        "test_005_N": "Verify animation response to user interaction after highlighting.",

    }

    def setUp(self):
        test_name = self._testMethodName
        title = self.TEST_TITLES.get(test_name, "Unknown test")

        print("\n" + "=" * 80)
        print(f"START TEST: {test_name} | {title}")
        print("=" * 80)

        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = utilis.create_driver("edge")
        self.driver.maximize_window()

    def tearDown(self):
        print("\n" + "=" * 80)
        print(f"END TEST: {self._testMethodName}")
        print("=" * 80)

        if hasattr(self, "driver"):
            self.driver.quit()
            print("Browser closed successfully")


    # ========= Positive Tests ==========

    # Verify xAI homepage opens and loads correctly
    def test_001_P(self):
        driver = self.driver
        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open homepage: {e}")
        # Wait for page load
        try:
            utilis.wait_body(driver)
            print("Page body loaded successfully")
        except Exception as e:
            raise Exception(f"Failed to load page body: {e}")
        # Verify Title
        try:
            utilis.wait_title_contains(driver, "xAI")
            print("Title verified successfully:", driver.title)
        except Exception as e:
            raise Exception(f"Title verification failed: {e}")
        # Verify homepage
        try:
            utilis.wait_url_contains(driver, "x.ai")
            # self.assertIn("x.ai", driver.current_url)
            print("URL verified successfully", driver.current_url)
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")

    # Verify xAI homepage top navigation and Area text field by hovering on links and button
    def test_002_P(self):
        driver = self.driver
        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open homepage: {e}")
        # Verify top navigation bar, btn links.
        try:
            utilis.wait_element_css(driver, ".flex.items-center.justify-between")
            print("Top navigation bar verified successfully")
            utilis.wait_element_xpath(driver, "//nav[.//a[@aria-label='xAI Homepage']]")
            print("Homepage button link verified successfully")
            utilis.wait_link_text(driver, "Grok")
            print("Grok button link verified successfully")
            utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            print("Try Grok button link verified successfully")
        except Exception as e:
            raise Exception(f"Top navigation bar verification failed: {e}")
        # User hover on Navigation bar link and TRY GROK button
        try:
            home_link = utilis.wait_element_css(driver, 'a[href="/"]')
            ActionChains(driver).move_to_element(home_link).perform()
            time.sleep(1)
            print("Home link hover successfully")
            grok_link = utilis.wait_element_css(driver, 'a[href="/grok"]')
            ActionChains(driver).move_to_element(grok_link).perform()
            time.sleep(1)
            print("Grok link hover successfully")
            api_link = utilis.wait_element_css(driver, 'a[href="/api"]')
            ActionChains(driver).move_to_element(api_link).perform()
            time.sleep(1)
            print("API link hover successfully")
            company_link = utilis.wait_element_css(driver, 'a[href="/company"]')
            ActionChains(driver).move_to_element(company_link).perform()
            time.sleep(1)
            print("Company link hover successfully")
            colossus_link = utilis.wait_element_css(driver, 'a[href="/colossus"]')
            ActionChains(driver).move_to_element(colossus_link).perform()
            time.sleep(1)
            print("Colossus link hover successfully")
            careers_link = utilis.wait_element_css(driver, 'a[href="/careers"]')
            ActionChains(driver).move_to_element(careers_link).perform()
            time.sleep(1)
            print("Careers link hover successfully")
            news_link = utilis.wait_element_css(driver, 'a[href="/news"]')
            ActionChains(driver).move_to_element(news_link).perform()
            time.sleep(1)
            print("News link hover successfully")
            shop_link = utilis.wait_element_css(driver, 'a[href="https://shop.x.ai"]')
            ActionChains(driver).move_to_element(shop_link).perform()
            time.sleep(1)
            print("Shop link hover successfully")
            space_link = utilis.wait_element_css(driver, 'a[href="https://spacex.com/"]')
            ActionChains(driver).move_to_element(space_link).perform()
            time.sleep(1)
            print("Space link hover successfully")
            x_link = utilis.wait_element_css(driver, 'a[href="https://x.com"]')
            ActionChains(driver).move_to_element(x_link).perform()
            time.sleep(1)
            print("X link hover successfully")
            try_grok_link = utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            ActionChains(driver).move_to_element(try_grok_link).perform()
            time.sleep(1)
            print("Try Grok link hover successfully")
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")
        # Verify Text Area field
        try:
            utilis.wait_element_name(driver, "query")
            print("Text Area field verified successfully")
        except Exception as e:
            raise Exception(f"Top navigation bar verification failed: {e}")

    # Hover  and click on TRY GROK button and verify URL, Title, and Elements on Grok page
    def test_003_P(self):
        driver = self.driver
        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open homepage: {e}")
        # Hover on Try Grok btn and click
        try:
            try_grok_link = utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            ActionChains(driver).move_to_element(try_grok_link).perform()
            time.sleep(1)
            try_grok_link.click()
            print("Try Grok button hover and clicked successfully")
        except Exception as e:
            raise Exception(f"Hover on Try Grok failed: {e}")
        # Verify URL
        try:
            utilis.wait_url_contains(driver, "grok.com")
            # self.assertIn("https://grok.com/?referrer=web", driver.current_url)
            print("URL verified successfully:", driver.current_url)
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")
        time.sleep(5)
        # Verify Title
        try:
            utilis.wait_title_contains(driver, "Grok")
            print("Title verified successfully:", driver.title)
        except Exception as e:
            raise Exception(f"Title verification failed: {e}")
        # Verify Elements on Grok page
        try:
            imagine_link = utilis.wait_element_css(driver, 'a[href="/imagine"]')
            self.assertTrue(imagine_link.is_displayed())
            print("Imagine Link on Grok page verified successfully:", imagine_link.text)
            text_area = utilis.wait_element_css(driver, 'textarea[aria-label="Ask Grok anything"]')
            self.assertTrue(text_area.is_displayed())
            print("Text Area on Grok page verified successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(5)

    # Click on Imagine link and enter text in prompt input field
    def test_004_P(self):
        driver = self.driver
        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open homepage: {e}")
        time.sleep(3)
        # Click on Try Grok btn
        try:
            try_grok_link = utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            time.sleep(1)
            try_grok_link.click()
            print("Try Grok button clicked successfully")
        except Exception as e:
            raise Exception(f"Click on Try Grok failed: {e}")
        time.sleep(3)

        # Click on Imagine link and click back arrow
        try:
            imagine_link = utilis.wait_element_css(driver, 'a[href="/imagine"]')
            imagine_link.click()
            print("Imagine Link on Grok page clicked successfully:")
        except Exception as e:
            raise Exception(f"Click on Imagine link failed: {e}")

        # Verify Imagine URL
        try:
            utilis.wait_url_contains(driver, "https://grok.com/imagine")
            self.assertIn("https://grok.com/imagine", driver.current_url)
            print("URL verified successfully:,", driver.current_url)
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")
        time.sleep(3)
        # Click back arrow
        try:
            time.sleep(2)
            driver.back()
            print("Back button clicked successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(3)
        # Type the Question and click Enter
        try:
            text_area = utilis.wait_element_css(driver, 'textarea[aria-label="Ask Grok anything"]')
            text_area.click()
            text_area.clear()
            text_area.send_keys("What is current Time, Date, and Year NOW?")
            time.sleep(5)
            text_area.send_keys(Keys.ENTER)
            print("Question Entered and submitted successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(5)

    # Verify by hover at least three tooltip texts appear on canvas
    def test_005_P(self):
        driver = self.driver
        expected_texts = {
            "WHAT FUELS THE PULSE OF CREATION?",
            "DOES EXISTENCE HOLD INHERENT MEANING?",
            "DO QUANTUM REALMS DICTATE FATE?",
            "ARE WE ALONE IN ETERNITY’S EXPANSE?",
            "HOW DOES CHAOS BIRTH COSMIC ORDER?",
            "WHAT LIES BEYOND THE OBSERVABLE VOID?",
            "CAN WE TRAVERSE TIME'S ARROW?",
            "WHAT HIDES IN THE UNIVERSE'S SHADOWS?",
            "IS THE UNIVERSE INFINITELY LAYERED?",
            "WHAT SPARKED THE UNIVERSE'S BIRTH?",
            "DO MULTIPLE REALITIES COEXIST?",
            "ARE WE ECHOES OF A GREATER DESIGN?",
            "CAN ENTROPY EVER BE REVERSED?",
            "HOW DO BLACK HOLES RESHAPE REALITY?",
            "HOW DOES CONSCIOUSNESS EMERGE FROM MATTER?",
            "CAN ONE THEORY ENCOMPASS ALL REALITY?",
            "DO OTHER MINDS INHABIT THE STARS?",
            "WHAT DESTINY AWAITS THE COSMOS?"
        }

        found_texts = set()
        minimum_required = 3
        try:
            # Open homepage
            driver.get("https://x.ai/")
            print("Page loaded successfully")
            time.sleep(4)
            # Scroll down
            utilis.scroll_page(driver, y=2000, timeout=5)
            print("Page scrolled successfully")

            # Verify canvas
            canvas = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'canvas[data-engine="three.js r172"]')
                )
            )
            self.assertTrue(canvas.is_displayed(), "Canvas is not visible")
            print("Canvas ready")
            # Start hovering tooltips on canvas
            for x in range(-220, 221, 40):
                for y in range(-220, 221, 40):
                    try:
                        ActionChains(driver).move_to_element_with_offset(canvas, x, y).perform()

                        tooltip_elements = driver.find_elements(
                            By.XPATH, '//div[contains(@class,"bg-background/80")]'
                        )
                        visible_tooltips = [el for el in tooltip_elements if el.is_displayed()]

                        if not visible_tooltips:
                            continue

                        current_text = visible_tooltips[0].text.strip()

                        if current_text in expected_texts and current_text not in found_texts:
                            found_texts.add(current_text)
                            print(f"Found text {len(found_texts)}: {current_text}")

                        if len(found_texts) >= minimum_required:
                            break

                    except StaleElementReferenceException:
                        continue

                if len(found_texts) >= minimum_required:
                    break
            print("\nFound texts:")
            for text in sorted(found_texts):
                print(text)

            missing_texts = expected_texts - found_texts

            self.assertGreaterEqual(
                len(found_texts),
                minimum_required,
                f"Too few texts found. Expected at least {minimum_required}, "
                f"but found {len(found_texts)}. Missing: {missing_texts}"
            )
        except Exception as e:
            raise Exception(f"Canvas hover verification failed: {e}")


 # ========= Negative Tests ==========

    # Check invalid URL handling
    def test_001_N(self):
        driver = self.driver

        # Open invalid URL
        try:
            driver.get("https://x.ai/https:/x.ai")
            print("Invalid URL opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open invalid URL: {e}")

        # Verify invalid page message
        try:
            page_not_found = driver.find_element(By.XPATH, "//h1[text()='Page not found']")
            assert page_not_found.is_displayed(), "Page not found message is not displayed"
            print("Invalid Page Message visible successful")
            driver.save_screenshot("page_not_found.png")
        except Exception as e:
            raise Exception(f"Invalid URL verification failed: {e}")

        # Verify BACK TO HOME button
        try:
            back_to_home = driver.find_element(By.XPATH, "//a[normalize-space()='Back to home']")
            assert back_to_home.is_displayed(), "BACK TO HOME button is not displayed"
            back_to_home.click()
            print("BACK TO HOME button visible successful and Clicked")
            driver.save_screenshot("back_to_home.png")
        except Exception as e:
            raise Exception(f"BACK TO HOME button verification failed: {e}")

        # Verify HOME PAGE URL
        try:
            self.assertIn("https://x.ai/", driver.current_url)
            print(f"URL Home Page verified successfully: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")

    # Check Grok link behaviour
    def test_002_N(self):
        driver = self.driver

        try:
            driver.get("https://x.ai")
            print(f"Valid URL opened successfully: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Failed to open URL: {e}")

        try:
            grok_link = driver.find_element(By.CSS_SELECTOR, "a[href='/grok']")
            current_url_before = driver.current_url

            # Hover over Grok link
            ActionChains(driver).move_to_element(grok_link).perform()
            time.sleep(2)

            # Right-click on Grok link
            ActionChains(driver).context_click(grok_link).perform()
            time.sleep(2)

            # Verify no navigation happened after right-click
            self.assertEqual(current_url_before, driver.current_url)

            # Close context menu
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(3)

            # Press unsupported keys
            ActionChains(driver).send_keys("a").send_keys("5").send_keys("@").send_keys(Keys.SPACE).perform()
            time.sleep(1)

            # Verify no navigation happened
            self.assertEqual(current_url_before, driver.current_url)
            print("Unsupported keys did not open the Grok page")

        except Exception as e:
            raise Exception(f"Failed Grok link negative test: {e}")

    # Check Grok link behavior by focusing and pressing Enter/Return
    def test_003_N(self):
        driver = self.driver

        try:
            driver.get("https://x.ai")
            print(f"Valid URL opened successfully: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Failed to open URL: {e}")

        try:
            grok_link = driver.find_element(By.CSS_SELECTOR, "a[href='/grok']")
            old_url = driver.current_url
            time.sleep(2)
        except Exception as e:
            raise Exception(f"Failed to find Grok link: {e}")

        try:
            # Focus Grok link
            driver.execute_script("arguments[0].focus();", grok_link)
            time.sleep(2)
        except Exception as e:
            raise Exception(f"Failed to find Grok link: {e}")

        try:
            # Press Enter
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            time.sleep(2)
        except Exception as e:
            raise Exception(f"Failed to find Grok link: {e}")

        try:
            # Wait for URL to change
            WebDriverWait(driver, 10).until(lambda d: d.current_url != old_url)
            new_url = driver.current_url

            print(f"Navigation successful. New URL: {new_url}")
            driver.save_screenshot("grok_link.png")
            print("New page screenshot saved successfully")

            # Verify navigation happened
            self.assertIn("/grok", new_url)
            self.assertNotEqual(old_url, new_url)
            print("Enter key opened the Grok page successfully")

        except Exception as e:
            raise Exception(f"Failed Grok link Enter key test: {e}")

    # Verify AI processes a Latin-letter foreign phrase

    def test_004_N(self):
        driver = self.driver
        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open homepage: {e}")
        time.sleep(3)
        # Click on Try Grok btn
        try:
            try_grok_link = utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            time.sleep(1)
            try_grok_link.click()
            print("Try Grok button clicked successfully")
        except Exception as e:
            raise Exception(f"Click on Try Grok failed: {e}")
        time.sleep(3)

        # Click on Imagine link and click back arrow
        try:
            imagine_link = utilis.wait_element_css(driver, 'a[href="/imagine"]')
            imagine_link.click()
            print("Imagine Link on Grok page clicked successfully:")
        except Exception as e:
            raise Exception(f"Click on Imagine link failed: {e}")

        # Verify Imagine URL
        try:
            utilis.wait_url_contains(driver, "https://grok.com/imagine")
            self.assertIn("https://grok.com/imagine", driver.current_url)
            print("URL verified successfully:,", driver.current_url)
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")
        time.sleep(3)
        # Click back arrow
        try:
            time.sleep(2)
            driver.back()
            print("Back button clicked successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(3)
        # Type the Question and click Enter
        try:
            text_area = utilis.wait_element_css(driver, 'textarea[aria-label="Ask Grok anything"]')
            text_area.click()
            text_area.clear()
            text_area.send_keys("nazovi kakoe ceicha chislo, vremya i god na angkiskom")
            time.sleep(5)
            text_area.send_keys(Keys.ENTER)
            print("Question Entered and submitted successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(5)
        # Verify AI processes a Latin-letter foreign phrase
        try:
            phrase = utilis.wait_element_css(driver, 'strong.font-semibold')
            print("Foreign phrase verified successfully:", phrase.text)
        except Exception as e:
            raise Exception(f"Failed text area test: {e}")
        # Get the current page title and verify it contains the keywords

    # Verify animation response to user interaction after highlighting.
    def test_005_N(self):
        driver = self.driver
        expected_texts = {
            "WHAT FUELS THE PULSE OF CREATION?",
            "DOES EXISTENCE HOLD INHERENT MEANING?",
            "DO QUANTUM REALMS DICTATE FATE?",
            "ARE WE ALONE IN ETERNITY’S EXPANSE?",
            "HOW DOES CHAOS BIRTH COSMIC ORDER?",
            "WHAT LIES BEYOND THE OBSERVABLE VOID?",
            "CAN WE TRAVERSE TIME'S ARROW?",
            "WHAT HIDES IN THE UNIVERSE'S SHADOWS?",
            "IS THE UNIVERSE INFINITELY LAYERED?",
            "WHAT SPARKED THE UNIVERSE'S BIRTH?",
            "DO MULTIPLE REALITIES COEXIST?",
            "ARE WE ECHOES OF A GREATER DESIGN?",
            "CAN ENTROPY EVER BE REVERSED?",
            "HOW DO BLACK HOLES RESHAPE REALITY?",
            "HOW DOES CONSCIOUSNESS EMERGE FROM MATTER?",
            "CAN ONE THEORY ENCOMPASS ALL REALITY?",
            "DO OTHER MINDS INHABIT THE STARS?",
            "WHAT DESTINY AWAITS THE COSMOS?"
        }

        found_texts = set()
        minimum_required = 3

        try:
            driver.get("https://x.ai/")
            print("Page loaded successfully")
            time.sleep(4)

            utilis.scroll_page(driver, y=2000, timeout=5)
            print("Page scrolled successfully")

            canvas_locator = (By.CSS_SELECTOR, 'canvas[data-engine="three.js r172"]')
            canvas = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(canvas_locator)
            )
            self.assertTrue(canvas.is_displayed(), "Canvas is not visible")
            print("Canvas ready")

            # click on empty space inside canvas
            ActionChains(driver).move_to_element_with_offset(canvas, 5, 5).click().perform()
            time.sleep(0.5)

            # Command + A on macOS
            ActionChains(driver).key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
            time.sleep(1)

            for x in range(-220, 221, 40):
                for y in range(-220, 221, 40):
                    try:
                        canvas = WebDriverWait(driver, 5).until(
                            EC.visibility_of_element_located(canvas_locator)
                        )

                        ActionChains(driver).move_to_element_with_offset(canvas, x, y).perform()
                        time.sleep(0.2)

                        tooltip_elements = driver.find_elements(
                            By.XPATH, '//div[contains(@class,"bg-background/80")]'
                        )

                        visible_tooltips = [
                            el for el in tooltip_elements
                            if el.is_displayed() and el.text.strip()
                        ]

                        if not visible_tooltips:
                            continue

                        current_text = visible_tooltips[0].text.strip()

                        if current_text in expected_texts and current_text not in found_texts:
                            found_texts.add(current_text)
                            print(f"Found text {len(found_texts)}: {current_text}")

                        if len(found_texts) >= minimum_required:
                            break

                    except StaleElementReferenceException:
                        continue

                if len(found_texts) >= minimum_required:
                    break

            print("\nFound texts:")
            for text in sorted(found_texts):
                print(text)

            missing_texts = expected_texts - found_texts

            self.assertGreaterEqual(
                len(found_texts),
                minimum_required,
                f"Too few texts found. Expected at least {minimum_required}, "
                f"but found {len(found_texts)}. Missing: {missing_texts}"
            )

        except Exception as e:
            raise Exception(f"Canvas hover verification failed: {e}")

class FirefoxDriverGrok(unittest.TestCase):

    TEST_TITLES = {
        "test_001_P": "Verify xAI homepage opens and loads correctly",
        "test_002_P": "Verify xAI homepage top navigation and Area text field by hovering on links and button",
        "test_003_P": "Hover  and click on TRY GROK button and verify URL, Title, and Elements on Grok page",
        "test_004_P": "Click on Imagine link and enter text in prompt input field",
        "test_005_P": "Verify by hover at least three tooltip texts appear on canvas",
        "test_001_N": "Invalid URL handling",
        "test_002_N": "Grok link behaviour",
        "test_003_N": "Grok link behavior by focusing and pressing Enter/Return",
        "test_004_N": "Verify AI processes a Latin-letter foreign phrase",
        "test_005_N": "Verify animation response to user interaction after highlighting.",

    }

    def setUp(self):
        test_name = self._testMethodName
        title = self.TEST_TITLES.get(test_name, "Unknown test")

        print("\n" + "=" * 80)
        print(f"START TEST: {test_name} | {title}")
        print("=" * 80)

        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = utilis.create_driver("firefox")
        self.driver.maximize_window()

    def tearDown(self):
        print("\n" + "=" * 80)
        print(f"END TEST: {self._testMethodName}")
        print("=" * 80)

        if hasattr(self, "driver"):
            self.driver.quit()
            print("Browser closed successfully")


    # ========= Positive Tests ==========

    # Verify xAI homepage opens and loads correctly
    def test_001_P(self):
        driver = self.driver
        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open homepage: {e}")
        # Wait for page load
        try:
            utilis.wait_body(driver)
            print("Page body loaded successfully")
        except Exception as e:
            raise Exception(f"Failed to load page body: {e}")
        # Verify Title
        try:
            utilis.wait_title_contains(driver, "xAI")
            print("Title verified successfully:", driver.title)
        except Exception as e:
            raise Exception(f"Title verification failed: {e}")
        # Verify homepage
        try:
            utilis.wait_url_contains(driver, "x.ai")
            # self.assertIn("x.ai", driver.current_url)
            print("URL verified successfully", driver.current_url)
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")

    # Verify xAI homepage top navigation and Area text field by hovering on links and button
    def test_002_P(self):
        driver = self.driver
        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open homepage: {e}")
        # Verify top navigation bar, btn links.
        try:
            utilis.wait_element_css(driver, ".flex.items-center.justify-between")
            print("Top navigation bar verified successfully")
            utilis.wait_element_xpath(driver, "//nav[.//a[@aria-label='xAI Homepage']]")
            print("Homepage button link verified successfully")
            utilis.wait_link_text(driver, "Grok")
            print("Grok button link verified successfully")
            utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            print("Try Grok button link verified successfully")
        except Exception as e:
            raise Exception(f"Top navigation bar verification failed: {e}")
        # User hover on Navigation bar link and TRY GROK button
        try:
            home_link = utilis.wait_element_css(driver, 'a[href="/"]')
            ActionChains(driver).move_to_element(home_link).perform()
            time.sleep(1)
            print("Home link hover successfully")
            grok_link = utilis.wait_element_css(driver, 'a[href="/grok"]')
            ActionChains(driver).move_to_element(grok_link).perform()
            time.sleep(1)
            print("Grok link hover successfully")
            api_link = utilis.wait_element_css(driver, 'a[href="/api"]')
            ActionChains(driver).move_to_element(api_link).perform()
            time.sleep(1)
            print("API link hover successfully")
            company_link = utilis.wait_element_css(driver, 'a[href="/company"]')
            ActionChains(driver).move_to_element(company_link).perform()
            time.sleep(1)
            print("Company link hover successfully")
            colossus_link = utilis.wait_element_css(driver, 'a[href="/colossus"]')
            ActionChains(driver).move_to_element(colossus_link).perform()
            time.sleep(1)
            print("Colossus link hover successfully")
            careers_link = utilis.wait_element_css(driver, 'a[href="/careers"]')
            ActionChains(driver).move_to_element(careers_link).perform()
            time.sleep(1)
            print("Careers link hover successfully")
            news_link = utilis.wait_element_css(driver, 'a[href="/news"]')
            ActionChains(driver).move_to_element(news_link).perform()
            time.sleep(1)
            print("News link hover successfully")
            shop_link = utilis.wait_element_css(driver, 'a[href="https://shop.x.ai"]')
            ActionChains(driver).move_to_element(shop_link).perform()
            time.sleep(1)
            print("Shop link hover successfully")
            space_link = utilis.wait_element_css(driver, 'a[href="https://spacex.com/"]')
            ActionChains(driver).move_to_element(space_link).perform()
            time.sleep(1)
            print("Space link hover successfully")
            x_link = utilis.wait_element_css(driver, 'a[href="https://x.com"]')
            ActionChains(driver).move_to_element(x_link).perform()
            time.sleep(1)
            print("X link hover successfully")
            try_grok_link = utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            ActionChains(driver).move_to_element(try_grok_link).perform()
            time.sleep(1)
            print("Try Grok link hover successfully")
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")
        # Verify Text Area field
        try:
            utilis.wait_element_name(driver, "query")
            print("Text Area field verified successfully")
        except Exception as e:
            raise Exception(f"Top navigation bar verification failed: {e}")

    # Hover  and click on TRY GROK button and verify URL, Title, and Elements on Grok page
    def test_003_P(self):
        driver = self.driver
        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open homepage: {e}")
        # Hover on Try Grok btn and click
        try:
            try_grok_link = utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            ActionChains(driver).move_to_element(try_grok_link).perform()
            time.sleep(1)
            try_grok_link.click()
            print("Try Grok button hover and clicked successfully")
        except Exception as e:
            raise Exception(f"Hover on Try Grok failed: {e}")
        # Verify URL
        try:
            utilis.wait_url_contains(driver, "grok.com")
            # self.assertIn("https://grok.com/?referrer=web", driver.current_url)
            print("URL verified successfully:", driver.current_url)
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")
        time.sleep(5)
        # Verify Title
        try:
            utilis.wait_title_contains(driver, "Grok")
            print("Title verified successfully:", driver.title)
        except Exception as e:
            raise Exception(f"Title verification failed: {e}")
        # Verify Elements on Grok page
        try:
            imagine_link = utilis.wait_element_css(driver, 'a[href="/imagine"]')
            self.assertTrue(imagine_link.is_displayed())
            print("Imagine Link on Grok page verified successfully:", imagine_link.text)
            text_area = utilis.wait_element_css(driver, 'textarea[aria-label="Ask Grok anything"]')
            self.assertTrue(text_area.is_displayed())
            print("Text Area on Grok page verified successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(5)

    # Click on Imagine link and enter text in prompt input field
    def test_004_P(self):
        driver = self.driver
        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open homepage: {e}")
        time.sleep(3)
        # Click on Try Grok btn
        try:
            try_grok_link = utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            time.sleep(1)
            try_grok_link.click()
            print("Try Grok button clicked successfully")
        except Exception as e:
            raise Exception(f"Click on Try Grok failed: {e}")
        time.sleep(3)

        # Click on Imagine link and click back arrow
        try:
            imagine_link = utilis.wait_element_css(driver, 'a[href="/imagine"]')
            imagine_link.click()
            time.sleep(1)
            print("Imagine Link on Grok page clicked successfully:")
        except Exception as e:
            raise Exception(f"Click on Imagine link failed: {e}")

        # Verify Imagine URL
        try:
            utilis.wait_url_contains(driver, "https://grok.com/imagine")
            self.assertIn("https://grok.com/imagine", driver.current_url)
            print("URL verified successfully:,", driver.current_url)
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")
        time.sleep(3)
        # Click back arrow
        try:
            time.sleep(2)
            driver.back()
            print("Back button clicked successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(3)
        # Type the Question and click Enter
        try:
            text_area = utilis.wait_element_css(driver, 'textarea[aria-label="Ask Grok anything"]')
            text_area.click()
            text_area.clear()
            text_area.send_keys("What is current Time, Date, and Year NOW?")
            time.sleep(5)
            text_area.send_keys(Keys.ENTER)
            print("Question Entered and submitted successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(5)

    # Verify by hover at least three tooltip texts appear on canvas
    def test_005_P(self):
        driver = self.driver
        expected_texts = {
            "WHAT FUELS THE PULSE OF CREATION?",
            "DOES EXISTENCE HOLD INHERENT MEANING?",
            "DO QUANTUM REALMS DICTATE FATE?",
            "ARE WE ALONE IN ETERNITY’S EXPANSE?",
            "HOW DOES CHAOS BIRTH COSMIC ORDER?",
            "WHAT LIES BEYOND THE OBSERVABLE VOID?",
            "CAN WE TRAVERSE TIME'S ARROW?",
            "WHAT HIDES IN THE UNIVERSE'S SHADOWS?",
            "IS THE UNIVERSE INFINITELY LAYERED?",
            "WHAT SPARKED THE UNIVERSE'S BIRTH?",
            "DO MULTIPLE REALITIES COEXIST?",
            "ARE WE ECHOES OF A GREATER DESIGN?",
            "CAN ENTROPY EVER BE REVERSED?",
            "HOW DO BLACK HOLES RESHAPE REALITY?",
            "HOW DOES CONSCIOUSNESS EMERGE FROM MATTER?",
            "CAN ONE THEORY ENCOMPASS ALL REALITY?",
            "DO OTHER MINDS INHABIT THE STARS?",
            "WHAT DESTINY AWAITS THE COSMOS?"
        }

        found_texts = set()
        minimum_required = 3
        try:
            # Open homepage
            driver.get("https://x.ai/")
            print("Page loaded successfully")
            time.sleep(4)
            # Scroll down
            utilis.scroll_page(driver, y=2000, timeout=5)
            print("Page scrolled successfully")

            # Verify canvas
            canvas = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'canvas[data-engine="three.js r172"]')
                )
            )
            self.assertTrue(canvas.is_displayed(), "Canvas is not visible")
            print("Canvas ready")
            # Start hovering tooltips on canvas
            for x in range(-220, 221, 40):
                for y in range(-220, 221, 40):
                    try:
                        ActionChains(driver).move_to_element_with_offset(canvas, x, y).perform()

                        tooltip_elements = driver.find_elements(
                            By.XPATH, '//div[contains(@class,"bg-background/80")]'
                        )
                        visible_tooltips = [el for el in tooltip_elements if el.is_displayed()]

                        if not visible_tooltips:
                            continue

                        current_text = visible_tooltips[0].text.strip()

                        if current_text in expected_texts and current_text not in found_texts:
                            found_texts.add(current_text)
                            print(f"Found text {len(found_texts)}: {current_text}")

                        if len(found_texts) >= minimum_required:
                            break

                    except StaleElementReferenceException:
                        continue

                if len(found_texts) >= minimum_required:
                    break
            print("\nFound texts:")
            for text in sorted(found_texts):
                print(text)

            missing_texts = expected_texts - found_texts

            self.assertGreaterEqual(
                len(found_texts),
                minimum_required,
                f"Too few texts found. Expected at least {minimum_required}, "
                f"but found {len(found_texts)}. Missing: {missing_texts}"
            )
        except Exception as e:
            raise Exception(f"Canvas hover verification failed: {e}")


 # ========= Negative Tests ==========

    # Check invalid URL handling
    def test_001_N(self):
        driver = self.driver

        # Open invalid URL
        try:
            driver.get("https://x.ai/https:/x.ai")
            print("Invalid URL opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open invalid URL: {e}")

        # Verify invalid page message
        try:
            page_not_found = driver.find_element(By.XPATH, "//h1[text()='Page not found']")
            assert page_not_found.is_displayed(), "Page not found message is not displayed"
            print("Invalid Page Message visible successful")
            driver.save_screenshot("page_not_found.png")
        except Exception as e:
            raise Exception(f"Invalid URL verification failed: {e}")

        # Verify BACK TO HOME button
        try:
            back_to_home = driver.find_element(By.XPATH, "//a[normalize-space()='Back to home']")
            assert back_to_home.is_displayed(), "BACK TO HOME button is not displayed"
            back_to_home.click()
            print("BACK TO HOME button visible successful and Clicked")
            driver.save_screenshot("back_to_home.png")
        except Exception as e:
            raise Exception(f"BACK TO HOME button verification failed: {e}")

        # Verify HOME PAGE URL
        try:
            self.assertIn("https://x.ai/", driver.current_url)
            print(f"URL Home Page verified successfully: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")

    # Check Grok link behaviour
    def test_002_N(self):
        driver = self.driver

        try:
            driver.get("https://x.ai")
            print(f"Valid URL opened successfully: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Failed to open URL: {e}")

        try:
            grok_link = driver.find_element(By.CSS_SELECTOR, "a[href='/grok']")
            current_url_before = driver.current_url

            # Hover over Grok link
            ActionChains(driver).move_to_element(grok_link).perform()
            time.sleep(2)

            # Right-click on Grok link
            ActionChains(driver).context_click(grok_link).perform()
            time.sleep(2)

            # Verify no navigation happened after right-click
            self.assertEqual(current_url_before, driver.current_url)

            # Close context menu
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(3)

            # Press unsupported keys
            ActionChains(driver).send_keys("a").send_keys("5").send_keys("@").send_keys(Keys.SPACE).perform()
            time.sleep(1)

            # Verify no navigation happened
            self.assertEqual(current_url_before, driver.current_url)
            print("Unsupported keys did not open the Grok page")

        except Exception as e:
            raise Exception(f"Failed Grok link negative test: {e}")

    # Check Grok link behavior by focusing and pressing Enter/Return
    def test_003_N(self):
        driver = self.driver

        try:
            driver.get("https://x.ai")
            print(f"Valid URL opened successfully: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Failed to open URL: {e}")

        try:
            grok_link = driver.find_element(By.CSS_SELECTOR, "a[href='/grok']")
            old_url = driver.current_url
            time.sleep(2)
        except Exception as e:
            raise Exception(f"Failed to find Grok link: {e}")

        try:
            # Focus Grok link
            driver.execute_script("arguments[0].focus();", grok_link)
            time.sleep(2)
        except Exception as e:
            raise Exception(f"Failed to find Grok link: {e}")

        try:
            # Press Enter
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            time.sleep(2)
        except Exception as e:
            raise Exception(f"Failed to find Grok link: {e}")

        try:
            # Wait for URL to change
            WebDriverWait(driver, 10).until(lambda d: d.current_url != old_url)
            new_url = driver.current_url

            print(f"Navigation successful. New URL: {new_url}")
            driver.save_screenshot("grok_link.png")
            print("New page screenshot saved successfully")

            # Verify navigation happened
            self.assertIn("/grok", new_url)
            self.assertNotEqual(old_url, new_url)
            print("Enter key opened the Grok page successfully")

        except Exception as e:
            raise Exception(f"Failed Grok link Enter key test: {e}")

    # Verify AI processes a Latin-letter foreign phrase

    def test_004_N(self):
        driver = self.driver
        # Open homepage
        try:
            driver.get("https://x.ai/")
            print("Homepage opened successfully")
        except Exception as e:
            raise Exception(f"Failed to open homepage: {e}")
        time.sleep(3)
        # Click on Try Grok btn
        try:
            try_grok_link = utilis.wait_element_xpath(driver, "//a[normalize-space()='Try Grok']")
            time.sleep(1)
            try_grok_link.click()
            print("Try Grok button clicked successfully")
        except Exception as e:
            raise Exception(f"Click on Try Grok failed: {e}")
        time.sleep(3)

        # Click on Imagine link and click back arrow
        try:
            imagine_link = utilis.wait_element_css(driver, 'a[href="/imagine"]')
            imagine_link.click()
            print("Imagine Link on Grok page clicked successfully:")
        except Exception as e:
            raise Exception(f"Click on Imagine link failed: {e}")

        # Verify Imagine URL
        try:
            utilis.wait_url_contains(driver, "https://grok.com/imagine")
            self.assertIn("https://grok.com/imagine", driver.current_url)
            print("URL verified successfully:,", driver.current_url)
        except Exception as e:
            raise Exception(f"Homepage verification failed: {e}")
        time.sleep(3)
        # Click back arrow
        try:
            time.sleep(2)
            driver.back()
            print("Back button clicked successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(3)
        # Type the Question and click Enter
        try:
            text_area = utilis.wait_element_css(driver, 'textarea[aria-label="Ask Grok anything"]')
            text_area.click()
            text_area.clear()
            text_area.send_keys("nazovi kakoe ceicha chislo, vremya i god na angkiskom")
            time.sleep(5)
            text_area.send_keys(Keys.ENTER)
            print("Question Entered and submitted successfully")
        except Exception as e:
            raise Exception(f"Elements on Grok page verification failed: {e}")
        time.sleep(5)
        # Verify AI processes a Latin-letter foreign phrase
        try:
            phrase = utilis.wait_element_css(driver, 'strong.font-semibold')
            print("Foreign phrase verified successfully:", phrase.text)
        except Exception as e:
            raise Exception(f"Failed text area test: {e}")
        # Get the current page title and verify it contains the keywords

    # Verify animation response to user interaction after highlighting.
    def test_005_N(self):
        driver = self.driver
        expected_texts = {
            "WHAT FUELS THE PULSE OF CREATION?",
            "DOES EXISTENCE HOLD INHERENT MEANING?",
            "DO QUANTUM REALMS DICTATE FATE?",
            "ARE WE ALONE IN ETERNITY’S EXPANSE?",
            "HOW DOES CHAOS BIRTH COSMIC ORDER?",
            "WHAT LIES BEYOND THE OBSERVABLE VOID?",
            "CAN WE TRAVERSE TIME'S ARROW?",
            "WHAT HIDES IN THE UNIVERSE'S SHADOWS?",
            "IS THE UNIVERSE INFINITELY LAYERED?",
            "WHAT SPARKED THE UNIVERSE'S BIRTH?",
            "DO MULTIPLE REALITIES COEXIST?",
            "ARE WE ECHOES OF A GREATER DESIGN?",
            "CAN ENTROPY EVER BE REVERSED?",
            "HOW DO BLACK HOLES RESHAPE REALITY?",
            "HOW DOES CONSCIOUSNESS EMERGE FROM MATTER?",
            "CAN ONE THEORY ENCOMPASS ALL REALITY?",
            "DO OTHER MINDS INHABIT THE STARS?",
            "WHAT DESTINY AWAITS THE COSMOS?"
        }

        found_texts = set()
        minimum_required = 3

        try:
            driver.get("https://x.ai/")
            print("Page loaded successfully")
            time.sleep(4)

            utilis.scroll_page(driver, y=2000, timeout=5)
            print("Page scrolled successfully")

            canvas_locator = (By.CSS_SELECTOR, 'canvas[data-engine="three.js r172"]')
            canvas = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(canvas_locator)
            )
            self.assertTrue(canvas.is_displayed(), "Canvas is not visible")
            print("Canvas ready")

            # click on empty space inside canvas
            ActionChains(driver).move_to_element_with_offset(canvas, 5, 5).click().perform()
            time.sleep(0.5)

            # Command + A on macOS
            ActionChains(driver).key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
            time.sleep(1)

            for x in range(-220, 221, 40):
                for y in range(-220, 221, 40):
                    try:
                        canvas = WebDriverWait(driver, 5).until(
                            EC.visibility_of_element_located(canvas_locator)
                        )

                        ActionChains(driver).move_to_element_with_offset(canvas, x, y).perform()
                        time.sleep(0.2)

                        tooltip_elements = driver.find_elements(
                            By.XPATH, '//div[contains(@class,"bg-background/80")]'
                        )

                        visible_tooltips = [
                            el for el in tooltip_elements
                            if el.is_displayed() and el.text.strip()
                        ]

                        if not visible_tooltips:
                            continue

                        current_text = visible_tooltips[0].text.strip()

                        if current_text in expected_texts and current_text not in found_texts:
                            found_texts.add(current_text)
                            print(f"Found text {len(found_texts)}: {current_text}")

                        if len(found_texts) >= minimum_required:
                            break

                    except StaleElementReferenceException:
                        continue

                if len(found_texts) >= minimum_required:
                    break

            print("\nFound texts:")
            for text in sorted(found_texts):
                print(text)

            missing_texts = expected_texts - found_texts

            self.assertGreaterEqual(
                len(found_texts),
                minimum_required,
                f"Too few texts found. Expected at least {minimum_required}, "
                f"but found {len(found_texts)}. Missing: {missing_texts}"
            )

        except Exception as e:
            raise Exception(f"Canvas hover verification failed: {e}")


if __name__ == "__main__":
    unittest.main()










