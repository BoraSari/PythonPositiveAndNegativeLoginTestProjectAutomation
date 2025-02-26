from argparse import Action


from  selenium.webdriver.common.by import By

class MainPage:




    def __init__(self,driver):
         self.driver = driver
         self.navigate_login_button = (By.CSS_SELECTOR, "a[href='https://www.n11.com/giris-yap']")
         self.search_box = (By.ID,"searchData")






    def navigate_login_page(self):
        self.driver.find_element(*self.navigate_login_button).click()




    def search_product(self,product):
       self.driver.find_element(*self.search_box).send_keys(product)