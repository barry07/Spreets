#!/usr/bin/env python

import base_page


class HomePage(base_page.BasePage):

    _page_title = "Treat Yourself to $200 of Pampering for Just $59! Includes: Facial, Swedish Massage, Eye Treatment & More! - Spreets "
    _sign_in_link_locator = (By.Text, "Sign In")
    
    def go_to_home_page(self):
        self.selenium.get(self.testsetup.base_url + "/")
        self.is_the_current_page

    def click_sign_in_link(self):
        self.selenium.find_element_by_link_text(*self._sign_in_link_locator).click()
        

    
