from JupJup.Login.login import Login
from selenium.webdriver.common.keys import Keys
import time


class NaverLogin(Login):
    XPATHS = {
        'MAINMENU': "//a[@id='main-menu-toggle']",
        'NAVEROAUTH': "//button[@class='btn-naver oauth-connect']",
        'USERNAME': "//input[@id='id']",
        'PASSWORD': "//input[@id='pw']",
        'SUBMIT': "//input[@title='Sign in']",
        'NOSAVE': '//a[text()="Don\'t Save"]'
    }

    def __init__(self, driver, data):
        self.driver = driver
        self.data = data

    def do_work(self):
        self.before_login()
        self.login()
        self.after_login()

    def before_login(self):
        main_menu = self.driver.find_element_by_xpath(NaverLogin.XPATHS['MAINMENU'])
        naver_oauth_btn = self.driver.find_element_by_xpath(NaverLogin.XPATHS['NAVEROAUTH'])

        main_menu.click()
        naver_oauth_btn.click()
        time.sleep(7)

    def login(self):
        """
            폼을 채운 뒤, 로그인한다.
        """
        try:
            print(self.driver.current_url)
            # find neccessary elements
            username_form = self.driver.find_element_by_xpath(NaverLogin.XPATHS['USERNAME'])
            password_form = self.driver.find_element_by_xpath(NaverLogin.XPATHS['PASSWORD'])
            submit_btn = self.driver.find_element_by_xpath(NaverLogin.XPATHS['SUBMIT'])

            # fill forms
            username_form.clear()
            username_form.send_keys(self.data['USERNAME'])

            password_form.clear()
            password_form.send_keys(self.data['PASSWORD'])

            # submit form
            submit_btn.click()
            time.sleep(7)
        except Exception as e:
            print(e)

    def after_login(self):
        print(self.driver.current_url)

        try:
            nosave_btn = self.driver.find_element_by_xpath(NaverLogin.XPATHS['NOSAVE'])
            print(nosave_btn)
            nosave_btn.click()
            time.sleep(7)
        except Exception as e:
            print(e)
