#!/usr/bin/env python
#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
import unittest,time
from util import drivers

class checkbaidu(unittest.TestCase):
	def setUp(self):
		d = drivers()
		self.driver=d.driver
		self.driver.implicitly_wait(5)
		self.driver.get("https://www.baidu.com")

	def test_tools(self):
+++1

	def tearDown(self):
		self.driver.quit()

if __name__=="__main__":
        unittest.main()
