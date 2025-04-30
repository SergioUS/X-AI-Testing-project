from selenium.webdriver.common.by import By
import time
import unittest
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


def delay():
    time.sleep(random.randint(3,4))

def company_button(driver):
    driver.find_element(By.XPATH, "(//a[@href='/company'])[1]").click()
    delay()

def hover_GROK_button(driver):
    element_to_hover = driver.find_element(By.XPATH, "(//a[contains(.,'Grok')])[1]")
# Create an ActionChains object
    actions = ActionChains(driver)
# Perform the hover action
    actions.move_to_element(element_to_hover).perform()
    delay()

def BUSINESS_button(driver):
    driver.find_element(By.XPATH, "//a[@href='/grok/business']").click()

def ScrollDown_Request_Early_Access(driver):
    Request_Early_Access = driver.find_element(By.XPATH, "//span[contains(.,'Request early access')]")
    driver.execute_script("arguments[0].scrollIntoView();", Request_Early_Access)

def Request_Access(driver):
    driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Request access')]").click()
    delay()

def alert_2(driver):
    driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(4)

    alert_2 = driver.find_element(By.XPATH, "//div[contains(text(),'Unexpected token')]")
    if alert_2:
        print("test_chrome_TC_N_002 PASS")
    else:
        print("test_chrome_TC_N_002 FAIL")

def alert_3(driver):
    driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(4)

    alert_3 = driver.find_element(By.XPATH, "//div[contains(text(),'Unexpected token')]")
    if alert_3:
        print("test_chrome_TC_N_003 PASS")
    else:
        print("test_chrome_TC_N_003 FAIL")

def alert_4(driver):
    driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(4)

    alert_4 = driver.find_element(By.XPATH, "//div[contains(text(),'Unexpected token')]")
    if alert_4:
        print("test_chrome_TC_N_004 PASS")
    else:
        print("test_chrome_TC_N_004 FAIL")

def alert_5(driver):
    driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(4)

    alert_5 = driver.find_element(By.XPATH, "//div[contains(text(),'Unexpected token')]")
    if alert_5:
        print("test_chrome_TC_N_005 PASS")
    else:
        print("test_chrome_TC_N_005 FAIL")

