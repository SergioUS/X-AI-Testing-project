import random
from builtins import Exception
# from multiprocessing.connection import address_type

from selenium import webdriver
from selenium.webdriver.common.devtools.v143.fed_cm import LoginState
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.core import driver
from selenium.webdriver.edge.options import Options as EdgeOptions
import os
import utils
import time
import unittest
# import HtmlTestRunner
import AllureReports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def keyboard_tab_times_then_space(driver, times=5):

   # """Used in TC_P_015: press TAB N times, then SPACE (example: captcha focus attempt)."""

    keys = [Keys.TAB] * times + [Keys.SPACE]
    driver.switch_to.active_element.send_keys(*keys)

def delay():
    time.sleep(random.randint(3,5))



class ChromeXAIPositiveTests(unittest.TestCase):

    def setUp(self):
        # options = webdriver.ChromeOptions()
        # options.page_load_strategy = 'eager'
        # options.add_argument("--disable-blink-features=AutomationControlled")
        #options.add_argument("--window-size=1920,1080")
        #options.add_argument("--headless")
        self.driver = utils.create_driver("chrome")
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
    def test_TC_P_011(self):
        driver = self.driver
        driver.get("https://x.ai/")
        delay()
        first_window = driver.window_handles[0]
        driver.find_element(By.XPATH,"//a[normalize-space()='Shop']").click()
        delay()
        second_window = driver.window_handles[0]
        driver.switch_to.window(second_window)
        # products= driver.find_element(By.XPATH,"//h2[normalize-space()='All Products']")
        try:
            products = driver.find_element(By.TAG_NAME,  'h2')
            assert products.is_displayed()
            print("test 011 is passed")
        except:
            print("test 011 is NOT passed")


    def test_TC_P_012(self):
        driver = self.driver
        driver.get("https://shop.x.com/")
        delay()
        try:
            assert driver.title == 'Official xAI Shop'
            print("test 012 is passed")
        except:
            print("test 012 is NOT passed",driver.title)

    def test_TC_P_013(self):

        driver = self.driver
        driver.get("https://x.ai/")
        delay()

        try:
            driver.find_element(By.XPATH, "//a[normalize-space()='Shop']").click()
            print("button is clickable")
        except:
            print(" button is NOT clickable")


    def test_TC_P_014(self):

        driver = self.driver
        driver.get("https://shop.x.com/")
        delay()

        # driver.find_element(By.XPATH, "//span[@class='h6 link-faded md-max:hidden'][normalize-space()='Login']").click()
        try:
           WebDriverWait(driver,4).until(EC.element_to_be_clickable((By.XPATH,
                                "//span[@class='h6 link-faded md-max:hidden'][normalize-space()='Login']")))

           print("button Login is displayed and clickable")
        except:
           print(" button Login is NOT displayed and clickable")
           delay()

        try:
            WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH,"//li[@class='header__search-link']//a")))
            print("button Search is displayed and clickable")
        except:
            print("button Search is NOT displayed and clickable")

            delay()

        try:
            WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/cart']//span[@class='h6 link-faded md-max:hidden']")))
            print("button Cart is displayed and clickable")
        except:
            print("button Cart is NOT displayed and clickable")

            delay()

    def test_TC_P_015(self):

            driver = self.driver
            driver.get("https://shop.x.com/")
            delay()

            # Scroll to bottom
            try:
                driver.execute_script("window.scrollBy({top: 200, left: 0, behavior: 'smooth'});")
                print(" Scrolled ")
            except Exception as e:
                raise Exception(f"Scroll failed: {e}")
            time.sleep(5)

            # Click to bottom xAILogo Tee
            try:
                driver.find_element(By.XPATH, "//a[normalize-space()='xAI Logo Tee']").click()
                print("xAILogo is displayed and clickable")
            except:
                print("xAILogo is NOT displayed and clickable")
                delay()

            # Click to Cart bottom

            try:
                driver.find_element(By.XPATH, "//button[@class='button w-full']").click()

                print("Cart button is displayed and clickable")
            except:
                print("Cart button is NOT displayed and clickable")

                driver.quit()


class TestEdgePositiveTest(unittest.TestCase):



    def setUp(self):
        os.environ[
            "SE_DRIVER_MIRROR_URL"] = "https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/"
        os.environ["SE_CACHE_PATH"] = ""
        options = EdgeOptions()
        # options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()

    def test_TC_P_011(self):
        driver = self.driver
        driver.get("https://x.ai/")
        delay()
        first_window = driver.window_handles[0]
        driver.find_element(By.XPATH, "//a[normalize-space()='Shop']").click()
        delay()
        second_window = driver.window_handles[0]
        driver.switch_to.window(second_window)

        try:
            products = driver.find_element(By.TAG_NAME, 'h2')
            assert products.is_displayed()
            print("test 011 is passed")
        except:
            print("test 011 is NOT passed")

    def test_TC_P_012(self):
        driver = self.driver
        driver.get("https://shop.x.com/")
        delay()
        try:
            assert driver.title == 'Official xAI Shop'
            print("test 012 is passed")
        except:
            print("test 012 is NOT passed", driver.title)

    def test_TC_P_013(self):

        driver = self.driver
        driver.get("https://x.ai/")
        delay()

        try:
            driver.find_element(By.XPATH, "//a[normalize-space()='Shop']").click()
            print("button is clickable")
        except:
            print(" button is NOT clickable")

    def test_TC_P_014(self):

        driver = self.driver
        driver.get("https://shop.x.com/")
        delay()

        # driver.find_element(By.XPATH, "//span[@class='h6 link-faded md-max:hidden'][normalize-space()='Login']").click()
        try:
            WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH,
                                                                       "//span[@class='h6 link-faded md-max:hidden'][normalize-space()='Login']")))

            print("button Login is displayed and clickable")
        except:
            print(" button Login is NOT displayed and clickable")
            delay()

        try:
            WebDriverWait(driver, 4).until(
                EC.element_to_be_clickable((By.XPATH, "//li[@class='header__search-link']//a")))
            print("button Search is displayed and clickable")
        except:
            print("button Search is NOT displayed and clickable")

            delay()

        try:
            WebDriverWait(driver, 4).until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='/cart']//span[@class='h6 link-faded md-max:hidden']")))
            print("button Cart is displayed and clickable")
        except:
            print("button Cart is NOT displayed and clickable")

            delay()

    def test_TC_P_015(self):

        driver = self.driver
        driver.get("https://shop.x.com/")
        delay()

        # Scroll to bottom
        try:
            driver.execute_script("window.scrollBy({top: 200, left: 0, behavior: 'smooth'});")
            print(" Scrolled ")
        except Exception as e:
            raise Exception(f"Scroll failed: {e}")
        time.sleep(5)

        # Click to bottom xAILogo Tee
        try:
            driver.find_element(By.XPATH, "//a[normalize-space()='xAI Logo Tee']").click()
            print("xAILogo is displayed and clickable")
        except:
            print("xAILogo is NOT displayed and clickable")
            delay()

        # Click to Cart bottom

        try:
            driver.find_element(By.XPATH, "//button[@class='button w-full']").click()

            print("Cart button is displayed and clickable")
        except:
            print("Cart button is NOT displayed and clickable")

            driver.quit()

class ChromeXAINegativeTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--window-size=1920,1080")
        # options.add_argument("--headless")

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        # self.driver = utils.create_driver("chrome")
    def tearDown(self):
        self.driver.quit()

    def test_TC_N_011(self):

        driver = self.driver
        try:
            driver.get(" https://x.ai/12345 ")
            print("Invalid URL Navigation")
        except Exception as e:
            print(" xAI main page is opened:", e)
            raise Exception(f"Failed to open xAI home page: {e}")

        time.sleep(3)

    def test_TC_N_012(self):

        driver = self.driver
        driver.get("https://shop.x.com/account/login")
        delay()

        wait = WebDriverWait(driver, 10)

        # Locate fields (adjust locators if UI changes)
        try:
            email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='input--template--25407258788123__main--customeremail']")))
            email_field.clear()
            email_field.send_keys("julia@@gmail.com")
            print("email entered")
        except Exception as e:
            print(" email not entered:", e)
            time.sleep(5)

        try:
            password_field = driver.find_element(By.XPATH, "//input[@id='input--template--25407258788123__main--customerpassword']")
            password_field.clear()
            password_field.send_keys("12345678")
            print("password entered")
        except Exception as e:
            print(" password not entered:", e)
            time.sleep(5)

        try:
            login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
            login_button.click()
            time.sleep(5)
            print("login button is displayed and clickable")
        except Exception as e:
            print(" login button NOT displayed and clickable")



    def test_TC_N_013(self):



        driver = self.driver
        driver.get("https://shop.x.com/checkouts/cn/hWNAx4Vzpw4vark8usbYIa8H/en-us/information?_r=AQABSS4sFGU7tPHhCpz4xEvrYiykf56xXx01a9FpwTIljwA")
        delay()


        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)
        delay()

        try:
            driver.find_element(By.XPATH, "//button[@class='_1m2hr9ge _1m2hr9gd _1fragemzd _1fragemsm _1fragemuq _1fragemyn _1fragemz4 _1fragemz6 _1fragemyv _1fragemux _1m2hr9g1l _1m2hr9g1j _1fragemum _1m2hr9g1d _1m2hr9g1a _1fragemyu _1m2hr9g1v _1m2hr9g1s _1m2hr9g14 _1m2hr9gh _1m2hr9gf _1fragem32 _1m2hr9g1q _1m2hr9g17 _1m2hr9g15 _1fragemvr _1m2hr9g1i']").click()
            print("button is clickable")
        except Exception as e:

            print(" button is NOT clickable")
        time.sleep(15)



    def test_TC_N_014(self):

        driver = self.driver
        driver.get( "https://shop.x.com/")
        delay()

        try:
            driver.find_element(By.XPATH, "//span[@class='h6 link-faded md-max:hidden'][normalize-space()='Search']").click()
            print("Search tab is clickable ")

        except Exception as e:
            print("Search tab is not clickable", e)
            delay()


        try:
            input_field = driver.find_element(By.XPATH,
                                                 "//input[@placeholder='Search...']")
            input_field.clear()
            input_field.send_keys("julia")
            print("input entered")
        except Exception as e:
            print(" input is not entered:", e)
            delay()



    def test_TC_N_015(self):

        driver = self.driver
        driver.get(
            "https://shop.x.com/checkouts/cn/hWNAziRp1LOwYT4jmecKGNhx/en-us/information?_r=AQABRDOlC1yF_Rv-AwTJI9xc2bjCA7VOpzs6xrDnkThTSOU")
        delay()

        try:
            discount_field = driver.find_element(By.XPATH, "//input[@id='ReductionsInput0']")
            discount_field.send_keys("INVALID123")
            print("Discount field field")
        except Exception as e:
            raise Exception(f"Failed to enter discount: {e}")
        time.sleep(3)

        try:
            apply_btn = driver.find_element(By.XPATH, "//button[@aria-label='Apply Discount Code']")
            apply_btn.click()
            print("Apply button clicked")
        except Exception as e:
            raise Exception(f"Failed to click apply button: {e}")



class EdgeXAINegativeTests(unittest.TestCase):

    def setUp(self):
        os.environ[
            "SE_DRIVER_MIRROR_URL"] = "https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/"
        os.environ["SE_CACHE_PATH"] = ""
        options = EdgeOptions()
        # options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_TC_N_011(self):

        driver = self.driver
        try:
            driver.get(" https://x.ai/12345 ")
            print("Invalid URL Navigation")
        except Exception as e:
            print(" xAI main page is opened:", e)
            raise Exception(f"Failed to open xAI home page: {e}")

        time.sleep(3)

    def test_TC_N_012(self):

        driver = self.driver
        driver.get("https://shop.x.com/account/login")
        delay()

        wait = WebDriverWait(driver, 10)

        # Locate fields (adjust locators if UI changes)
        try:
            email_field = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//input[@id='input--template--25407258788123__main--customeremail']")))
            email_field.clear()
            email_field.send_keys("julia@@gmail.com")
            print("email entered")
        except Exception as e:
            print(" email not entered:", e)
            time.sleep(5)

        try:
            password_field = driver.find_element(By.XPATH,
                                                 "//input[@id='input--template--25407258788123__main--customerpassword']")
            password_field.clear()
            password_field.send_keys("12345678")
            print("password entered")
        except Exception as e:
            print(" password not entered:", e)
            time.sleep(5)

        try:
            login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
            login_button.click()
            time.sleep(5)
            print("login button is displayed and clickable")
        except Exception as e:
            print(" login button NOT displayed and clickable")

    def test_TC_N_013(self):

        driver = self.driver
        driver.get(
            "https://shop.x.com/checkouts/cn/hWNAx4Vzpw4vark8usbYIa8H/en-us/information?_r=AQABSS4sFGU7tPHhCpz4xEvrYiykf56xXx01a9FpwTIljwA")
        delay()

        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)
        delay()

        try:
            driver.find_element(By.XPATH,
                                "//button[@class='_1m2hr9ge _1m2hr9gd _1fragemzd _1fragemsm _1fragemuq _1fragemyn _1fragemz4 _1fragemz6 _1fragemyv _1fragemux _1m2hr9g1l _1m2hr9g1j _1fragemum _1m2hr9g1d _1m2hr9g1a _1fragemyu _1m2hr9g1v _1m2hr9g1s _1m2hr9g14 _1m2hr9gh _1m2hr9gf _1fragem32 _1m2hr9g1q _1m2hr9g17 _1m2hr9g15 _1fragemvr _1m2hr9g1i']").click()
            print("button is clickable")
        except Exception as e:

            print(" button is NOT clickable")
        time.sleep(15)

        # try:
        #     error_text = wait.until(EC.presence_of_element_located((By.XPATH, ""))

    def test_TC_N_014(self):

        driver = self.driver
        driver.get("https://shop.x.com/")
        delay()

        try:
            driver.find_element(By.XPATH,
                                "//span[@class='h6 link-faded md-max:hidden'][normalize-space()='Search']").click()
            print("Search tab is clickable ")

        except Exception as e:
            print("Search tab is not clickable", e)
            delay()

        try:
            input_field = driver.find_element(By.XPATH,
                                              "//input[@placeholder='Search...']")
            input_field.clear()
            input_field.send_keys("julia")
            print("input entered")
        except Exception as e:
            print(" input is not entered:", e)
            delay()


    def test_TC_N_015(self):

        driver = self.driver
        driver.get("https://shop.x.com/checkouts/cn/hWNAzrK4gTJlHnzD9ciF03V3/en-us/information?_r=AQABdTxNkK3OFoknrlzJvyAGm-p8LRUDlsfjJ1EjTcTGsZs")
        delay()

        try:
            discount_field = driver.find_element(By.XPATH, "//input[@id='ReductionsInput0']")
            discount_field.send_keys("INVALID123")
            print("Discount field field")
        except Exception as e:
            raise Exception(f"Failed to enter discount: {e}")
        time.sleep(3)

        try:
            apply_btn = driver.find_element(By.XPATH, "//button[@aria-label='Apply Discount Code']")
            apply_btn.click()
            print("Apply button clicked")
        except Exception as e:
            raise Exception(f"Failed to click apply button: {e}")

if __name__ == "__main__":
        unittest.main(AllureReports)
