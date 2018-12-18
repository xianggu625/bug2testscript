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
		self.driver.get("https://www.baidu.com")
		self.driver.find_element_by_id("kw").clear()
		self.driver.find_element_by_id("kw").send_keys("软件测试")
		self.driver.find_element_by_id("su").click()
		time.sleep(5)
		self.assertEqual(self.driver.title,"软件测试_百度搜索")

	def tearDown(self):
		self.driver.quit()

if __name__=="__main__":
        unittest.main()
