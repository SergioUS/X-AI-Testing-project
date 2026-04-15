import pytest
from pages.career_page import CareersPage

# 1. Positive TC_021 View Open Roles button
def test_view_open_roles(browser, url):
    page = CareersPage(browser, url)
    page.open()
    page.click_view_open_roles()
    expected_url = "https://x.ai/careers/open-roles"
    if browser.current_url == expected_url:
        print("Test Passed")
    else:
        print("Test Failed")

# 2. Positive TS_022 Filter Jobs
def test_filter_jobs(browser, url):
    page = CareersPage(browser, url)
    page.open()
    page.click_view_open_roles()
    page.click_office_filter()
    page.click_department_filter()

    current_url = browser.current_url.lower()
    try:
        assert "location=london" in current_url and "dept=" in current_url
    except AssertionError:
        assert False, f" Filters not applied correctly. Current URL: {current_url}"

# 3. Positive TC_023 View Job Details
def test_view_job_details(browser, url):
    page = CareersPage(browser, url)
    page.open()
    page.scroll_to_featured_roles()
    page.click_first_featured_role()

# 4. Positive TC_024 Apply Now button
def test_apply_now(browser, url):
    page = CareersPage(browser, url)
    page.open()
    page.scroll_to_interview_process()
    page.click_apply_now()
    current_url = browser.current_url
    if current_url == "https://x.ai/careers/open-roles":
        print(" Apply Now navigated correctly")
    else:
        print(f" Navigation failed, current URL: {current_url}")


# 5. Positive TC_025 View Open Roles (Collaboration Across Borders)
def test_view_open_roles_collab(browser, url):
    page = CareersPage(browser, url)
    page.open()
    page.scroll_to_collab_section()
    page.click_view_open_roles_collab()
    current_url = browser.current_url
    if current_url == "https://x.ai/careers/open-roles":
        print(" Apply Now navigated correctly")
    else:
        print(f" Navigation failed, current URL: {current_url}")

