from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import string, random

def test_shopping_list():
    print("testing search...")
    browser = webdriver.Chrome()
    try:
        browser.get("http://localhost:8080")
        assert "broccoli" in browser.page_source
        assert "Delete" in browser.page_source
        assert "Edit" in browser.page_source
        assert "Add an item" in browser.page_source
    finally:
        browser.close()

def test_add_item():
    print("testing search...")
    browser = webdriver.Chrome()
    try:
        browser.get("http://localhost:8080/add")
        assert "Add a new item.." in browser.page_source
        assert "New Item:" in browser.page_source
        new_item = "".join(random.choices(string.ascii_letters,k=14))
        item_input = browser.find_element(By.NAME, "description")
        item_input.clear()
        item_input.send_keys(new_item)
        submit_button = browser.find_element(By.TAG_NAME,"button")
        submit_button.click()
        time.sleep(3)
        browser.get("http://localhost:8080")
        assert new_item in browser.page_source
        time.sleep(3)
    finally:
        browser.close()

def test_delete_item():
    print("testing search...")
    browser = webdriver.Chrome()
    try:
        browser.get("http://localhost:8080/add")
        assert "Add a new item.." in browser.page_source
        assert "New Item:" in browser.page_source
        new_item = "".join(random.choices(string.ascii_letters,k=14))
        item_input = browser.find_element(By.NAME, "description")
        item_input.clear()
        item_input.send_keys(new_item)
        submit_button = browser.find_element(By.TAG_NAME,"button")
        submit_button.click()
        time.sleep(1)
        browser.get("http://localhost:8080")
        assert new_item in browser.page_source
        time.sleep(2)
        list_items = browser.find_elements(By.TAG_NAME,"tr")
        for list_item in list_items:
            columns = list_item.find_elements(By.TAG_NAME,"td")
            desc = columns[1].text
            if new_item == columns[1].text:
                print("found", list_item.text)
                delete_link = columns[2]
                delete_link.click()
                break
        time.sleep(5)
        browser.get("http://localhost:8080")
        assert new_item not in browser.page_source
        
    finally:
        browser.close()

if __name__ == "__main__":
    # test_shopping_list()
    # test_add_item()
    test_delete_item()
    print("done.")