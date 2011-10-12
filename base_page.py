#!/usr/bin/env python

from selenium.webdriver.common.by import By

from page import Page
import personal_tools_region


class BasePage(Page):

    _page_title_locator = (By.CSS_SELECTOR, "#page-title")

    @property
    def personal_tools_region(self):
        return personal_tools_region.PersonalToolsRegion(self.testsetup)

    @property
    def page_title(self):
        return self.selenium.find_element(*self._page_title_locator).text
