#!/usr/bin/env python

from selenium.webdriver.common.by import By

import base_page


class HomePage(base_page.BasePage):

    _page_title = "Get the Perfect Silhouette! Only $39 for Two Pairs of Amazing Slimming Body Shape-Wear Pants. In Beige & Black. Worth $118. Includes Delivery! - Spreets"
    _sign_in_link_locator = (By.LINK_TEXT, "Sign In")
    
    def go_to_home_page(self):
        self.selenium.get(self.testsetup.base_url)
        self.is_the_current_page

    def click_sign_in_link(self):
        self.selenium.find_element(*self._sign_in_link_locator).click()
        

    
