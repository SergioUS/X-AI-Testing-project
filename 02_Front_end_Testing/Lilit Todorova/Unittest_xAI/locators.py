from selenium.webdriver.common.by import By

class HomeLocators:
    CAREERS_MODULE = (By.XPATH, "(//a[contains(text(), 'Careers')])[1]")

class CareersLocators:
    VIEW_OPEN_ROLES = (By.XPATH, "//span[contains(text(), 'View Open Roles')]")
    OPEN_ROLES = (By.XPATH, "//h2[normalize-space(text())='Open roles']")
    OFFICE_FILTER = (By.XPATH, "//span[contains(text(), 'Office:')]")
    OFFICE_SAN_FRANCISCO = (By.XPATH, "//button[contains(text(), 'San Francisco')]")
    DEPARTMENT_FILTER = (By.XPATH, "//span[contains(text(), 'Department:')]")
    DEPARTMENT_ENGINEERING = (By.XPATH, "//button[contains(text(), 'Engineering, Research & Product')]")
    AI_ENGINEER_RESEARCHER = (By.XPATH, "//a[contains(@href, 'https://job-boards.greenhouse.io/xai/jobs/4533894007')]")
    JOB_TITLE_HEADER = (By.XPATH, "//h1[contains(text(), 'AI Engineer & Researcher - Inference')]")
    JOB_LISTINGS = (By.CSS_SELECTOR, ".job-card")

class ApplicationLocators:
    # Personal Information Fields
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    EMAIL_INPUT = (By.ID, "email")
    PHONE_INPUT = (By.ID, "phone")

    # Resume Upload and Manual Entry
    RESUME_UPLOAD = (By.ID, "upload-label-resume")  # Optional if not using manual entry
    ATTACH_BUTTON = (By.XPATH, "//div[@class='secondary-button']/div/button[contains(text(), 'Attach')]")
    ENTER_MANUALLY = (By.XPATH, "//button[contains(text(), 'Enter manually')]")
    RESUME_TEXT = (By.ID, "resume_text")

    # Additional Application Fields
    WORK_EXPERIENCE_TEXTAREA = (By.XPATH, "//textarea[@id='question_8742881007']")  # What exceptional work have you done?
    SUBMIT_BUTTON = (By.XPATH, "//div[@class='application--submit']/button[contains(text(), 'Submit application')]")

    # Confirmation Page
    THANK_YOU_FOR_APPLYING = (By.XPATH, "//h1[contains(text(), 'Thank you for applying.')]")

    # Email Verification
    EMAIL_VERIFICATION_FIELD = (By.XPATH, "//fieldset[@id='email-verification']")
    VERIFICATION_LEGEND_TEXT = (By.XPATH, "//fieldset[@id='email-verification']//legend")

class LatestRoles:
    LATEST_ROLES = (By.XPATH, "//h2[contains(text(), 'Latest Roles')]")
    VIEW_ALL_OPEN_ROLES = (By.XPATH, "//a[contains(text(), 'View all open roles')]")
    SECURITY = (By.XPATH, "(//div/div/h3[contains(text(), 'Security')])[2]")

class ApplicationFieldsErrors:
    FIRST_NAME_ERROR = (By.ID, "first_name-error")
    LAST_NAME_ERROR = (By.ID, "last_name-error")
    EMAIL_FORMAT_ERROR = (By.ID, "email-error")
    PHONE_ERROR = (By.ID, "phone-error")
    RESUME_ERROR = (By.ID, "resume-error")
    WORK_EXPERIENCE_TEXTAREA_ERROR = (By.ID, "question_8742881007-error")  # What exceptional work have you done?
    EMAIL_VERIFICATION_ERROR = (By.ID, "email-verification-error")

class SecurityLocators:
    INPUT = lambda idx: (By.ID, f"security-input-{idx}")
    VERIFY_BUTTON = (By.XPATH, "//button[contains(text(),'Verify') or contains(text(),'Submit')]")
    WRONG_CODE_ERROR = (
        By.XPATH,
        "//div[contains(text(),'incorrect code') or contains(text(),'wrong code')]"
    )