#!/usr/bin/env python

from selenium.webdriver.common.by import By

from page import Page


class BasePage(Page):

    _page_title_locator = (By.CSS_SELECTOR, "#page-title")

    @property
    def page_title(self):
        return self.selenium.find_element(*self._page_title_locator).text
