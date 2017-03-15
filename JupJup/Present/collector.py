from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from JupJup import config


class PresentCollector:
    XPATHS = {
        'COLLECTBTN': '//button[@class="present-getpoint"]'
    }

    def __init__(self, driver):
        self.driver = driver

    def collect_all(self):
        collect_btns = self.driver.find_elements_by_xpath(PresentCollector.XPATHS['COLLECTBTN'])
        # `확인하기` 버튼은 무시한다
        collect_btns = [collect_btn for collect_btn in collect_btns if "받기" in collect_btn.text]

        try:
            for collect_btn in collect_btns:
                collect_btn.click()
                time.sleep(config.WAIT_LONG)

        except Exception as e:
            print(e)
