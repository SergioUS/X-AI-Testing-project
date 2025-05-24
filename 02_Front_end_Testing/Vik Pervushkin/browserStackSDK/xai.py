import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:\\webdriver\\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)
driver.maximize_window()

try:
    print("Verifying clickability of all API modules")
    driver.get("https://x.ai/")
    print("Page loaded")

    # Optional: Hover over API link (only if present)
    try:
        api_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//a[@href='/api'])[1]"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(api_element).perform()
        print("Hovered over API menu")
    except (TimeoutException, NoSuchElementException):
        print("API menu not found or failed to hover - skipping hover step")

    modules = [
        ("Overview", "//a[@href='/api#capabilities']") ]

    original_window = driver.current_window_handle

    for name, locator in modules:
        print(f"Testing '{name}' with locator: {locator}")

        try:
            # Wait for element to be clickable
            module_element = wait.until(
                EC.element_to_be_clickable((By.XPATH, locator))
            )


            for attempt in range(3):
                try:
                    module_element.click()
                    print(f" Clicked on '{name}'")
                    break
                except ElementClickInterceptedException:
                    print(f"Click intercepted on '{name}', retrying with JS...")
                    driver.execute_script("arguments[0].click();", module_element)
                    print(f" JS-clicked on '{name}'")
                    break
            else:
                print(f" Failed to click '{name}' after multiple attempts")
                continue


            time.sleep(2)  # Small pause before next action

        except Exception as e:
            print(f"Error while testing '{name}': {str(e)}\n")
            driver.switch_to.window(original_window)

finally:
    driver.quit()
    print("Browser closed")

