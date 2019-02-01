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
		self.driver.get("https://www.baidu.com")
		self.driver.find_element_by_id("kw").send_keys("软件测试")
		self.driver.find_element_by_id("su").click()
		ActionChains(self.driver).move_to_element(self.driver.find_element_by_name("tj_settingicon")).perform()
		self.driver.find_element_by_link_text("高级搜索").click()
		self.assertTrue(self.driver.find_element_by_id("q5_0").is_selected())


	def tearDown(self):
		self.driver.quit()

if __name__=="__main__":
        unittest.main()
