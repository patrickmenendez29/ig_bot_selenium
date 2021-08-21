from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException
from enum import Enum


class web_drivers(Enum):
    CHROME = 0
    FIREFOX = 1


class SeleniumManager:

    INSTAGRAM_URL = "https://www.instagram.com/"

    def __init__(self, driver_path, web_driver: web_drivers):
        self.clicks = 0
        self.index = 0
        self.config = {}
        self.driver_path = driver_path
        self.driver: web_drivers = web_driver

    def set_configuration(self, key: str,  value):
        self.config[key] = value


