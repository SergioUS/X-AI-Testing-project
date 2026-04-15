import pytest
import undetected_chromedriver as uc


@pytest.fixture(scope="function")
def browser():
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")

    # popups + notifications
    prefs = {
        "profile.default_content_setting_values.popups": 1,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)

    driver = uc.Chrome(
        options=options,
        use_subprocess=True,
        version_main=146
    )

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def browser_incognito():
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")

    # popups + notifications
    prefs = {
        "profile.default_content_setting_values.popups": 1,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)

    driver = uc.Chrome(
        options=options,
        use_subprocess=True,
        version_main=146
    )

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def url():
    return "https://x.ai/careers"