import time

from  selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.email_field = (By.ID,"email")
        self.password_field = (By.XPATH,"//input[@name='password' and @id='password']")
        self.login_button = (By.ID,"loginButton")
        self.account_icon = (By.CSS_SELECTOR,"a[href='//www.n11.com/hesabim']")
        self.invalid_email_message = (By.XPATH,"//span[contains(text(),'E-posta adresi veya şifre hatalı, kontrol edebilir misin?')]")
        self.invalid_password_message = (By.XPATH, "//span[contains(text(),'E-posta adresi veya şifre hatalı, kontrol edebilir misin?')]")




    def enter_email(self,email):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.email_field))
        self.driver.find_element(*self.email_field).send_keys(email)




    def enter_password(self, password):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.password_field))
        self.driver.find_element(*self.password_field).send_keys(password)



    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()


    def get_icon(self):
        return self.driver.find_element(*self.account_icon)

    def get_icon_text(self):
        return self.driver.find_element(*self.account_icon).text


    def get_invalid_email_message_text(self):
        return  self.driver.find_element(*self.invalid_email_message).text


    def get_invalid_email_message(self):
        return  self.driver.find_element(*self.invalid_email_message)


    def get_invalid_password_message(self):
        return self.driver.find_element(*self.invalid_password_message)

    def get_invalid_password_text(self):
        return  self.driver.find_element(*self.invalid_password_message).text