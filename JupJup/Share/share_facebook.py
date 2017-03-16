from JupJup import config
from JupJup.Login.facebook_login import FacebookLogin
import time
from JupJup import config


class ShareFacebook:
    XPATHS = {
        'SHAREBTN': '//button[@class="sqc__share__btn"]',
        'TOFACEBOOK': '//button[@class="sharepop__btn sharepop__btn--facebook"]',
        'LOGINCONTENT': '//div[@id="content"]',
        'TEXTAREA': '//textarea[@title="하고 싶은 말을 남겨주세요..."]',
        'POSTBTN': '//button[@name="__CONFIRM__"]'
    }

    def __init__(self, driver):
        self.driver = driver
        self.data = config.FB_USERDATA
        self.facebook_authorize = FacebookLogin(self.driver, self.data)

        self.main_window = self.driver.current_window_handle
        self.facebook_window = None

    def do_work(self):
        self.open_facebook()

        if self.is_login_page():
            self.facebook_authorize.authorize()

        self.post_feed()
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
    def open_facebook(self):
        self.main_window = self.driver.window_handles[0]

        share_btn = self.driver.find_element_by_xpath(ShareFacebook.XPATHS['SHAREBTN'])
        share_btn.click()

        to_facebook_btn = self.driver.find_element_by_xpath(ShareFacebook.XPATHS['TOFACEBOOK'])
        to_facebook_btn.click()

        time.sleep(config.WAIT_LONG)

    def is_login_page(self):
        facebook_window = self.driver.window_handles[1]
        self.driver.switch_to_window(facebook_window)

        login_content = self.driver.find_element_by_xpath(ShareFacebook.XPATHS['LOGINCONTENT'])

        return "Log in to use your Facebook account with LezhinComics" in login_content.text

    def post_feed(self):
        # type message
        textarea = self.driver.find_element_by_xpath(ShareFacebook.XPATHS['TEXTAREA'])

        textarea.clear()
        textarea.send_keys(config.FB_POSTMSG)
        # post feed
        post_btn = self.driver.find_element_by_xpath(ShareFacebook.XPATHS['POSTBTN'])
        post_btn.click()

        time.sleep(config.WAIT_LONG)
        # switch to main window again
        self.driver.switch_to_window(self.main_window)
