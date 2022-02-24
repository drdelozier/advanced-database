from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def test_python_org_search():
    print("testing search...")
    driver = webdriver.Chrome()
    try:
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element(By.NAME,"q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No results found." not in driver.page_source
    finally:
        driver.close()

def test_python_org_go_button():
    print("testing go button...")
    browser = webdriver.Chrome()
    try:
        browser.get("http://www.python.org")
        assert "Python" in browser.title
        elem = browser.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        go_button = browser.find_element(By.ID, "submit")
        go_button.click()
        time.sleep(5)
        assert "No results found." not in browser.page_source
    finally:
        browser.close()