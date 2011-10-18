#!/usr/bin/env python

from selenium.webdriver.common.by import By

import base_page

class SignInPage(base_page.BasePage):
    _page_title = "Spreets"
    _your_email_locator = (By.ID, "email")
    _your_password_locator = (By.ID, "password")
    _sign_in_button_locator = (By.ID, "loginBtn")

    def sign_in(self, user="default"):
        credentials = self.credentials_of_user(user)
        self.type_useremail(credentials["useremail"])
        self.type_password(credentials["password"])
        self.click_sign_in()

    def type_usermail(self, useremail):
        useremail_field = self.selenium.find_element(*self._your_email_locator)
        useremail_field.clear()
        useremail_field.send_keys(useremail)

    def type_password(self, password):
        password_field = self.selenium.find_element(*self._your_password_locator)
        password_field.clear()
        password_field.send_keys(password)

    def click_sign_in(self):
        self.selenium.find_element(*self._sign_in_button_locator).click()

    
