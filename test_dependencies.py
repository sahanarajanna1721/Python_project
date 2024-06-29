from selenium import webdriver
import pytest
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\QSP\PycharmProjects\drivers\chromedriver.exe')

driver.get('https://demo.actitime.com/login.do')
driver.maximize_window()
time.sleep(2)

@pytest.mark.dependency()       #independent
def test_login():
    driver.find_element('id', 'username').send_keys('adminnnn')
    time.sleep(1)
    driver.find_element('name', 'pwd').send_keys('manager')
    time.sleep(1)
    driver.find_element('xpath', '//div[text()="Login "]').click()
    time.sleep(5)

@pytest.mark.dependency(depends=['test_login'])
def test_logout():
    driver.find_element('xpath', '//a[text()="Logout"]').click()

## @pytest.mark.dependency(depends=['testname1', 'testname2', 'testname3'...])