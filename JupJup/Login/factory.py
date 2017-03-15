from JupJup.Login.general_login import GeneralLogin
from JupJup.Login.naver_login import NaverLogin
from JupJup.Login.facebook_login import FacebookLogin


class LoginFactory:

    @staticmethod
    def login_class(type, driver, data):
        if type == "general":
            return GeneralLogin(driver, data)
        elif type == "naver":
            return NaverLogin(driver, data)
        elif type == "facebook":
            return FacebookLogin(driver, data)
        else:
            raise Exception('invalid login method')
