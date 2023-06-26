import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class Activity2():
    def test(self):
        base_url="https://www.google.co.in/"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)
        #Search box
        searchbox=driver.find_element(By.CLASS_NAME,"gLFyf")
        searchbox.send_keys("Online python compiler")
        #open online python compiler
        driver.get("https://www.programiz.com/python-programming/online-compiler/")
        #select all content
        driver.find_element(By.CLASS_NAME,"ace_text-input").send_keys(Keys.CONTROL+"a")
        time.sleep(2)
        #delete selected items
        driver.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.DELETE)
        #read the python file
        file = open("file.py","r")
        #pass the code in editor
        driver.find_element(By.CLASS_NAME,"ace_text-input").send_keys(file.read())
        file.close()
        #click the Run button
        driver.find_element(By.CLASS_NAME,"run-text").click()
        time.sleep(30)
act2=Activity2()
act2.test()