from abc import ABCMeta
from abc import abstractmethod


class Login(metaclass=ABCMeta):
    """
        로그인 시 필요한 함수 종류 써놓은 추상클래스
    """
    @abstractmethod
    def do_work(self):
        pass
    @abstractmethod
    def before_login(self):
        pass
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def after_login(self):
        pass
