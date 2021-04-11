from selenium import webdriver
import time

WEBDRIVER_PATH = "/Users/patrickmenendez/PycharmProjects/ig_bot/chromedriver 3"
URL = "https://www.instagram.com/"

# Setting up web driver
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(WEBDRIVER_PATH, options=options)


def login():
    # Opening webpage
    driver.get(URL)

    # locate login items
    email_input_x_path = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input"
    email_input = driver.find_element_by_xpath(email_input_x_path)

    password_input_x_path = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input"
    password_input = driver.find_element_by_xpath(password_input_x_path)

    login_button_x_path = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button"
    login_button = driver.find_element_by_xpath(login_button_x_path)

    # entering input and logging in

    email_input.send_keys("allprogrammingmx@gmail.com")
    password_input.send_keys("pmr292001")
    login_button.click()
    time.sleep(5)

def find_account(username):
    not_now_button_x_path = "/html/body/div[1]/section/main/div/div/div/div/button"
    not_now_button = driver.find_element_by_xpath(not_now_button_x_path)

    not_now_button.click()

    search_bar_x_path = "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input"
    search_bar = driver.find_element_by_xpath(search_bar_x_path)

    search_bar.send_keys(username)
    time.sleep(5)

    target_x_path = "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]"

    target = driver.find_element_by_xpath(target_x_path)

    target.click()
    time.sleep(5)
    followers_button_x_path = "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a"
    followers_button = driver.find_element_by_xpath(followers_button_x_path)
    time.sleep(5)
    followers_button.click()
    time.sleep(5)

if __name__ == '__main__':

    login()
    find_account("itchallenges")

