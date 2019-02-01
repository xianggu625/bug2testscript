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
		self.driver.get("https://www.jd.com/")
		self.driver.find_element_by_id("key").clear()
		self.driver.find_element_by_id("key").send_keys("巧克力")
		self.driver.find_element_by_class_name("button").click()
		time.sleep(3)
		self.driver.find_element_by_class_name("p-tag").click()
		time.sleep(3)
		current_windows = self.driver.current_window_handle
		all_handles = self.driver.window_handles
		for handle in all_handles:
			if handle != current_windows:
				self.driver.switch_to.window(handle)
				break
		for handle in all_handles:
			if handle == current_windows:
				self.driver.switch_to.window(handle)
				self.driver.close()
				break
		for handle in all_handles:
			if handle != current_windows:
				self.driver.switch_to.window(handle)
				break
		self.assertIn("巧克力",self.driver.title)


	def tearDown(self):
		self.driver.quit()

if __name__=="__main__":
        unittest.main()
