from selenium import webdriver
from pytest_package.pages.welcome_page import WelcomePage
import unittest
import time
import pytest


class TestWelcome:

    def test_welcome_home(self, setup):
        wc = WelcomePage(setup)
        wc.get_title()
        wc.checkWelcomeLinks()
