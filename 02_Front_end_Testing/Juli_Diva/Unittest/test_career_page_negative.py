import pytest
from pages.career_page import CareersPage


# 1. Negative TC_026
def test_clear_all_search(browser, url):
    page = CareersPage(browser, url)
    page.open()
    page.click_view_open_roles()
    page.click_office_filter()
    page.click_department_filter()
    page.clear_all_search()

    office_elem = browser.find_element(*page.OFFICE_FILTER)
    department_elem = browser.find_element(*page.DEPARTMENT_FILTER)
    if office_elem.is_selected() and department_elem.is_selected():
        print("Test Failed")
    else:
        print("Test Passed")



# 2. Negative TC_027
def test_search_for_term(browser, url):
    page = CareersPage(browser, url)
    page.open()
    page.click_view_open_roles()
    page.search_for_term("Star")

    search_results = browser.find_elements(*page.SEARCH_NOT_FOUND)
    if search_results:
        print("Test Passed")
    else:
        print("Test Failed")


#3. Negative TC_028
def test_invalid_careers_subpage(browser, url):
    page = CareersPage(browser, url)
    page.open()
    page.invalid_careers_subpage()

    if browser.title == "404 Not Found":
        print("Test Passed")
    else:
        print("Test Failed")


#4. Negative TC_029
def test_click_back_to_jobs(browser, url):
    page = CareersPage(browser, url)
    page.open()
    page.scroll_to_featured_roles()
    page.click_first_featured_role()
    page.click_back_to_jobs()

    if browser.title == "Jobs at xAI":
        print("Test Passed")
    else:
        print("Test Failed")


#5. Negative TC_030
def test_view_open_roles_collab_incognito(browser_incognito, url):
    page = CareersPage(browser_incognito, url)
    page.open()
    page.scroll_to_collab_section()
    page.click_view_open_roles_collab()

    try:
        browser_incognito.execute_script("""
                try {
                    localStorage.setItem('test', '1');
                    localStorage.removeItem('test');
                } catch (e) {
                    console.log('Might be incognito');
                }
            """)
    except Exception as e:
        print(f"JS execution failed: {e}")
