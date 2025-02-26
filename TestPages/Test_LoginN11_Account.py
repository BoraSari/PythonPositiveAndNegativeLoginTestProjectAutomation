import os
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.devtools.v85.network import set_data_size_limits_for_test
from webdriver_manager.chrome import ChromeDriverManager
from N11Pages.Datas import base_url
from N11Pages.Login_Page import LoginPage
from N11Pages.MainPage import MainPage
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv()
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import os

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()



def test_for_login(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    driver.get(base_url)
    email= os.getenv("Email")
    password= os.getenv("Password")
    main_page.navigate_login_page()
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login_button()

    actual_result = login_page.get_icon()
    actual_result_text = login_page.get_icon_text()
    expected_result = "KL"

    assert  actual_result.is_displayed()
    assert expected_result.__eq__(actual_result_text) ,"Expected: {expected_result}, Actual: {actual_result_text}"



def test_for_login_invalid_email(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    driver.get(base_url)
    main_page.navigate_login_page()
    password = os.getenv("password")
    login_page.enter_email("123014034343434@gmail.com")
    login_page.enter_password(password)
    login_page.click_login_button()

    actual_result = login_page.get_invalid_email_message()
    actual_result_text = login_page.get_invalid_email_message_text()
    expected_result = "E-posta adresi veya şifre hatalı, kontrol edebilir misin?"

    assert actual_result.is_displayed()
    assert expected_result.__eq__(actual_result_text),"Expected: {expected_result}, Actual: {actual_result_text}"


def test_for_login_invalid_password(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    driver.get(base_url)
    main_page.navigate_login_page()
    login_page.enter_email("kingoflight529@gmail.com")
    login_page.enter_password("123456")
    login_page.click_login_button()

    actual_result = login_page.get_invalid_password_message()
    actual_result_text = login_page.get_invalid_password_text()
    expected_result = "E-posta adresi veya şifre hatalı, kontrol edebilir misin?"

    assert  actual_result.is_displayed()
    assert  expected_result.__eq__(actual_result_text) ,"Expected: {expected_result}, Actual: {actual_result_text}"






















