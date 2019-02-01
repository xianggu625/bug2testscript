#!/usr/bin/env python
#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import unittest,time
from util import drivers

class checkbaidu(unittest.TestCase):
	def setUp(self):
		d = drivers()
		self.driver=d.driver
		self.driver.implicitly_wait(5)

	def test_tools(self):
		self.driver.get("http://127.0.0.1:8080/sec/33/index.html")
		element = self.driver.find_element_by_id("c1")
		if not element.is_selected():
			element.click()
		self.assertTrue(self.driver.find_element_by_id("c1").is_selected())


	def tearDown(self):
		self.driver.quit()

if __name__=="__main__":
        unittest.main()
