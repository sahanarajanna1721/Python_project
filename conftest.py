from selenium import webdriver
import pytest
import time

@pytest.fixture()
def _drivers():
    driver = webdriver.Chrome(executable_path=r'C:\Users\QSP\PycharmProjects\drivers\chromedriver.exe')
    driver.get('https://demowebshop.tricentis.com/')
    driver.maximize_window()
    time.sleep(3)
    yield driver
    driver.close()
