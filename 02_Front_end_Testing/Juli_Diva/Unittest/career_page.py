from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CareersPage:
        def __init__(self, driver, url):
            self.driver = driver
            self.url = url

        # Locators
        VIEW_OPEN_ROLES_BTN = (By.XPATH,
                               "//a[@href='/careers/open-roles' and .//span[normalize-space()='View Open Roles']]")
        # office London ,UK
        OFFICE_FILTER = (By.XPATH, "//span[text()='london, uk']")
        # department Engineering
        DEPARTMENT_FILTER = (By.XPATH, "//span[text()='Engineering']")
        # scroll to Featured section
        FEATURED_ROLES_SECTION = (By.XPATH, "//h2[text()='Featured roles']")
        CLICK_ROLE = (By.XPATH, "(//span[contains(@class, 'line-clamp-1')])[1]")
        # scroll to Interview Process section
        INTERVIEW_PROCESS_SECTION = (By.XPATH, "//h2[text()='Interview process']")
        APPLY_NOW_BTN = (By.XPATH, "//a[normalize-space()='Apply Now' or .='Apply Now']")
        # scroll to Collaboration across borders section
        COLLAB_ACROSS_BORDERS_SECTION = (By.XPATH, "//h2[text()='Collaboration across borders']")
        VIEW_OPEN_ROLES_COLLAB_BTN = (By.XPATH, "//a[text()='View Open Roles']")
        # Search bar in Open Roles section
        SEARCH_BAR = (By.XPATH, "//input[@type='text']")
        CLEAR_ALL_BTN = (By.XPATH, "//button[normalize-space()='Clear all']")
        BACK_TO_JOBS_BTN = (By.XPATH, "//a[normalize-space()='Back to jobs']")
        SEARCH_NOT_FOUND = (By.XPATH, "//p[contains(text(), 'No results found')]")
        COMMAND_LINE = (By.ID, "command_line")

        # Methods PositiveTC
        def open(self):
            self.driver.get(self.url)

        # TC_021
        def click_view_open_roles(self):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.VIEW_OPEN_ROLES_BTN)).click()

        # TC_022
        def click_office_filter(self):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.OFFICE_FILTER)).click()

        def click_department_filter(self):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.DEPARTMENT_FILTER)).click()

        # TC_023
        def scroll_to_featured_roles(self):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.FEATURED_ROLES_SECTION))

        def click_first_featured_role(self):
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.CLICK_ROLE)
            )
            self.driver.execute_script("arguments[0].click();", element)

        # TC_024
        def scroll_to_interview_process(self):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.INTERVIEW_PROCESS_SECTION))

        def click_apply_now(self):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.APPLY_NOW_BTN)).click()

        # TC_025
        def scroll_to_collab_section(self):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.COLLAB_ACROSS_BORDERS_SECTION))

        def click_view_open_roles_collab(self):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.VIEW_OPEN_ROLES_COLLAB_BTN)).click()

            # Methods NegativeTC
            # TC_026

        def clear_all_search(self):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CLEAR_ALL_BTN)).click()

            # TC_027

        def search_for_term(self, term):
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SEARCH_BAR))
            self.driver.find_element(*self.SEARCH_BAR).click()
            self.driver.find_element(*self.SEARCH_BAR).clear()
            self.driver.find_element(*self.SEARCH_BAR).send_keys(term)

        # TC_028
        def invalid_careers_subpage(self):
            self.driver.get("https://x.ai/careers/fake-page")

        # TC_029
        def click_back_to_jobs(self):
            self.driver.switch_to.window(self.driver.window_handles[-1])
            btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.BACK_TO_JOBS_BTN)
            )
            btn.click()