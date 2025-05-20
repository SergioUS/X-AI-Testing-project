import time
import random
from pkgutil import extend_path

import self
from selenium.common import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common import WebDriverException as WDE

# Constants (URL and Locators)
URL = "https://x.ai/"
OVR_URL="https://x.ai/api#capabilities"
PRC_URL="https://x.ai/api#pricing"
DOC_URL="https://docs.x.ai/docs/overview"

#header locators
API_LOCATOR = "(//a[@href='/api'])[1]"
overview_locator = "//a[@href='/api#capabilities']"
PRICING_LOCATOR = "(//a[@target='_blank'])[1]"
DOCUMENTATION_LOCATOR = "(//a[@target='_blank'][contains(.,'Documentation')])[1]"
CALCULATOR_LOCATOR = "//h2[contains(.,'Cost calculator')]"

#field input and buttons
TEXT_INPUT1 = "//input[@id='text-input']"
TEXT_INPUT2 ="(//input[@type='text'])[2]"
TEXT_INPUT3 ="(//input[@type='text'])[3]"
RESET_BUTTON = "//button[contains(.,'Reset')]"
COST_CALC_LOCATOR = "//h2[contains(.,'Cost calculator')]"
SEARCH_BAR = "(//div[contains(.,'Ctrl+K')])[4]"
SEARCH_BAR_2 = "//input[@placeholder='Search documentation...']"

#logos
EXP_DOC_TITLE ="Overview | xAI Docs"
HOME_LOGO = "/html[1]/body[1]/header[1]/div[3]/nav[1]/a[1]/*[name()='svg'][1]/*[name()='path'][1]"
HOME_LOGO2 ="//a[@class='flex items-center']//span[@class='inline-flex items-center justify-center p-0 m-0']//*[name()='svg']//*[name()='path' and contains(@d,'m3.005 8.8')]"



# Helper Functions

# data entry

# generates and inserts a random number
def random_number(driver, by, value, min_value=0, max_value=1000000):
    try:
        #waiting for calculator cost to appear on the screen
        input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by,value)))
        random_num = random.randint(min_value, max_value)
        #clearing field
        input_field.clear()
        input_field.send_keys(str(random_num))
        field_value = input_field.get_attribute("value")
        # assertion if random number was accepted
        assert field_value.strip, f"input field received '{value}'"
        return random_number
    except NoSuchElementException as s_e:
        print(f"An error occurred while entering the random number: {s_e}")
    except AssertionError as a_e:
        print(f"An error occurred while entering the random number: {a_e}")

    # except WebDriverException as wde:
    #     print(f"An error occurred while entering the random number: {wde}")




# enters desired data
def enter_data(driver, by, value, data_to_enter, timeout=10):
    try:
        # wait til elements becomes visible
        elem = driver.find_element(by, value)
        elem.click()
        # clear field and enter any data
        elem.clear()
        elem.send_keys(str(data_to_enter))
        print(f"Entered data:{data_to_enter}")
        # to slow things down
        time.sleep(5)
    except Exception as e:
        print(f"Unexpected error while entering data: {e}")
        raise



# waiting/assertions/presence

def wait_for_element(driver, by, value, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((by, value)))
print("waited for it")

def is_element_present(driver, by, value):
    try:
        driver.find_element(by, value)
        print(f"Element with locator {value} is present.")
        return True
    except NoSuchElementException:
        print(f"Element with locator {value} is not present.")
        return False


def check_url(driver, expected_url, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.url_to_be(expected_url))
        print(f"URL matched: {driver.current_url}")
    except Exception:
        actual_url = driver.current_url
        raise AssertionError(f"URL mismatch! Expected: {expected_url}, Actual: {actual_url}")


def check_element_present(driver, by, value):

    if not driver.find_elements(by, value):
        raise AssertionError(f"Element with locator {value} is not present!")

# hovering/clicking/scrolling

def hover_over_element(driver, by, value):

    try:
        element = WebDriverWait(driver,10).until(EC.visibility_of_element_located((by,value)))
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
    except NoSuchElementException:
        print(f"Element with locator {value} not found!")



def click_on_elem(driver, by, value):

    try:
        elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((by, value)))
        elem.click()
    except NoSuchElementException:
        print(f"Element with locator {value} not found or not clickable")

        time.sleep(5)
        raise



def scroll_down(driver, by, value, pause_duration=2, timeout=10):
    try:
        # Wait for the element to be present in the DOM
        target_element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

        # Scroll the element into view using JavaScript
        driver.execute_script("arguments[0].scrollIntoView(true);", target_element)

        # Pause to simulate scrolling completion or data entry
        time.sleep(pause_duration)

        # Optionally, return the element for further interaction
        return target_element

    except Exception as e:
        print(f"An error occurred while scrolling to the element: {e}")
        raise





#window hub

def switch_to_new_tab(driver, expected_url):

    # Get all open window handles
    windows = driver.window_handles

    # Check if there is more than one tab open
    if len(windows) > 1:
        # Switch to the new tab (second window handle)
        driver.switch_to.window(windows[1])
        current_url = driver.current_url
        print(f"Switched to new tab. URL: {driver.current_url}")

        # Wait and validate if URL  provided
        if expected_url:
            WebDriverWait(driver, 10).until(EC.url_to_be(expected_url),
            message=f"Expected URL '{expected_url}' found in new tab")
            print("URL validated")
        else:
            raise Exception("No new tab was opened.")

def validate_home_button(driver, module_url, URL):
    try:

        driver.get(module_url)
        print(f"Navigated to module: {module_url}")

        # check if the home button exists
        home_buttons = driver.find_elements(By.XPATH, HOME_LOGO)
        if len(home_buttons) > 0:
            # Home button exists, click it
            print("Home button found. Clicking the Home button.")
            home_buttons[0].click()
        else:
        # another button (e.g., a logo or Back button)
            fallback_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, HOME_LOGO2))
            )
            print("Home button not found. Clicking the fallback button.")
            fallback_button.click()

        # Wait for the URL to change to the main page URL
        WebDriverWait(driver, 10).until(EC.url_to_be(URL))
        print(f"Redirected to main page: {driver.current_url}")

        # Assert that the current URL matches the expected main page URL
        assert driver.current_url == URL, (
            f"Expected URL: {URL}, but got: {driver.current_url}"
        )

    except WDE:
        print(f"Error the logo button on '{driver.current_url}' isn't clickable ")


def switch_new_tab(driver, main_url, current_url):

    # Get all open window handles
    windows = driver.window_handles


    # Check if there is more than one tab open
    if len(windows) > 1:
        # Switch to the new tab (second window handle)
        driver.switch_to.window(windows[1])
        current_url = driver.current_url
        print(f"Switched to new tab. URL: {driver.current_url}")

        # Wait and validate if URL  provided
        if current_url:
            WebDriverWait(driver, 10).until(EC.url_to_be(current_url),
            message=f"Expected URL '{current_url}' found in new tab")
            print("URL validated")
            driver.get(main_url)
        else:
            raise Exception("No new tab was opened.")








