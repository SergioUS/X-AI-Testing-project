import pytest
from appium.options.gecko.firefox_options_option import FIREFOX_OPTIONS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager


#This is necessary to pass cl options
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Choose browser: Chrome(default), Firefox, or IE"
    )
# Load all the reusable browser invocation into an object inside a fixture.
# Use the object in the actual test scripts.

@pytest.fixture(scope="class")
def setup(request): # pytest object that allows the fixture to interact with the test that requested it

    browser_name=request.config.getoption("browser_name") # receives value entered at runtime
    if browser_name == "chrome":
        driver = webdriver.Chrome (service=ChromeService(ChromeDriverManager().install()))

    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser_name == "IE":
        driver = webdriver.Ie (service=IEService (IEDriverManager ().install ()))

    driver.get('https://x.ai/')
    driver.maximize_window ()

    request.cls.driver = driver  #Attach the driver to the test class = available to all test methods in class

    yield   # script run fixture setup -> exe test script -> yield to teardown
    driver.close()
