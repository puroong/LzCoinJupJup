from selenium import webdriver
from JupJup import Login, Present, Share
from JupJup import config
from multiprocessing import Process
import time

class CoinJupJupManager:

    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.data = config.USERDATA
        self.login = Login.factory.LoginFactory.login_class(config.LOGIN_METHOD, self.driver, self.data)
        self.collector = Present.collector.PresentCollector(self.driver)
        self.share = Share.share_facebook.ShareFacebook(self.driver)

        self.last_shared_at = time.time()
        self.last_collected_at = time.time()

        self.shared_done = True
        self.collected_done = True

    def start(self):
        p_collect = Process(target=self.collect_task)
        p_share = Process(target=self.share_task)

        p_collect.start()
        p_share.start()

    def collect_task(self):
        while True:
            if not self.collected_done:
                self.driver.maximize_window()

                self.attend()
                self.collect_presents()

                self.collected_done = True

            if time.time() - self.last_collected_at > config.COLLECT_PERIOD:
                self.last_collected_at = time.time()
                self.collected_done = False

            time.sleep(config.WORK_PERIOD)

    def share_task(self):
        while True:
            if not self.shared_done:
                self.driver.maximize_window()

                self.attend()
                self.share_lezhin()

                self.shared_done = True

            if time.time() - self.last_shared_at > config.SHARE_PERIOD:
                self.last_shared_at = time.time()
                self.shared_done = False

            time.sleep(config.WORK_PERIOD)

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
