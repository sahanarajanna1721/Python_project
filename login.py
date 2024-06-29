class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_link(self):
        self.driver.find_element('xpath', '//a[text()="Log in"]').click()

    def login_email(self, mail_id):
        self.driver.find_element('id', 'Email').send_keys(mail_id)

    def login_password(self, password):
        self.driver.find_element('id', 'Password').send_keys(password)
