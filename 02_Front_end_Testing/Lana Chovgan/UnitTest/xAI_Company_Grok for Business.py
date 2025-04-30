import time
import unittest
import random
#import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait

import Helpers_xAI as H

import os
os.environ['WDM_SSL_VERIFY'] = '0'
import warnings
from urllib3.exceptions import InsecureRequestWarning
# Suppress only the single InsecureRequestWarning from urllib3
warnings.filterwarnings("ignore", category=InsecureRequestWarning)
from webdriver_manager.core import driver


from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

from selenium.common import WebDriverException as WDE, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def delay():
    time.sleep(random.randint(3,4))
# This function is for delay() it randomly pics time between 2 and 4 seconds

class ChromeTestsPositive(unittest.TestCase): # This is a class setUp. We will have 3 (chrome,firefox,edge)
    def setUp(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.page_load_strategy = 'eager'
        # options.add_argument("--headless")
        # options.add_argument(
        #     "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_chrome_TC_P_001(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        driver.find_element(By.XPATH, "(//a[@href='/company'])[1]").click()
        delay()

# 3. Verify the presence of the following three unique elements on the page:
#    - "Our Mission" section
        Our_Mission = driver.find_element(By.XPATH, "//span[contains(.,'Our Mission')]")
        if Our_Mission is not None:
            print("Section 'Our Mission' is visible and displayed")
        else:
            print("Section 'Our Mission' is not displayed")

#    -  A page title
        try:
            assert "Company | xAI" in driver.title
            print("Title is correct!")
        except WDE:
            print("Title is wrong! Title is: ", driver.title)

#    - "At our core" section with three columns
        At_our_core = driver.find_element(By.XPATH, "//h2[contains(text(),'At our core')]")
        driver.execute_script("return arguments[0].scrollIntoView(true);", At_our_core)
        if At_our_core:
            print("'At our core' section is displayed on the page")
        else:
            print("'At our core' section is not visible!")

    def test_chrome_TC_P_002(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        H.company_button(driver)

# 3. On the "Company" page, click on the “Join Us” button.
        driver.find_element(By.XPATH, "//a[contains(.,'Join Us')]").click()
        delay()

# 4. Verify that clicking "Join Us" navigates to the correct “Careers” page (check URL, page title, or content to confirm).
        try:
            assert "Careers | xAI" in driver.title
            print("Title is correct!")
        except WDE:
            print("Title is wrong! Title is: ", driver.title)

# content to confirm
        wait = WebDriverWait(driver, 4)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'View Open Roles')])[2]")))
            print ("Button to 'View Open Roles' is visible on the page")
        except NoSuchElementException:
            print("Button 'View Open Roles' not found")

    def test_chrome_TC_P_003(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        H.company_button(driver)

# 3. On the "Company" page, scroll down to the "Our path of progress" section.
        Our_path_of_progress = driver.find_element(By.XPATH, "//h2[contains(text(),'Our path of progress')]")
        driver.execute_script("arguments[0].scrollIntoView();", Our_path_of_progress)

# 4. Hover the mouse over the date “03 Apr” in the timeline event list.
        element_to_hover = driver.find_element(By.XPATH, "(//div[@aria-label='Event entry selector'])[16]")
    # Create an ActionChains object
        actions = ActionChains(driver)
    # Perform the hover action
        actions.move_to_element(element_to_hover).perform()

# 5. Verify that the correct event is displayed: “Grok 3 API” appears in the event details.
        Grok_3_API = driver.find_element(By.XPATH, "//div[@class='no-scrollbar overflow-x-auto']")
        if Grok_3_API is not None:
            print("Section 'Grok_3_API' is visible and displayed")
        else:
            print("Section 'Grok_3_API' is not displayed")

    def test_chrome_TC_P_004(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        H.company_button(driver)

# 3. On the "Company" page, scroll down to the "Collaboration across borders" section.
        Collaboration_across_borders = driver.find_element(By.XPATH, "//h2[contains(.,'Collaboration across borders')]")
        driver.execute_script("arguments[0].scrollIntoView();", Collaboration_across_borders)

# 4. Verify the presence of the globe visual element on the page (animated globe, 3D model).
        Globe = driver.find_element(By.XPATH, "//canvas[contains(@height,'600')]")
        if Globe is not None:
            print("Globe is visible and displayed")
        else:
            print("Globe is not displayed")

    def test_chrome_TC_P_005(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        H.company_button(driver)

        first_window = driver.window_handles[0]

# 3. On the "Company" page, click on the “TRY GROK” button.
        driver.find_element(By.XPATH, "//a[contains(.,'Try Grok')]").click()
        delay()
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
# 4. Verify that clicking “TRY GROK” opens a new browser tab and navigates to the correct page (check URL, page title, or content to confirm)
        try:
            assert "Grok" in driver.title
            print("Title is correct!")
        except WDE:
            print("Title is wrong! Title is: ", driver.title)

        # content to confirm
        wait = WebDriverWait(driver, 3)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@aria-label='Ask Grok anything']")))
            print("Text area is visible and displayed on the page")
        except NoSuchElementException:
            print("Text area not found")

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()

class EdgeTestsPositive(unittest.TestCase):# This is a class setUp. We will have 3 (chrome,firefox,edge)
    def setUp(self):

        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.page_load_strategy = 'eager'
        # options.add_argument("--headless")
        # options.add_argument(
        #     "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_Edge_TC_P_001(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        driver.find_element(By.XPATH, "(//a[@href='/company'])[1]").click()
        delay()

# 3. Verify the presence of the following three unique elements on the page:
#    - "Our Mission" section
        Our_Mission = driver.find_element(By.XPATH, "//span[contains(.,'Our Mission')]")
        if Our_Mission is not None:
            print("Section 'Our Mission' is visible and displayed")
        else:
            print("Section 'Our Mission' is not displayed")

#    -  A page title
        try:
            assert "Company | xAI" in driver.title
            print("Title is correct!")
        except WDE:
            print("Title is wrong! Title is: ", driver.title)

#    - "At our core" section with three columns
        At_our_core = driver.find_element(By.XPATH, "//h2[contains(text(),'At our core')]")
        driver.execute_script("return arguments[0].scrollIntoView(true);", At_our_core)
        if At_our_core:
            print("'At our core' section is displayed on the page")
        else:
            print("'At our core' section is not visible!")

    def test_Edge_TC_P_002(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        H.company_button(driver)

# 3. On the "Company" page, click on the “Join Us” button.
        driver.find_element(By.XPATH, "//a[contains(.,'Join Us')]").click()
        delay()

# 4. Verify that clicking "Join Us" navigates to the correct “Careers” page (check URL, page title, or content to confirm).
        try:
            assert "Careers | xAI" in driver.title
            print("Title is correct!")
        except WDE:
            print("Title is wrong! Title is: ", driver.title)

# content to confirm
        wait = WebDriverWait(driver, 4)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'View Open Roles')])[2]")))
            print ("Button to 'View Open Roles' is visible on the page")
        except NoSuchElementException:
            print("Button 'View Open Roles' not found")

    def test_Edge_TC_P_003(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        H.company_button(driver)

# 3. On the "Company" page, scroll down to the "Our path of progress" section.
        Our_path_of_progress = driver.find_element(By.XPATH, "//h2[contains(text(),'Our path of progress')]")
        driver.execute_script("arguments[0].scrollIntoView();", Our_path_of_progress)

# 4. Hover the mouse over the date “03 Apr” in the timeline event list.
        element_to_hover = driver.find_element(By.XPATH, "(//div[@aria-label='Event entry selector'])[16]")
    # Create an ActionChains object
        actions = ActionChains(driver)
    # Perform the hover action
        actions.move_to_element(element_to_hover).perform()

# 5. Verify that the correct event is displayed: “Grok 3 API” appears in the event details.
        Grok_3_API = driver.find_element(By.XPATH, "//div[@class='no-scrollbar overflow-x-auto']")
        if Grok_3_API is not None:
            print("Section 'Grok_3_API' is visible and displayed")
        else:
            print("Section 'Grok_3_API' is not displayed")

    def test_Edge_TC_P_004(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        H.company_button(driver)

# 3. On the "Company" page, scroll down to the "Collaboration across borders" section.
        Collaboration_across_borders = driver.find_element(By.XPATH, "//h2[contains(.,'Collaboration across borders')]")
        driver.execute_script("arguments[0].scrollIntoView();", Collaboration_across_borders)

# 4. Verify the presence of the globe visual element on the page (animated globe, 3D model).
        Globe = driver.find_element(By.XPATH, "//canvas[contains(@height,'600')]")
        if Globe is not None:
            print("Globe is visible and displayed")
        else:
            print("Globe is not displayed")

    def test_Edge_TC_P_005(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        H.company_button(driver)

        first_window = driver.window_handles[0]

# 3. On the "Company" page, click on the “TRY GROK” button.
        driver.find_element(By.XPATH, "//a[contains(.,'Try Grok')]").click()
        delay()
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
# 4. Verify that clicking “TRY GROK” opens a new browser tab and navigates to the correct page (check URL, page title, or content to confirm)
        try:
            assert "Grok" in driver.title
            print("Title is correct!")
        except WDE:
            print("Title is wrong! Title is: ", driver.title)

        # content to confirm
        wait = WebDriverWait(driver, 3)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@aria-label='Ask Grok anything']")))
            print("Text area is visible and displayed on the page")
        except NoSuchElementException:
            print("Text area not found")

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()

class FifeFoxTestsPositive(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-certificate-errors')
        options.page_load_strategy = 'eager'
        # options.add_argument("--headless")
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_FifeFox_TC_P_001(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        driver.find_element(By.XPATH, "(//a[@href='/company'])[1]").click()
        delay()

# 3. Verify the presence of the following three unique elements on the page:
#    - "Our Mission" section
        Our_Mission = driver.find_element(By.XPATH, "//span[contains(.,'Our Mission')]")
        if Our_Mission is not None:
            print("Section 'Our Mission' is visible and displayed")
        else:
            print("Section 'Our Mission' is not displayed")

#    -  A page title
        try:
            assert "Company | xAI" in driver.title
            print("Title is correct!")
        except WDE:
            print("Title is wrong! Title is: ", driver.title)

#    - "At our core" section with three columns
        At_our_core = driver.find_element(By.XPATH, "//h2[contains(text(),'At our core')]")
        driver.execute_script("return arguments[0].scrollIntoView(true);", At_our_core)
        if At_our_core:
            print("'At our core' section is displayed on the page")
        else:
            print("'At our core' section is not visible!")

    def test_FifeFox_TC_P_002(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        H.company_button(driver)

# 3. On the "Company" page, click on the “Join Us” button.
        driver.find_element(By.XPATH, "//a[contains(.,'Join Us')]").click()
        delay()

# 4. Verify that clicking "Join Us" navigates to the correct “Careers” page (check URL, page title, or content to confirm).
        try:
            assert "Careers | xAI" in driver.title
            print("Title is correct!")
        except WDE:
            print("Title is wrong! Title is: ", driver.title)

# content to confirm
        wait = WebDriverWait(driver, 4)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'View Open Roles')])[2]")))
            print ("Button to 'View Open Roles' is visible on the page")
        except NoSuchElementException:
            print("Button 'View Open Roles' not found")

    def test_FifeFox_TC_P_003(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        H.company_button(driver)

# 3. On the "Company" page, scroll down to the "Our path of progress" section.
        Our_path_of_progress = driver.find_element(By.XPATH, "//h2[contains(text(),'Our path of progress')]")
        driver.execute_script("arguments[0].scrollIntoView();", Our_path_of_progress)

# 4. Hover the mouse over the date “03 Apr” in the timeline event list.
        element_to_hover = driver.find_element(By.XPATH, "(//div[@aria-label='Event entry selector'])[16]")
    # Create an ActionChains object
        actions = ActionChains(driver)
    # Perform the hover action
        actions.move_to_element(element_to_hover).perform()

# 5. Verify that the correct event is displayed: “Grok 3 API” appears in the event details.
        Grok_3_API = driver.find_element(By.XPATH, "//div[@class='no-scrollbar overflow-x-auto']")
        if Grok_3_API is not None:
            print("Section 'Grok_3_API' is visible and displayed")
        else:
            print("Section 'Grok_3_API' is not displayed")

    def test_FifeFox_TC_P_004(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        H.company_button(driver)

# 3. On the "Company" page, scroll down to the "Collaboration across borders" section.
        Collaboration_across_borders = driver.find_element(By.XPATH, "//h2[contains(.,'Collaboration across borders')]")
        driver.execute_script("arguments[0].scrollIntoView();", Collaboration_across_borders)

# 4. Verify the presence of the globe visual element on the page (animated globe, 3D model).
        Globe = driver.find_element(By.XPATH, "//canvas[contains(@height,'600')]")
        if Globe is not None:
            print("Globe is visible and displayed")
        else:
            print("Globe is not displayed")

    def test_FifeFox_TC_P_005(self):
        driver = self.driver
# 1. Open the xAI website (Go to https://x.ai/)
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Click on the "Company" link/button in the header menu.
        H.company_button(driver)

        first_window = driver.window_handles[0]

# 3. On the "Company" page, click on the “TRY GROK” button.
        driver.find_element(By.XPATH, "//a[contains(.,'Try Grok')]").click()
        delay()
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
# 4. Verify that clicking “TRY GROK” opens a new browser tab and navigates to the correct page (check URL, page title, or content to confirm)
        try:
            assert "Grok" in driver.title
            print("Title is correct!")
        except WDE:
            print("Title is wrong! Title is: ", driver.title)

        # content to confirm
        wait = WebDriverWait(driver, 3)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@aria-label='Ask Grok anything']")))
            print("Text area is visible and displayed on the page")
        except NoSuchElementException:
            print("Text area not found")

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()


class ChromeTestsNegative(unittest.TestCase):
    def setUp(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--headless")
        # options.add_argument(
        #     "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        self.driver.maximize_window()

        options.page_load_strategy = 'eager'
        #wait = WebDriverWait(driver, 4)

# This is a class setUp. We will have 3 (chrome,firefox,edge)

    def test_chrome_TC_N_001(self): #Attempt to request access without filling out any required fields
        driver = self.driver

# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Hover the mouse over the “GROK” link/button in the header menu.
        element_to_hover = driver.find_element(By.XPATH, "(//a[contains(.,'Grok')])[1]")
        # Create an ActionChains object
        actions = ActionChains(driver)
        # Perform the hover action
        actions.move_to_element(element_to_hover).perform()
        delay()

# 3. Click on the “FOR BUSINESS” link/button that appears.
        driver.find_element(By.XPATH, "//a[@href='/grok/business']").click()

# 4. Scroll down to the “Request Early Access” form.
        Request_Early_Access = driver.find_element(By.XPATH, "//span[contains(.,'Request early access')]")
        driver.execute_script("arguments[0].scrollIntoView();", Request_Early_Access)

# 5. Without filling out any fields, click the “Request Access” button.
        driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Request access')]").click()
        delay()

# 6. Validate that the system displays the error message
        first_name_field = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
        validation_message = driver.execute_script("return arguments[0].validationMessage;", first_name_field)

        if validation_message=="Please fill out this field":
            print("test_chrome_TC_N_001 PASS")
        else:
            print("test_chrome_TC_N_001 FAIL")

    def test_chrome_TC_N_002(self): # Attempt to request access using an invalid email address
        driver = self.driver
# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

#2. Hover the mouse over the “GROK” link/button in the header menu.
        H.hover_GROK_button(driver)

#3. Click on the “FOR BUSINESS” link/button that appears.
        H.BUSINESS_button(driver)

#4. Scroll down to the “Request Early Access” form.
        H.ScrollDown_Request_Early_Access(driver)

# 5. Fill in the following fields:
#    - First Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Harry")
        delay()
#    - Last Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("Potter")
        delay()
#    - Company Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hogwarts")
        delay()

# 6. In the "Email Address" field, enter an invalid email address (e.g., test@invalid or test.com).
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("test@invalid")
        delay()

# 7. Click the “Request Access” button.
        H.Request_Access(driver)

# 8. Validate that the system displays the error message
        H.alert_2(driver)

    def test_chrome_TC_N_003(self):  # Attempt to request access with the 'Company Name' field containing only whitespace.
        driver = self.driver
# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Hover the mouse over the “GROK” link/button in the header menu.
        H.hover_GROK_button(driver)

# 3. Click on the “FOR BUSINESS” link/button that appears.
        H.BUSINESS_button(driver)

# 4. Scroll down to the “Request Early Access” form.
        H.ScrollDown_Request_Early_Access(driver)

# 5. Fill in the following fields:
#    - First Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Harry")
        delay()
#    - Last Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("Potter")
        delay()
#    - Email Address
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("HarryPotter@Hogwarts.com")
        delay()

# 6. In the "Company Name" field, enter only whitespaces.
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("   ")
        delay()

# 7. Click the “Request Access” button.
        H.Request_Access(driver)

# 8. Validate that the system displays the error message
        H.alert_3(driver)

    def test_chrome_TC_N_004(self):  # Attempt to request access with numeric characters entered in the 'Last Name' field.
        driver = self.driver
# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Hover the mouse over the “GROK” link/button in the header menu.
        H.hover_GROK_button(driver)

# 3. Click on the “FOR BUSINESS” link/button that appears.
        H.BUSINESS_button(driver)

# 4. Scroll down to the “Request Early Access” form.
        H.ScrollDown_Request_Early_Access(driver)

# 5. Fill in the following fields:
#    - First Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Harry")
        delay()
#    - Company Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hogwarts")
        delay()
#    - Email Address
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("HarryPotter@Hogwarts.com")
        delay()

# 6. In the "Last Name" field, enter only numeric characters 155.
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("155")
        delay()

# 7. Click the “Request Access” button.
        H.Request_Access(driver)

# 8. Validate that the system displays the error message
        H.alert_4(driver)

    def test_chrome_TC_N_005(self):  # Attempt to request access with special characters in the 'First Name' field.
        driver = self.driver
# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Hover the mouse over the “GROK” link/button in the header menu.
        H.hover_GROK_button(driver)

# 3. Click on the “FOR BUSINESS” link/button that appears.
        H.BUSINESS_button(driver)

# 4. Scroll down to the “Request Early Access” form.
        H.ScrollDown_Request_Early_Access(driver)

# 5. Fill in the following fields:
#    - Last Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("Potter")
        delay()
#    - Company Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hogwarts")
        delay()
#    - Email Address
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("HarryPotter@Hogwarts.com")
        delay()

# 6. In the "First Name" field, enter only special characters $$%.
        driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("$$%")
        delay()

# 7. Click the “Request Access” button.
        H.Request_Access(driver)

# 8. Validate that the system displays the error message
        H.alert_5(driver)

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()

class EdgeTestsNegative(unittest.TestCase):# This is a class setUp. We will have 3 (chrome,firefox,edge)
    def setUp(self):

        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.page_load_strategy = 'eager'
        # options.add_argument("--headless")
        # options.add_argument(
        #     "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_Edge_TC_N_001(self): #Attempt to request access without filling out any required fields
        driver = self.driver

# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Hover the mouse over the “GROK” link/button in the header menu.
        element_to_hover = driver.find_element(By.XPATH, "(//a[contains(.,'Grok')])[1]")
        # Create an ActionChains object
        actions = ActionChains(driver)
        # Perform the hover action
        actions.move_to_element(element_to_hover).perform()
        delay()

# 3. Click on the “FOR BUSINESS” link/button that appears.
        driver.find_element(By.XPATH, "//a[@href='/grok/business']").click()

# 4. Scroll down to the “Request Early Access” form.
        Request_Early_Access = driver.find_element(By.XPATH, "//span[contains(.,'Request early access')]")
        driver.execute_script("arguments[0].scrollIntoView();", Request_Early_Access)

# 5. Without filling out any fields, click the “Request Access” button.
        driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Request access')]").click()
        delay()

# 6. Validate that the system displays the error message
        first_name_field = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
        validation_message = driver.execute_script("return arguments[0].validationMessage;", first_name_field)

        if validation_message=="Please fill out this field":
            print("test_chrome_TC_N_001 PASS")
        else:
            print("test_chrome_TC_N_001 FAIL")

    def test_Edge_TC_N_002(self): # Attempt to request access using an invalid email address
        driver = self.driver
# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

#2. Hover the mouse over the “GROK” link/button in the header menu.
        H.hover_GROK_button(driver)

#3. Click on the “FOR BUSINESS” link/button that appears.
        H.BUSINESS_button(driver)

#4. Scroll down to the “Request Early Access” form.
        H.ScrollDown_Request_Early_Access(driver)

# 5. Fill in the following fields:
#    - First Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Harry")
        delay()
#    - Last Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("Potter")
        delay()
#    - Company Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hogwarts")
        delay()

# 6. In the "Email Address" field, enter an invalid email address (e.g., test@invalid or test.com).
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("test@invalid")
        delay()

# 7. Click the “Request Access” button.
        H.Request_Access(driver)

# 8. Validate that the system displays the error message
        H.alert_2(driver)

    def test_Edge_TC_N_003(self):  # Attempt to request access with the 'Company Name' field containing only whitespace.
        driver = self.driver
# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Hover the mouse over the “GROK” link/button in the header menu.
        H.hover_GROK_button(driver)

# 3. Click on the “FOR BUSINESS” link/button that appears.
        H.BUSINESS_button(driver)

# 4. Scroll down to the “Request Early Access” form.
        H.ScrollDown_Request_Early_Access(driver)

# 5. Fill in the following fields:
    #    - First Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Harry")
        delay()
    #    - Last Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("Potter")
        delay()
    #    - Email Address
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("HarryPotter@Hogwarts.com")
        delay()

# 6. In the "Company Name" field, enter only whitespaces.
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("   ")
        delay()

# 7. Click the “Request Access” button.
        H.Request_Access(driver)

# 8. Validate that the system displays the error message
        H.alert_3(driver)

    def test_Edge_TC_N_004(self):  # Attempt to request access with numeric characters entered in the 'Last Name' field.
        driver = self.driver
# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Hover the mouse over the “GROK” link/button in the header menu.
        H.hover_GROK_button(driver)

# 3. Click on the “FOR BUSINESS” link/button that appears.
        H.BUSINESS_button(driver)

# 4. Scroll down to the “Request Early Access” form.
        H.ScrollDown_Request_Early_Access(driver)

# 5. Fill in the following fields:
    #    - First Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Harry")
        delay()
    #    - Company Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hogwarts")
        delay()
    #    - Email Address
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("HarryPotter@Hogwarts.com")
        delay()

# 6. In the "Last Name" field, enter only numeric characters 155.
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("155")
        delay()

# 7. Click the “Request Access” button.
        H.Request_Access(driver)

# 8. Validate that the system displays the error message
        H.alert_4(driver)

    def test_Edge_TC_N_005(self):  # Attempt to request access with special characters in the 'First Name' field.
        driver = self.driver
# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Hover the mouse over the “GROK” link/button in the header menu.
        H.hover_GROK_button(driver)

# 3. Click on the “FOR BUSINESS” link/button that appears.
        H.BUSINESS_button(driver)

# 4. Scroll down to the “Request Early Access” form.
        H.ScrollDown_Request_Early_Access(driver)

# 5. Fill in the following fields:
#    - Last Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("Potter")
        delay()
#    - Company Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hogwarts")
        delay()
#    - Email Address
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("HarryPotter@Hogwarts.com")
        delay()

# 6. In the "First Name" field, enter only special characters $$%.
        driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("$$%")
        delay()

# 7. Click the “Request Access” button.
        H.Request_Access(driver)

# 8. Validate that the system displays the error message
        H.alert_5(driver)

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()

class FifeFoxTestsNegative(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-certificate-errors')
        options.page_load_strategy = 'eager'
        # options.add_argument("--headless")
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_FifeFox_TC_N_001(self): #Attempt to request access without filling out any required fields
        driver = self.driver

# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Hover the mouse over the “GROK” link/button in the header menu.
        element_to_hover = driver.find_element(By.XPATH, "(//a[contains(.,'Grok')])[1]")
        # Create an ActionChains object
        actions = ActionChains(driver)
        # Perform the hover action
        actions.move_to_element(element_to_hover).perform()
        delay()

# 3. Click on the “FOR BUSINESS” link/button that appears.
        driver.find_element(By.XPATH, "//a[@href='/grok/business']").click()

# 4. Scroll down to the “Request Early Access” form.
        Request_Early_Access = driver.find_element(By.XPATH, "//span[contains(.,'Request early access')]")
        driver.execute_script("arguments[0].scrollIntoView();", Request_Early_Access)

# 5. Without filling out any fields, click the “Request Access” button.
        driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Request access')]").click()
        delay()

# 6. Validate that the system displays the error message
        first_name_field = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
        validation_message = driver.execute_script("return arguments[0].validationMessage;", first_name_field)

        if validation_message=="Please fill out this field":
            print("test_chrome_TC_N_001 PASS")
        else:
            print("test_chrome_TC_N_001 FAIL")

    def test_FifeFox_TC_N_002(self): # Attempt to request access using an invalid email address
        driver = self.driver
# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

#2. Hover the mouse over the “GROK” link/button in the header menu.
        H.hover_GROK_button(driver)

#3. Click on the “FOR BUSINESS” link/button that appears.
        H.BUSINESS_button(driver)

#4. Scroll down to the “Request Early Access” form.
        H.ScrollDown_Request_Early_Access(driver)

# 5. Fill in the following fields:
#    - First Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Harry")
        delay()
#    - Last Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("Potter")
        delay()
#    - Company Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hogwarts")
        delay()

# 6. In the "Email Address" field, enter an invalid email address (e.g., test@invalid or test.com).
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("test@invalid")
        delay()

# 7. Click the “Request Access” button.
        H.Request_Access(driver)

# 8. Validate that the system displays the error message
        H.alert_2(driver)

    def test_FifeFox_TC_N_003(self):  # Attempt to request access with the 'Company Name' field containing only whitespace.
        driver = self.driver
# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Hover the mouse over the “GROK” link/button in the header menu.
        H.hover_GROK_button(driver)

# 3. Click on the “FOR BUSINESS” link/button that appears.
        H.BUSINESS_button(driver)

# 4. Scroll down to the “Request Early Access” form.
        H.ScrollDown_Request_Early_Access(driver)

# 5. Fill in the following fields:
    #    - First Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Harry")
        delay()
    #    - Last Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("Potter")
        delay()
    #    - Email Address
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("HarryPotter@Hogwarts.com")
        delay()

# 6. In the "Company Name" field, enter only whitespaces.
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("   ")
        delay()

# 7. Click the “Request Access” button.
        H.Request_Access(driver)

# 8. Validate that the system displays the error message
        H.alert_3(driver)

    def test_FifeFox_TC_N_004(self):  # Attempt to request access with numeric characters entered in the 'Last Name' field.
        driver = self.driver
# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Hover the mouse over the “GROK” link/button in the header menu.
        H.hover_GROK_button(driver)

# 3. Click on the “FOR BUSINESS” link/button that appears.
        H.BUSINESS_button(driver)

# 4. Scroll down to the “Request Early Access” form.
        H.ScrollDown_Request_Early_Access(driver)

# 5. Fill in the following fields:
    #    - First Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Harry")
        delay()
    #    - Company Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hogwarts")
        delay()
    #    - Email Address
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("HarryPotter@Hogwarts.com")
        delay()

# 6. In the "Last Name" field, enter only numeric characters 155.
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("155")
        delay()

# 7. Click the “Request Access” button.
        H.Request_Access(driver)

# 8. Validate that the system displays the error message
        H.alert_4(driver)

    def test_FifeFox_TC_N_005(self):  # Attempt to request access with special characters in the 'First Name' field.
        driver = self.driver
# 1. Open the xAI website.
        driver.get("https://x.ai/")
        time.sleep(4)

# 2. Hover the mouse over the “GROK” link/button in the header menu.
        H.hover_GROK_button(driver)

# 3. Click on the “FOR BUSINESS” link/button that appears.
        H.BUSINESS_button(driver)

# 4. Scroll down to the “Request Early Access” form.
        H.ScrollDown_Request_Early_Access(driver)

# 5. Fill in the following fields:
#    - Last Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("Potter")
        delay()
#    - Company Name
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hogwarts")
        delay()
#    - Email Address
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("HarryPotter@Hogwarts.com")
        delay()

# 6. In the "First Name" field, enter only special characters $$%.
        driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("$$%")
        delay()

# 7. Click the “Request Access” button.
        H.Request_Access(driver)

# 8. Validate that the system displays the error message
        H.alert_5(driver)

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()