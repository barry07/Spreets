#!/usr/bin/env python

import pytest
import py

from selenium import webdriver


def pytest_runtest_setup(item):
    item.host = item.config.option.host
    item.browser_name = item.config.option.browser_name
    item.browser_version = item.config.option.browser_version
    item.platform = item.config.option.platform
    item.port = item.config.option.port
    TestSetup.base_url = item.config.option.base_url
    TestSetup.skip_selenium = True

    if item.browser_name is None:
        raise Exception("You must specify a browser name.")
    if item.browser_version is None:
        raise Exception("You must specify a browser version.")
    if item.platform is None:
        raise Exception("You must specify a platform.")

    if not "skip_selenium" in item.keywords:
        TestSetup.skip_selenium = False
        
        try:
            capabilities = getattr(webdriver.DesiredCapabilities, item.browser_name.upper())
            capabilities["version"] = item.browser_version
            capabilities["platform"] = item.platform.upper()
            TestSetup.selenium = webdriver.Remote(
                command_executor = "http://%s:%s/wd/hub" % (item.host, item.port),
                desired_capabilities = capabilities)
        except AttributeError:
            valid_browsers = [attr for attr in dir(webdriver.DesiredCapabilities) if not attr.startswith('__')]
            raise AttributeError("Invalid browser name: '%s'. Valid options are: %s" % (item.browser_name, ", ".join(valid_browsers)))


def pytest_runtest_teardown(item):
    if hasattr(TestSetup, "selenium") and not TestSetup.skip_selenium:
        TestSetup.selenium.quit()


def pytest_funcarg__testsetup(request):
    return TestSetup(request)


def pytest_addoption(parser):
    parser.addoption("--host",
                     action="store",
                     default="localhost",
                     help="host that Selenium server is listening on")
    parser.addoption("--port",
                     action="store",
                     default="4444",
                     help="port that Selenium server is listening on")
    parser.addoption("--browser-name",
                     action="store",
                     dest="browser_name",
                     help="target browser")
    parser.addoption("--browser-version",
                     action="store",
                     dest="browser_version",
                     help="target browser version")
    parser.addoption("--platform",
                     action="store",
                     help="target platform")
    parser.addoption("--base-url",
                     action="store",
                     dest="base_url",
		     default="http://spreets.local.au",
                     help="base URL for the application under test")


class TestSetup:
    def __init__(self, request):
        self.request = request

