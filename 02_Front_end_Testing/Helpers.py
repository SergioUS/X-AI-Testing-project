from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import requests


def delay():
    time.sleep(random.randint(2, 6))


home_url = "https://x.ai/"
colossus_url = "https://x.ai/colossus"


