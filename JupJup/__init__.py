from selenium import webdriver
from JupJup import Login, Present, Share
from JupJup import config
from multiprocessing import Process
import time

class CoinJupJupManager:

    def __init__(self):
        self.data = config.USERDATA

    def start(self):
        p_collect = Process(target=self.collect_task)
        p_share = Process(target=self.share_task)

        p_collect.start()
        p_share.start()

    def collect_task(self):
        driver = webdriver.PhantomJS()

        login = Login.factory.LoginFactory.login_class(config.LOGIN_METHOD, driver, self.data)
        collector = Present.collector.PresentCollector(driver)

        last_collected_at = time.time()
        collected_done = False

        while True:
            if not collected_done:
                driver.maximize_window()

                self.attend(driver, login)
                self.collect_presents(driver, collector)

                self.reset(driver)

                collected_done = True

            if time.time() - last_collected_at > config.COLLECT_PERIOD:
                last_collected_at = time.time()
                collected_done = False

            time.sleep(config.WORK_PERIOD)

    def share_task(self):
        driver = webdriver.PhantomJS()

        login = Login.factory.LoginFactory.login_class(config.LOGIN_METHOD, driver, self.data)
        share = Share.share_facebook.ShareFacebook(driver)

        last_shared_at = time.time()
        shared_done = False

        while True:
            if not shared_done:
                driver.maximize_window()

                self.attend(driver, login)
                self.share_lezhin(driver, share)

                self.reset(driver)

                shared_done = True

            if time.time() - last_shared_at > config.SHARE_PERIOD:
                last_shared_at = time.time()
                shared_done = False

            time.sleep(config.WORK_PERIOD)

    def attend(self, driver, login):
        print('attend start')

        driver.get('https://www.lezhin.com/ko')
        time.sleep(config.WAIT_LONG)
        login.do_work()

        print('attend finish')

    def collect_presents(self, driver, collector):
        print('present collect start')

        driver.get('https://www.lezhin.com/ko/present')
        time.sleep(config.WAIT_LONG)
        collector.collect_all()

        print('present collect finish')

    def share_lezhin(self, driver, share):
        print('share lezhin start')

        driver.get('https://www.lezhin.com/ko/payment#invite')
        time.sleep(config.WAIT_LONG)
        share.do_work()

        time.sleep(config.WAIT_LONG)

        print('share lezhin finish')

    def reset(self, driver):
        driver.get('https://www.lezhin.com/ko')
        #delete cookies to ensure that naver login process is always same
        driver.delete_all_cookies()
