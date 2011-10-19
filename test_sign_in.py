#!/usr/bin/env python

import pytest
from unittestzero import Assert
import home_page
import signin_page

class TestSignIn:
    def test_user_can_sign_in(self, testsetup):
        home_pg = home_page.HomePage(testsetup)
        home_pg.go_to_home_page()
        Assert.true(home_pg.is_the_current_page)
        '''home_pg.click_sign_in_link()

        signin_pg = signin_page.SignInPage(testsetup)
        signin_pg.sign_in()'''
