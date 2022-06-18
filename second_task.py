from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self):
        username_input = self.browser.find_element(by=By.CSS_SELECTOR, value="input[name='username']")
        password_input = self.browser.find_element(by=By.CSS_SELECTOR, value="input[name='password']")
        username_input.send_keys("yoshidazaz@gmail.com")
        password_input.send_keys("pogger6969!")
        login_button = self.browser.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button/div')
        login_button.click()
        sleep(5)


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')


browser = webdriver.Chrome(executable_path='D:\python\likes task\chromedriver.exe')
browser.implicitly_wait(5)
home_page = HomePage(browser)