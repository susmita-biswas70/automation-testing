import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait

base_url = "https://sakshingp.github.io/assignment/login.html"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(base_url)
driver.implicitly_wait(3)
#For Login
def login_test_page():
    #Valid login
    login_page("valid_username","valid_password")
    #Invalid Login
    # login_page("","")
    # login_page("valid_username","")
    # login_page("","valid_password")

def login_page(username, password):

    # For Login Page:-
    # Username input box
    username_box = driver.find_element(By.ID, "username")
    # Password input box
    password_box = driver.find_element(By.ID, "password")
    # Login button
    login = driver.find_element(By.ID, "log-in")

    username_box.send_keys(username)
    password_box.send_keys(password)
    login.click()
    time.sleep(2)

    accualUrl="https://sakshingp.github.io/assignment/home.html"
    currentUrl=driver.current_url
    if(accualUrl==currentUrl):
        print("Successfully Login")

        # After successfully login
        # For Home Page:-
        # Click Amount header
        amount = driver.find_element(By.ID, "amount")
        amount.click()
        time.sleep(2)

        # Check the values are sorted
        transaction_amounts = driver.find_elements(By.XPATH, '//table[@id="transactionTable"]//td[4]')
        amounts = [float(amount.text) for amount in transaction_amounts]
        sorted_amounts = sorted(amounts)
        assert amounts == sorted_amounts
        print("Amounts are sorted")
    else:
        print("Invalid Login")

login_test_page()

driver.quit()