#!/usr/bin/env python

'''
page.py
October 12th, 2011
'''

import time
import base64
'''import yaml'''
import re

class Page(object):
    
    def __init__(self, testsetup):
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.selenium = testsetup.selenium

    @property
    def is_the_current_page(self):
        page_title = self.selenium.title
        if not page_title == self._page_title:
            self.record_error()
            print "Expected page title: %s" % self._page_title
            raise Exception("Expected page title does not match actual page title.")
        else:
            return True

    def is_element_visible(self, locator):
        try:
            self.selenium.find_element(*locator)
            return True
        except:
            return False

    def record_error(self):
        print "-------------------"
        print "Error at: %s" % self.selenium.current_url
        print "Page title: %s" % self.selenium.title.encode('utf-8')
        print "-------------------"
        filename = "%s.png" % str(time.time()).split('.')[0]

        print "Screenshot of error in file: %s" % filename
        f = open(filename, "wb")
        f.write(base64.decodestring(self.selenium.get_screenshot_as_base64()))
        f.close()
