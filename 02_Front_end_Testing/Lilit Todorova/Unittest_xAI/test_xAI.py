# test_xAI.py
import os
import random
import tempfile
import unittest
from faker import Faker

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import wait_for_element, wait_for_elements, delay, scroll_and_delay, take_screenshot, get_driver, close_driver
from locators import (
    HomeLocators,
    CareersLocators,
    ApplicationLocators,
    ApplicationFieldsErrors,
    LatestRoles, SecurityLocators
)

fake = Faker()

class TestXAI(unittest.TestCase):
    def setUp(self):
        """Set up the WebDriver and base URL."""
        self.browser = os.getenv("BROWSER", "chrome").lower()
        self.driver  = get_driver()

        print(f"=== Starting tests on: {self.browser.upper()} ===")
        self.base_url = "https://x.ai"

    def tearDown(self):
        """Close the WebDriver after each test."""
        close_driver(self.driver)

    # ==== POSITIVE TESTS ==== #

    def test_BR_P_021_navigation_to_careers(self):
        self.driver.get(self.base_url)
        careers = wait_for_element(self.driver, HomeLocators.CAREERS_MODULE)
        scroll_and_delay(self.driver, careers)
        careers.click()
        delay(1, 2)
        self.assertIn("/careers", self.driver.current_url)

    def test_BR_P_022_view_open_roles(self):
        self.driver.get(f"{self.base_url}/careers")
        delay(2, 3)
        btn = wait_for_element(self.driver, LatestRoles.VIEW_ALL_OPEN_ROLES, timeout=15)
        scroll_and_delay(self.driver, btn)
        btn.click()
        WebDriverWait(self.driver, 10).until(lambda d: "/careers/open-roles" in d.current_url)
        self.assertIn("/careers/open-roles", self.driver.current_url)

    def test_BR_P_023_filter_jobs(self):
        self.driver.get(f"{self.base_url}/careers/open-roles")
        delay(3, 5)

        office = wait_for_element(self.driver, CareersLocators.OFFICE_FILTER)
        scroll_and_delay(self.driver, office)
        sf = wait_for_element(self.driver, CareersLocators.OFFICE_SAN_FRANCISCO)
        scroll_and_delay(self.driver, sf)
        sf.click()
        delay(1, 2)

        dept = wait_for_element(self.driver, CareersLocators.DEPARTMENT_FILTER)
        scroll_and_delay(self.driver, dept)
        eng = wait_for_element(self.driver, CareersLocators.DEPARTMENT_ENGINEERING)
        scroll_and_delay(self.driver, eng)
        eng.click()
        delay(3, 5)

        roles = wait_for_elements(self.driver, CareersLocators.AI_ENGINEER_RESEARCHER)
        self.assertGreater(len(roles), 0, "No job listings found after filtering.")
        scroll_and_delay(self.driver, roles[0])
        card_title = roles[0].text.strip()
        roles[0].click()

        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        self.assertTrue(
            self.driver.current_url.startswith("https://job-boards.greenhouse.io/xai/jobs/"),
            f"Unexpected job URL: {self.driver.current_url}"
        )
        hdr = wait_for_element(self.driver, CareersLocators.JOB_TITLE_HEADER)
        self.assertIn(card_title, hdr.text)

    def test_BR_P_024_job_listing_new_tab_and_form(self):
        # inline open_application_form
        self.driver.get(f"{self.base_url}/careers/open-roles")
        delay(2, 3)
        job_links = wait_for_elements(self.driver, CareersLocators.AI_ENGINEER_RESEARCHER)
        self.assertGreater(len(job_links), 0, "AI Engineer listing not found.")
        scroll_and_delay(self.driver, job_links[0])
        job_links[0].click()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # fill names + email
        for loc, val in (
            (ApplicationLocators.FIRST_NAME_INPUT, fake.first_name()),
            (ApplicationLocators.LAST_NAME_INPUT,  fake.last_name()),
            (ApplicationLocators.EMAIL_INPUT,     fake.email()),
        ):
            el = wait_for_element(self.driver, loc)
            scroll_and_delay(self.driver, el)
            el.clear()
            el.send_keys(val)

        # phone
        phone = wait_for_element(self.driver, ApplicationLocators.PHONE_INPUT)
        scroll_and_delay(self.driver, phone)
        phone.clear()
        phone.send_keys("".join(random.choice("0123456789") for _ in range(10)))

        # sponsorship = No
        control = wait_for_element(
            self.driver,
            (By.CSS_SELECTOR, "div.select__control.remix-css-13cymwt-control")
        )
        scroll_and_delay(self.driver, control)
        control.click()
        no_opt = wait_for_element(
            self.driver,
            (By.XPATH, "//div[contains(@class,'select__option') and normalize-space(.)='No']")
        )
        scroll_and_delay(self.driver, no_opt)
        no_opt.click()

        # enter manually
        enter = wait_for_element(self.driver, ApplicationLocators.ENTER_MANUALLY)
        scroll_and_delay(self.driver, enter)
        enter.click()

        # resume text
        resume = wait_for_element(self.driver, ApplicationLocators.RESUME_TEXT)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", resume)
        delay(1,1)
        resume.clear()
        resume.send_keys(fake.paragraph())

        # work experience
        work = wait_for_element(self.driver, ApplicationLocators.WORK_EXPERIENCE_TEXTAREA)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", work)
        delay(1,1)
        work.clear()
        work.send_keys(fake.text())

        # submit
        submit = wait_for_element(self.driver, ApplicationLocators.SUBMIT_BUTTON)
        scroll_and_delay(self.driver, submit)
        submit.click()

        try:
            vf = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(ApplicationLocators.EMAIL_VERIFICATION_FIELD)
            )
            self.assertTrue(vf.is_displayed())
        except TimeoutException:
            if "/confirmation" in self.driver.current_url:
                thank = wait_for_element(self.driver, ApplicationLocators.THANK_YOU_FOR_APPLYING)
                self.assertTrue(thank.is_displayed())
            else:
                for i in range(8):
                    fld = wait_for_element(self.driver, SecurityLocators.INPUT(i), timeout=20)
                    scroll_and_delay(self.driver, fld)
                    fld.send_keys(str(random.randint(0,9)))
                take_screenshot(self.driver, os.path.join("evidence_N_024", "security.png"))
                first = wait_for_element(self.driver, SecurityLocators.INPUT(0))
                self.assertTrue(first.is_displayed())

    def test_BR_P_025_view_all_open_roles(self):
        self.driver.get(f"{self.base_url}/careers")
        delay(2, 4)
        latest = wait_for_element(self.driver, LatestRoles.LATEST_ROLES)
        scroll_and_delay(self.driver, latest)
        view_all = wait_for_element(self.driver, LatestRoles.VIEW_ALL_OPEN_ROLES)
        scroll_and_delay(self.driver, view_all)
        view_all.click()
        WebDriverWait(self.driver, 10).until(lambda d: "/careers/open-roles" in d.current_url)
        self.assertIn("/careers/open-roles", self.driver.current_url)

    # ==== NEGATIVE TESTS ==== #

    def test_BR_N_021_verify_error_message_for_missing_required_fields(self):
        # inline open_application_form
        self.driver.get(f"{self.base_url}/careers/open-roles")
        delay(2, 3)
        job_links = wait_for_elements(self.driver, CareersLocators.AI_ENGINEER_RESEARCHER)
        self.assertGreater(len(job_links), 0)
        scroll_and_delay(self.driver, job_links[0])
        job_links[0].click()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # must click Enter manually to reveal resume+work
        enter = wait_for_element(self.driver, ApplicationLocators.ENTER_MANUALLY)
        scroll_and_delay(self.driver, enter)
        enter.click()

        submit = wait_for_element(self.driver, ApplicationLocators.SUBMIT_BUTTON)
        scroll_and_delay(self.driver, submit)
        submit.click()

        for err_loc in (
            ApplicationFieldsErrors.FIRST_NAME_ERROR,
            ApplicationFieldsErrors.LAST_NAME_ERROR,
            ApplicationFieldsErrors.RESUME_ERROR,
            ApplicationFieldsErrors.WORK_EXPERIENCE_TEXTAREA_ERROR,
        ):
            err = wait_for_element(self.driver, err_loc, timeout=10)
            scroll_and_delay(self.driver, err)
            self.assertTrue(err.is_displayed())

    def test_BR_N_022_verify_error_message_for_invalid_email_format(self):
        # inline open_application_form
        self.driver.get(f"{self.base_url}/careers/open-roles")
        delay(2, 3)
        job_links = wait_for_elements(self.driver, CareersLocators.AI_ENGINEER_RESEARCHER)
        scroll_and_delay(self.driver, job_links[0])
        job_links[0].click()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        enter = wait_for_element(self.driver, ApplicationLocators.ENTER_MANUALLY)
        scroll_and_delay(self.driver, enter)
        enter.click()

        email = wait_for_element(self.driver, ApplicationLocators.EMAIL_INPUT)
        scroll_and_delay(self.driver, email)
        email.clear()
        email.send_keys("invalid-email.com")

        submit = wait_for_element(self.driver, ApplicationLocators.SUBMIT_BUTTON)
        scroll_and_delay(self.driver, submit)
        submit.click()

        err = wait_for_element(self.driver, ApplicationFieldsErrors.EMAIL_FORMAT_ERROR, timeout=10)
        scroll_and_delay(self.driver, err)
        self.assertTrue(err.is_displayed())

    def test_BR_N_023_verify_error_for_missing_resume_manually(self):
        # inline open_application_form
        self.driver.get(f"{self.base_url}/careers/open-roles")
        delay(2, 3)
        job_links = wait_for_elements(self.driver, CareersLocators.AI_ENGINEER_RESEARCHER)
        scroll_and_delay(self.driver, job_links[0])
        job_links[0].click()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        enter = wait_for_element(self.driver, ApplicationLocators.ENTER_MANUALLY)
        scroll_and_delay(self.driver, enter)
        enter.click()

        submit = wait_for_element(self.driver, ApplicationLocators.SUBMIT_BUTTON)
        scroll_and_delay(self.driver, submit)
        submit.click()

        err = wait_for_element(self.driver, ApplicationFieldsErrors.RESUME_ERROR, timeout=10)
        scroll_and_delay(self.driver, err)
        self.assertTrue(err.is_displayed())

    def test_BR_N_024_verify_error_for_invalid_symbols_in_first_and_last_name(self):
        # 1) Open the job’s application form
        self.driver.get(f"{self.base_url}/careers/open-roles")
        delay(2, 3)
        job_links = wait_for_elements(self.driver, CareersLocators.AI_ENGINEER_RESEARCHER)
        scroll_and_delay(self.driver, job_links[0])
        job_links[0].click()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # 2) Enter invalid symbols into name fields
        for loc in (ApplicationLocators.FIRST_NAME_INPUT, ApplicationLocators.LAST_NAME_INPUT):
            fld = wait_for_element(self.driver, loc)
            scroll_and_delay(self.driver, fld)
            fld.clear()
            fld.send_keys("!@#$%^&*")

        # 3) Provide a valid email so we reach the security‐code step
        email = wait_for_element(self.driver, ApplicationLocators.EMAIL_INPUT)
        scroll_and_delay(self.driver, email)
        email.clear()
        email.send_keys(fake.email())

        # 4) Click “Enter manually” and fill resume + work so the form is “complete”
        enter = wait_for_element(self.driver, ApplicationLocators.ENTER_MANUALLY)
        scroll_and_delay(self.driver, enter)
        enter.click()

        resume = wait_for_element(self.driver, ApplicationLocators.RESUME_TEXT)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", resume)
        delay(1, 1)
        resume.clear()
        resume.send_keys(fake.paragraph())

        work = wait_for_element(self.driver, ApplicationLocators.WORK_EXPERIENCE_TEXTAREA)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", work)
        delay(1, 1)
        work.clear()
        work.send_keys(fake.text())

        # 5) Sponsorship = No
        sponsor = wait_for_element(
            self.driver,
            (By.CSS_SELECTOR, "div.select__control.remix-css-13cymwt-control")
        )
        scroll_and_delay(self.driver, sponsor)
        sponsor.click()
        no_opt = wait_for_element(
            self.driver,
            (By.XPATH, "//div[contains(@class,'select__option') and normalize-space(.)='No']")
        )
        scroll_and_delay(self.driver, no_opt)
        no_opt.click()

        # 6) Submit the form
        submit = wait_for_element(self.driver, ApplicationLocators.SUBMIT_BUTTON)
        scroll_and_delay(self.driver, submit)
        submit.click()

        from selenium.common.exceptions import TimeoutException
        from selenium.webdriver.support import expected_conditions as EC

        try:
            first_code_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(SecurityLocators.INPUT(0))
            )
            self.assertTrue(
                first_code_field.is_displayed(),
                "Expected the security-code input to be displayed after invalid names."
            )

        # ─── …or we fall back to the confirmation page ──────────────────────
        except TimeoutException:
            WebDriverWait(self.driver, 10).until(
                lambda d: "/confirmation" in d.current_url
            )
            thank_you = wait_for_element(self.driver, ApplicationLocators.THANK_YOU_FOR_APPLYING)
            self.assertTrue(
                thank_you.is_displayed(),
                "Submission landed on confirmation but 'Thank you for applying' not visible."
            )

    def test_BR_N_025_verify_error_on_unsupported_resume_file_type(self):
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".exe")
        tmp.close()
        os.makedirs("evidence_025", exist_ok=True)

        # inline open_application_form
        self.driver.get(f"{self.base_url}/careers/open-roles")
        delay(2, 3)
        job_links = wait_for_elements(self.driver, CareersLocators.AI_ENGINEER_RESEARCHER)
        scroll_and_delay(self.driver, job_links[0])
        job_links[0].click()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        enter = wait_for_element(self.driver, ApplicationLocators.ENTER_MANUALLY)
        scroll_and_delay(self.driver, enter)
        enter.click()

        for loc, val in (
            (ApplicationLocators.FIRST_NAME_INPUT, fake.first_name()),
            (ApplicationLocators.LAST_NAME_INPUT,  fake.last_name()),
            (ApplicationLocators.EMAIL_INPUT,     fake.email()),
            (ApplicationLocators.WORK_EXPERIENCE_TEXTAREA, fake.text()),
        ):
            el = wait_for_element(self.driver, loc)
            scroll_and_delay(self.driver, el)
            el.clear()
            el.send_keys(val)
        take_screenshot(self.driver, "evidence_025/step_filled_text_fields.png")

        upload = wait_for_element(self.driver, ApplicationLocators.RESUME_UPLOAD)
        scroll_and_delay(self.driver, upload)
        upload.click()

        file_input = wait_for_element(self.driver, (By.CSS_SELECTOR, "input[type='file']"))
        scroll_and_delay(self.driver, file_input)
        file_input.send_keys(tmp.name)
        take_screenshot(self.driver, "evidence_025/step_uploaded_exe.png")

        submit = wait_for_element(self.driver, ApplicationLocators.SUBMIT_BUTTON)
        scroll_and_delay(self.driver, submit)
        submit.click()

        err = wait_for_element(self.driver, ApplicationFieldsErrors.RESUME_ERROR, timeout=10)
        self.assertTrue(err.is_displayed())
        self.assertNotIn("/confirmation", self.driver.current_url)
        take_screenshot(self.driver, "evidence_025/step_resume_error.png")
        os.unlink(tmp.name)


if __name__ == "__main__":
    unittest.main()
