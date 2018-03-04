#!/usr/bin/env python3
from selenium import webdriver


class BrowserFactory:
    def __init__(self):
        self.__chromeDriverPath = "D:/Playground_Python/chromedriver_win32/chromedriver.exe"

    @property
    def get_chrome_driver(self):
        driver = webdriver.Chrome(self.__chromeDriverPath)
        return driver
