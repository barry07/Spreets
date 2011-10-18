#!/usr/bin/env python

import base_page


class HomePage(base_page.BasePage):

    _page_title = "Treat Yourself to $200 of Pampering for Just $59! Includes: Facial, Swedish Massage, Eye Treatment & More! - Spreets "

    def go_to_home_page(self):
        self.selenium.get(self.testsetup.base_url + "/")
        self.is_the_current_page
