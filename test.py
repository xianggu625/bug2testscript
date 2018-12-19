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
		self.driver.get("http://127.0.0.1:8000")
		self.driver.find_element_by_id("id_username").clear()
		self.driver.find_element_by_id("id_username").send_keys("cindy")
		self.driver.find_element_by_id("id_password").clear()
		self.driver.find_element_by_id("id_password").send_keys("123456")
		csrftoken=self.driver.find_element_by_name("csrfmiddlewaretoken").get_attribute("value")
		self.driver.add_cookie({"name":"csrftoken","value":csrftoken})
		self.driver.find_element_by_class_name("form-signin").submit()
		time.sleep(3)
		self.assertEqual("电子商务系统",self.driver.title)

	def tearDown(self):
		self.driver.quit()

if __name__=="__main__":
        unittest.main()
