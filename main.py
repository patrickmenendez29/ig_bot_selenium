from selenium import webdriver
import time

WEBDRIVER_PATH = "/Users/patrickmenendez/PycharmProjects/ig_bot/chromedriver 3"
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

def init_follow():
    index = 1
    scroll_height = 40
    followers_button_xpath = "/html/body/div[1]/section/main/div/ul/li[2]/a"
    (followers_button := driver.find_element_by_xpath(followers_button_xpath)).click()
    time.sleep(2)
    for _ in range(200):

        username_xpath = f"/html/body/div[1]/section/main/div/ul/div/li[{index}]/div/div[1]/div[2]/div[1]/a"
        username = driver.find_element_by_xpath(username_xpath).text
        if username == "allprogrammingmx":
            print("This is you")
            index += 1
            driver.execute_script(f"window.scrollTo(0, {scroll_height} * {index})")
            continue

        xpath = f"/html/body/div[1]/section/main/div/ul/div/li[{index}]/div/div[2]/button"
        button = driver.find_element_by_xpath(xpath)
        print(button.text)

        if button.text != "Follow":
            print("User was already followed, skipping it")
            index += 1
            driver.execute_script(f"window.scrollTo(0, {scroll_height} * {index} )")
            continue

        time.sleep(2)
        button.click()
        index += 1
        time.sleep(0.5)
        driver.execute_script(f"window.scrollTo(0, {scroll_height} * {index})")



if __name__ == '__main__':

    login()
    find_account("developers.reality")
    init_follow()

