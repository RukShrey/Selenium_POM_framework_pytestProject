from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    UserName = (By.NAME,"username")
    PassWord = (By.NAME,"password")
    LoginButton = (By.XPATH, "//button[@type='submit']")

    def load(self):
        self.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self,username:str, password:str):
        self.type(self.UserName, username)
        self.type(self.PassWord, password)
        self.click(self.LoginButton)
