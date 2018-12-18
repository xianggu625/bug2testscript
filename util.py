#!/usr/bin/env python
#coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class drivers:
        def __init__(self):
                f = open("info.txt", "r")
                driverPach = "C:\\Lib\\";
                brower = f.readline()
                f.close()
                if brower.lower() == "ie":
                        self.driver = webdriver.Ie(executable_path=driverPach+"IEDriverServer.exe")
                if brower.lower() == "firefox":
                        self.driver = webdriver.Firefox(executable_path=driverPach+"geckodriver.exe")
                if brower.lower() == "chrome":
                        self.driver = webdriver.Chrome(executable_path=driverPach+"chromedriver.exe")
                if brower.lower() == "edge":
                        self.driver = webdriver.Edge(executable_path=driverPach+"MicrosoftWebDriver.exe")
                self.driver.maximize_window()
