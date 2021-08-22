from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException


WEBDRIVER_PATH = "/Users/patrickmenendez/PycharmProjects/ig_bot/chromedriver"
URL = "https://www.instagram.com/"

# Setting up web driver
options = webdriver.ChromeOptions()
mobile_emulation = {"deviceName": "iPhone X"}
options.add_argument("--disable-notifications")
options.add_experimental_option("mobileEmulation",mobile_emulation)

driver = webdriver.Chrome(WEBDRIVER_PATH, options=options)


def select_login():
    # Opening webpage
    driver.get(URL)
    # locate login items
    mobile_login_button_xpath = "/html/body/div[1]/section/main/article/div/div/div/div[3]/button[1]"
    try:
        mobile_login_button = driver.find_element_by_xpath(mobile_login_button_xpath)
    except:
        select_login()
    else:
    # change page to login
        mobile_login_button.click()


def insert_email():
    email_input_x_path = "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input"

    try:
        print("attempting to find email xpath")
        email_input = driver.find_element_by_xpath(email_input_x_path)
    except:
        insert_email()
    else:
        email_input.send_keys("allprogrammingmx@gmail.com")
        print("email inserted")


def insert_password():
    password_input_x_path = "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input"
    try:
        password_input = driver.find_element_by_xpath(password_input_x_path)
    except:
        insert_password()
    else:
        password_input.send_keys("pmr292001")


def click_login():
    login_button_x_path = "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button"
    try:
        login_button = driver.find_element_by_xpath(login_button_x_path)
    except:
        click_login()
    login_button.click()


def login():
    select_login()
    insert_email()
    insert_password()
    click_login()

    time.sleep(2)

    #not_not_button_xpath = "/html/body/div[1]/section/main/div/div/div/button"
    #not_not_button = driver.find_element_by_xpath(not_not_button_xpath)
    #not_not_button.click()

    #time.sleep(5)
    #cancel_button_xpath = "/html/body/div[4]/div/div/div/div[3]/button[2]"
    #cancel_button = driver.find_element_by_xpath(cancel_button_xpath)
    #cancel_button.click()


def find_account(username):
    URL = f"https://www.instagram.com/{username}/"
    driver.get(URL)
    time.sleep(2)


def get_username_element(index):
    username_xpath = f"/html/body/div[1]/section/main/div/ul/div/li[{index}]/div/div[1]/div[2]/div[1]/a"
    username = driver.find_element_by_xpath(username_xpath).text
    return username


def current_user_is_self(username):
    if username == "allprogrammingmx":
        print("This is you")
        return True


def get_button(index):
    xpath = f"/html/body/div[1]/section/main/div/ul/div/li[{index}]/div/div[2]/button"
    button = driver.find_element_by_xpath(xpath)
    print(button.text)
    return button


def current_user_is_already_followed(button):
    if button.text != "Follow":
        print("User was already followed, skipping it")
        # driver.execute_script(f"window.scrollTo(0, {scroll_height} * {index} )")


def click_follow(button):
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


def __scroll_up(index, scroll_height):
    driver.execute_script(f"window.scrollTo(0, {scroll_height * 5} * {index})")


def go_to_followers():
    followers_button_xpath = "/html/body/div[1]/section/main/div/ul/li[2]/a"
    driver.find_element_by_xpath(followers_button_xpath).click()


def init_follow():
    index = 1
    scroll_height = 38
    go_to_followers()
    time.sleep(2)
    for _ in range(200):

        username = get_username_element(index)
        # check if current username is the account itself
        if current_user_is_self(username):
            index += 1
            continue

        button = get_button(index)
        # check if the user is already followed
        if current_user_is_already_followed(button):
            index += 1
            continue

        time.sleep(2)
        try:
            click_follow(button)
            # If the button is not found, scroll
        except ElementClickInterceptedException:
            index += 1
            __scroll_up(index, scroll_height)
        index += 1
        time.sleep(0.5)


if __name__ == '__main__':

    login()
    find_account("node.js_learning")
    init_follow()

