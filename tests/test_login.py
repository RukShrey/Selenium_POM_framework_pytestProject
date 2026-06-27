#cretaed login test script
from pages.login_page import LoginPage

def test_login(driver):
    login = LoginPage(driver)
    login.load()
    login.login(username="Admin",password="admin123")

