import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import string

# Constants (URL and Locators)
URL = "https://x.ai/"
OVR_URL="https://x.ai/api#capabilities"
PRC_URL="https://x.ai/api#pricing"
DOC_URL="https://docs.x.ai/docs/overview"


#locators
API_LOCATOR = "(//a[@href='/api'])[1]"
overview_locator = "//a[@href='/api#capabilities']"
PRICING_LOCATOR = "(//a[@target='_blank'])[1]"
DOCUMENTATION_LOCATOR = "(//a[@target='_blank'])[1]"
CALCULATOR_LOCATOR = "//h2[contains(.,'Cost calculator')]"
FIELD_INPUT1 = "//input[@id='text-input']"
FIELD_INPUT2 ="(//input[@type='text'])[2]"
FIELD_INPUT3 ="(//input[@type='text'])[3]"
RESET_BUTTON = "//button[contains(.,'Reset')]"
COST_CALC_LOCATOR = "//h2[contains(.,'Cost calculator')]"
SEARCH_BAR = "(//div[contains(.,'Ctrl+K')])[4]"
SEARCH_BAR_2 = "//input[@placeholder='Search documentation...']"
EXP_DOC_TITLE ="Models and Pricing | xAI Docs"
HOME_LOGO = "/html[1]/body[1]/header[1]/div[3]/nav[1]/a[1]/*[name()='svg'][1]/*[name()='path'][1]"
HOME_LOGO2 ="//a[@class='flex items-center']//span[@class='inline-flex items-center justify-center p-0 m-0']//*[name()='svg']//*[name()='path' and contains(@d,'m3.005 8.8')]"
#sliders
slider1 ="(//input[@min='0'])[1]"
slider2= "(//input[@min='0'])[2]"
slider3="(//input[@min='0'])[3]"


# Helper Functions

# data entry

# generates and inserts a random number
def random_number(driver, by, value, min_value=0, max_value=1000000, timeout=10):
    try:
        input_field = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by,value)))
        random_number= random.randint(min_value, max_value)
        print(f"generated number :{random_number}")
        #clearirng field and typing IN
        input_field.clear()
        input_field.send_keys(str(random_number))
        time.sleep(2)

        return random_number
    except Exception as e:
        print(f"An error occurred while entering the random number: {e}")
        raise
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

def wait_for_element(driver, by, value,):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((by, value))
    )
    print(" Waited for element successfully")
    return element


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

# hovering/clicking/scrolling

def hover_over_element(driver, by, value):

    try:
        element = driver.find_element(by, value)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
    except NoSuchElementException:
        print(f"Element with locator {value} not found!")
        raise


def click_on_elem(driver, by, value):

    try:
        elem = driver.find_element(by, value)
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

def switch_to_new_tab(driver, expected_title=None):

    # Get all open window handles
    windows = driver.window_handles

    # Check if there is more than one tab open
    if len(windows) > 1:
        # Switch to the new tab (second window handle)
        driver.switch_to.window(windows[1])
        print(f"Switched to new tab. Title: {driver.title}")

        # Validate the title if provided
        if expected_title:
            assert expected_title in driver.title, (
                f"Unexpected title in new tab. Expected: '{expected_title}', Actual: '{driver.title}'"
            )
            print("Successfully validated the title of the new tab.")
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

    except Exception as e:
        print(f"An error occurred while validating the Home button: {e}")
        raise


def boundary_test (driver, by, value, expected_max, expected_min,timeout=10):
    field = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )
    try:
        print("tetsing minimum value")
        field.clear()
        field.send_keys(str(expected_min))
        actual = field.get_attribute("value")
        assert actual == str(expected_min), f"Expected min '{expected_min}', got '{actual}'"
        print(f" Min test passed: {expected_min}")
        field.clear()
        field.send_keys(str(expected_min + 1))
        above_actual= field.get_attribute("value")
        assert above_actual == str(expected_min + 1), f"expected '{above_actual}', got'{actual}'"
    except Exception as e:
        print(f"an error occurred while testing min value :{e}")

    try:
        print("testing below minimum")
        field.clear()
        field.send_keys(str(expected_min) + "1" + Keys.LEFT + "-")
        actual = field.get_attribute("value")
        assert actual == "" or actual == str(expected_min), f"Invalid input accepted: {actual}"
        print(f"Below-min test passed: {expected_min - 1}")
    except Exception as e:
        print(f"an error occured during below minimum testing")

    try:
        print("testing maximum value")
        field.clear()
        field.send_keys(str(expected_max))
        actual = field.get_attribute("value")
        assert actual == str(expected_max), f"Expected max '{expected_max}', got '{actual}'"
        print(f" Max test passed: {expected_max}")
    except Exception as e:
        print(f"Maximum value is not as expected :{e}")

    try:
        print("tetsing above/below maximum")
        field.clear()
        field.send_keys(str(expected_max + 1))
        field.send_keys(str(expected_max - 1))
        actual = field.get_attribute("value")
        assert actual == "" or actual == str(expected_max), f"Invalid input accepted: {actual}"
        print(f"Above-max test passed: {expected_max + 1}; Below_max tested:{expected_max - 1}")
    except Exception as e:
        print(f"an error:{e}")

    try:
        print("mid value testing")
        mid = (expected_min + expected_max) // 2
        field.clear()
        field.send_keys(str(mid))
        actual = field.get_attribute("value")
        assert actual == str(mid), f"Expected mid '{mid}', got '{actual}'"
        print(f" Mid-range test passed: {mid}")
    except Exception as e:
        print(f"an error occurred {e}")

def space_input(driver, by, value, space_count=100):
    try:
        field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
        field.clear()
        for _ in range(space_count):
            field.send_keys(Keys.SPACE)
            # validating values and count
        final_value = field.get_attribute("value")
        assert len(final_value) == space_count, f"Expected {space_count} spaces, got {len(final_value)}"
        print(f" if  {space_count} spaces entered one at a time - test failed ")

    except Exception as e:
        print(f" Test failed: {str(e)}")
        driver.save_screenshot("space_test_failure.png")
        raise

















