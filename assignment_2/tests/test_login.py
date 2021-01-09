
from Niyuj.pages.login_page import LoginPage
from selenium import webdriver

class Test():

    def test1(self):

        lp = LoginPage(driver=webdriver.Chrome())
        lp.setup()

        lp.click_signin()
        lp.enter_email(email_add="test@email.com")
        lp.enter_password(password='abcabc')
        lp.click_submit()
        lp.teardown()

ff = Test()
ff.test1()
