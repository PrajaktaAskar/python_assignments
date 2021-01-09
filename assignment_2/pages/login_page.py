from selenium import webdriver
from selenium.webdriver.common.by import By
from Niyuj.base import locators

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def setup(self):
        baseurl = "https://courses.letskodeit.com/"
        #self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(baseurl)


    def click_signin(self):
        self.driver.find_element(By.LINK_TEXT, locators._sign_in_link).click()

    def enter_email(self, email_add):
        self.driver.find_element(By.ID, locators._email_ID).send_keys("email_add")

    def enter_password(self, password):
        self.driver.find_element(By.ID, locators._pass_ID).send_keys("password")

    def click_submit(self):
        self.driver.find_element(By.XPATH, locators._submit_btn_xpath).click()

    def teardown(self):
        self.driver.close()

