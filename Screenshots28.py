from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")

driver.get("https://www.eenadu.net/")

driver.get_screenshot_as_file("C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\Screenshots\\6.jpg")

#driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\Screenshots\\5.png")
time.sleep(3)

