from JupJup.Login.login import Login
from selenium.webdriver.common.keys import Keys
import time
from JupJup import config


class FacebookLogin(Login):
    XPATHS = {
        'MAINMENU': "//a[@id='main-menu-toggle']",
        'FACEBOOKOAUTH': "//button[@class='btn-facebook oauth-connect']",
        'USERNAME': "//input[@id='email']",
        'PASSWORD': "//input[@id='pass']",
        'SUBMIT': "//button[@id='loginbutton']"
    }

    def __init__(self, driver, data):
        self.driver = driver
        self.data = data

    def do_work(self):
        self.before_login()
        self.login()
        self.after_login()

    def before_login(self):
        #delete cookies to ensure that facebook login process is always same
        self.driver.delete_all_cookies()

        main_menu = self.driver.find_element_by_xpath(FacebookLogin.XPATHS['MAINMENU'])
        facebook_oauth_btn = self.driver.find_element_by_xpath(FacebookLogin.XPATHS['FACEBOOKOAUTH'])

        main_menu.click()
        facebook_oauth_btn.click()
        time.sleep(config.WAIT_LONG)

    def login(self):
        """
            폼을 채운 뒤, 로그인한다.
        """
        try:
            # find neccessary elements
            username_form = self.driver.find_element_by_xpath(FacebookLogin.XPATHS['USERNAME'])
            password_form = self.driver.find_element_by_xpath(FacebookLogin.XPATHS['PASSWORD'])
            submit_btn = self.driver.find_element_by_xpath(FacebookLogin.XPATHS['SUBMIT'])

            # fill forms
            username_form.clear()
            username_form.send_keys(self.data['USERNAME'])

            password_form.clear()
            password_form.send_keys(self.data['PASSWORD'])

            # submit form
            submit_btn.click()
            time.sleep(config.WAIT_LONG)
        except Exception as e:
            print(e)

    def after_login(self):
        print(self.driver.current_url)
        pass
