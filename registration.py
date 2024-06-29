class RegistrationPage:

    ##initialization
    def __init__(self, driver):
        self.driver = driver

    ##declaration
    def reg_link(self):
        self.driver.find_element('xpath', '//a[text()="Register"]').click()

    def first_name(self, f_name):
        self.driver.find_element('id', 'FirstName').send_keys(f_name)

    def last_name(self, l_name):
        self.driver.find_element('id', 'LastName').send_keys(l_name)