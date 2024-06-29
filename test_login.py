# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path=r'C:\Users\QSP\PycharmProjects\drivers\chromedriver.exe')
#
# def test_login():
#     driver.get('https://demowebshop.tricentis.com/')
#     driver.maximize_window()
#     driver.find_element('xpath', "//a[text()='Log in']").click()

#-----------------------------

## Using conftest

def test_login(_drivers):
    _drivers.find_element('xpath', "//a[text()='Log in']").click()
