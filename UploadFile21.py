from selenium import webdriver
from selenium.webdriver import ActionChains
import time


driver=webdriver.Chrome(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.execute_script("window.scrollBy(0,1000)","")

driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")

time.sleep(10)
