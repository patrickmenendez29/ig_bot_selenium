from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException
from enum import Enum


class web_drivers(Enum):
    CHROME = 0
    FIREFOX = 1


class SeleniumManager:

    INSTAGRAM_URL = "https://www.instagram.com/"

    def __init__(self, webdriver_path, target_account):
        self.webdriver_path = webdriver_path
        self.driver = self.config()
        self.index = 1
        self.current_username = None
        self.target_account = target_account

    # configure the manager
    def config(self):
        # Setting up web driver
        options = webdriver.ChromeOptions()
        mobile_emulation = {"deviceName": "iPhone X"}
        options.add_argument("--disable-notifications")
        options.add_experimental_option("mobileEmulation", mobile_emulation)

        driver = webdriver.Chrome(self.webdriver_path, options=options)

        return driver

    def select_login(self):
        # Opening webpage
        self.driver.get(SeleniumManager.INSTAGRAM_URL)
        # locate login items
        mobile_login_button_xpath = "/html/body/div[1]/section/main/article/div/div/div/div[3]/button[1]"
        try:
            mobile_login_button = self.driver.find_element_by_xpath(mobile_login_button_xpath)
        except:
            self.select_login()
        else:
            # change page to login
            mobile_login_button.click()

    def insert_email(self):
        email_input_x_path = "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input"

        try:
            print("attempting to find email xpath")
            email_input = self.driver.find_element_by_xpath(email_input_x_path)
        except:
            self.insert_email()
        else:
            email_input.send_keys("allprogrammingmx@gmail.com")
            print("email inserted")

    def insert_password(self):
        password_input_x_path = "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input"
        try:
            password_input = self.driver.find_element_by_xpath(password_input_x_path)
        except:
            self.insert_password()
        else:
            password_input.send_keys("pmr292001")

    def click_login(self):
        login_button_x_path = "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button"
        try:
            login_button = self.driver.find_element_by_xpath(login_button_x_path)
        except:
            self.click_login()
        login_button.click()

    def login(self):
        self.select_login()
        self.insert_email()
        self.insert_password()
        self.click_login()

        time.sleep(2)

    def find_account(self):
        URL = f"https://www.instagram.com/{self.target_account}/"
        self.driver.get(URL)
        time.sleep(2)

    def get_username_element(self):
        username_xpath = f"/html/body/div[1]/section/main/div/ul/div/li[{self.index}]/div/div[1]/div[2]/div[1]/a"
        username = self.driver.find_element_by_xpath(username_xpath).text
        return username

    def current_user_is_self(self):
        if self.current_username == "allprogrammingmx":
            print("This is you")
            return True

    def get_button(self):
        xpath = f"/html/body/div[1]/section/main/div/ul/div/li[{self.index}]/div/div[2]/button"
        button = self.driver.find_element_by_xpath(xpath)
        print(button.text)
        return button

    def current_user_is_already_followed(self, button):
        if button.text != "Follow":
            print("User was already followed, skipping it")
            # driver.execute_script(f"window.scrollTo(0, {scroll_height} * {index} )")

    def click_follow(self, button):
        # current user status is unknown, set it to false
        following = False
        # while the account is not following the user, do the following:
        while not following:
            # click the follow button and wait 3 seconds for the text to change
            button.click()
            time.sleep(3)
            # if the text changes to "Following" or "Requested", continue with the next row
            if button.text == "Following" or button.text == "Requested":
                following = True

    def __scroll_up(self, scroll_height):
        self.driver.execute_script(f"window.scrollTo(0, {scroll_height * 5} * {self.index})")

    def go_to_followers(self):
        followers_button_xpath = "/html/body/div[1]/section/main/div/ul/li[2]/a"
        self.driver.find_element_by_xpath(followers_button_xpath).click()

    def init_follow(self):
        scroll_height = 38
        self.go_to_followers()
        time.sleep(2)
        for _ in range(200):

            self.current_username = self.get_username_element()
            # check if current username is the account itself
            if self.current_user_is_self():
                self.index += 1
                continue

            button = self.get_button()
            # check if the user is already followed
            if self.current_user_is_already_followed(button):
                self.index += 1
                continue

            time.sleep(2)

            try:
                self.click_follow(button)
                # If the button is not found, scroll
            except ElementClickInterceptedException:
                self.index += 1
                self.__scroll_up(scroll_height)
            self.index += 1
            time.sleep(0.5)


