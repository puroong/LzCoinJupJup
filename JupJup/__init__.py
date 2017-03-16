from selenium import webdriver
from JupJup import Login, Present, Share
from JupJup import config
import time

class CoinJupJupManager:

    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.data = config.USERDATA
        self.login = Login.factory.LoginFactory.login_class(config.LOGIN_METHOD, self.driver, self.data)
        self.collector = Present.collector.PresentCollector(self.driver)
        self.share = Share.share_facebook.ShareFacebook(self.driver)

        self.last_worked_at = time.time()
        self.worked_today = False

    def do_work(self):
        while True:
            if not self.worked_today:
                self.driver.maximize_window()

                self.attend()
                self.collect_presents()
                self.share_lezhin()

                self.worked_today = True

            if time.time() - self.last_worked_at > 86400:
                self.last_worked_at = time.time()
                self.worked_today = False

    def attend(self):
        print('attend start')

        self.driver.get('https://www.lezhin.com/ko')
        time.sleep(config.WAIT_LONG)
        self.login.do_work()

        print('attend finish')

    def collect_presents(self):
        print('present collect start')

        self.driver.get('https://www.lezhin.com/ko/present')
        time.sleep(config.WAIT_LONG)
        self.collector.collect_all()

        print('present collect finish')

    def share_lezhin(self):
        print('share lezhin start')

        self.driver.get('https://www.lezhin.com/ko/payment#invite')
        time.sleep(config.WAIT_LONG)
        self.share.do_work()

        time.sleep(config.WAIT_LONG)

        print('share lezhin finish')
