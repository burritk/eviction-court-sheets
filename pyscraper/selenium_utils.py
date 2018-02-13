import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_headless_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    current_path = os.path.dirname(__file__)
    filename = os.path.join(current_path, 'chromedriver')
    driver = webdriver.Chrome(filename, chrome_options=chrome_options)

    return driver

def get_headed_driver():
    current_path = os.path.dirname(__file__)
    filename = os.path.join(current_path, 'chromedriver')
    driver = webdriver.Chrome(filename)
    return driver

def wait_for_xpath(driver, xpath, time=10): # add if_exists
    element = WebDriverWait(driver, time).until(  # wait for form
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    return element

def wait_for_tag(driver, tag, time=10): # add if_exists
    element = WebDriverWait(driver, time).until(  # wait for form
        EC.presence_of_element_located((By.TAG_NAME, tag))
    )
    return element

def wait_for_classname(driver, classname, time=0):
    element = WebDriverWait(driver, time).until(
        EC.presence_of_element_located((By.CLASS_NAME, classname))
    )
    return element


def get_selenium_xpath_if_exists(driver, xpath):
    if len(driver.find_elements_by_xpath(xpath)) < 1:
        return ''
    text = driver.find_element_by_xpath(xpath) if 'text' in xpath else driver.find_element_by_xpath(xpath).text
    return text.strip() if text else ''
