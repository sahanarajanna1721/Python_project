# import time
#
# def test_registration_link(_drivers):
#     _drivers.find_element('xpath', '//a[text()="Register"]').click()
#     time.sleep(2)
#     _drivers.find_element('id', 'FirstName').send_keys('demo')
#     time.sleep(1.5)
#     _drivers.find_element('id', 'LastName').send_keys('web')

#---------------------------------------------------
import time

##utilization

from registration import RegistrationPage
def test_registration(_drivers):
    exe_driver = _drivers
    reg_page = RegistrationPage(exe_driver)

    reg_page.reg_link()
    time.sleep(2)
    reg_page.first_name('demowebshop')
    time.sleep(2)
    reg_page.last_name('tricentis')
    time.sleep(2)

def test_registration_2(_drivers):
    exe_driver = _drivers
    reg_page = RegistrationPage(exe_driver)

    reg_page.reg_link()
    time.sleep(2)
    reg_page.first_name('demo')
    time.sleep(2)
    reg_page.last_name('tricentis')
    time.sleep(2)


from login import LoginPage
def test_loginpage(_drivers):
    exe_driver = _drivers
    login_obj = LoginPage(exe_driver)

    login_obj.login_link()
    time.sleep(2)
    login_obj.login_email('demo@tricentis.com')
    time.sleep(2)
    login_obj.login_password('demo@123')
    time.sleep(2)

def test_loginpage_2(_drivers):
    exe_driver = _drivers
    login_obj = LoginPage(exe_driver)

    login_obj.login_link()
    time.sleep(2)
    login_obj.login_email('demo@gmail.com')
    time.sleep(2)
    login_obj.login_password('demo@123')
    time.sleep(2)