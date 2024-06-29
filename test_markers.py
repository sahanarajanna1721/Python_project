'''
If we give --> pytest -vs
This will execute all the modules present in the directory. This we call it as
a Batch execution
'''

#--------------------------------
'''
1. built in markers
2. custom markers
'''

#-----------------------------------
# import pytest
#
# @pytest.mark.smoke      #smoke is the testcasename. can pass any pass
# def test_signup():
#     print('test signup executing')
#
# @pytest.mark.regression
# def test_login():
#     print('login page executing')
#
# @pytest.mark.smoke
# def test_shopping_cart():
#     print('shopping cart executing')
#
# @pytest.mark.sanity
# def test_logout():
#     print('logout executing')
import pytest

'''To execute the particular testcase
right click --> open terminal --> pytest test_filename.py -vs -m testcase_name

## To execute only sanity --> pytest test_fname -vs -m sanity
# sanity or smoke--> pytest test_fname -vs -m "sanity or smoke"
'''

#-----------------------------
# import pytest
#
# @pytest.mark.smoke      #smoke is the testcasename. can pass any pass
# def test_signup():
#     print('test signup executing')
#
# @pytest.mark.sanity
# @pytest.mark.regression
# def test_login():
#     print('login page executing')
#
# @pytest.mark.smoke
# def test_shopping_cart():
#     print('shopping cart executing')
#
# @pytest.mark.sanity
# def test_logout():
#     print('logout executing')

#-----------------------
# import pytest
#
# class TestSpam:
#
#     @pytest.mark.smoke
#     def test_login(self):
#         print('test login executing')
#
#     @pytest.mark.sanity
#     def test_username(self):
#         print('test username executing')
#
#     @pytest.mark.sanity
#     def test_pwd(self):
#         print('test password executing')
#
#     @pytest.mark.regression
#     def test_logout(self):
#         print('test logout executing')

#-----------------------------------------
# import pytest
#
# @pytest.mark.smoke
# class TestSpam:
#
#     @pytest.mark.smoke
#     def test_login(self):
#         print('test login executing')
#
#     @pytest.mark.sanity
#     def test_username(self):
#         print('test username executing')
#
#     @pytest.mark.sanity
#     def test_pwd(self):
#         print('test password executing')
#
#     @pytest.mark.regression
#     def test_logout(self):
#         print('test logout executing')

#------------------------------------------------------
# import pytest
#
# @pytest.mark.smoke
# class TestSpam:
#
#     def test_login(self):
#         print('test login executing')
#
#     def test_signup(self):
#         print('test signup executing')
#
# @pytest.mark.smoke
# class TestDisplay:
#
#     def test_logout(self):
#         print('test logout executing')
#
#     def test_signin(self):
#         print('test signin executing')

#-------------------------------------------------------
'''
skip
skipif
parameterized
dependencies
xfail
'''
#------------------
'''skip --> To skip the particular testcase'''
# import pytest
#
# @pytest.mark.skip(reason='Unnecessary testcase')
# def test_signup():
#     print('test signup executing')
#
# def test_login():
#     print('login page executing')
#
# @pytest.mark.skip
# def test_shopping_cart():
#     print('shopping cart executing')
#
# def test_logout():
#     print('logout executing')

#---------------------------------
'''skipif : skipif will take condition as the argument, when the condition is true, 
testcase will be skipped'''

# import pytest
#
# a = 10
# @pytest.mark.skipif(a==10, reason='same value')
# def test_signup():
#     print('test signup executing')
#
# def test_login():
#     print('login page executing')
#
# def test_shopping_cart():
#     print('shopping cart executing')
#
# def test_logout():
#     print('logout executing')

#--------
# url = 'demo'
# @pytest.mark.skipif(url in 'https://demowebshop.tricentis.com/', reason='url not found')
# def test_login():
#     print('test login executing')
#
# def test_logout():
#     print('test logout executing')
#
# def test_signup():
#     print('test signup executing')

#------------------------------
'''xfail'''
# import pytest
#
# @pytest.mark.xfail(reason='not a valid testcase')
# def test_login():
#     print('test login executing')
#
# def test_logout():
#     print('test logout executing')
#
# def test_signup():
#     print('test signup executing')

#---------------------------------------------
'''parameterized markers'''
# import pytest
#
# @pytest.mark.parametrize('name', ['ram', 'lakshman', 'ravan', 'sita']) ##actual parameters will be considered in string
# # format, formal parameters  be considered in list format
# def test_login(name):
#     print(f'Username is {name}')

#---------
import pytest

@pytest.mark.parametrize(["username", "password"], [('ram', 'ram1234'), ('sita', 'sita1234')])
def test_login(username, password):
    print(username)
    print(password)

#--------------------

# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path=r'C:\Users\QSP\PycharmProjects\drivers\chromedriver.exe')
#
# driver.get('https://demo.actitime.com/login.do')
# driver.maximize_window()
#
# @pytest.mark.parametrize(["username", "password"], [("admin", "manager"),
#                                                     ('trainee', 'trainee'),
#                                                     ('admin', 'trainee')])
# def test_login(username, password):
#     driver.find_element('name', 'username').send_keys(username)
#     driver.find_element('name', 'pwd').send_keys(password)
#     driver.find_element('xpath', '//div[text()="Login "]').click()







































