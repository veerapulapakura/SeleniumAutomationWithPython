from datetime import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")

ele = driver.find_element_by_name("signup")
print(ele.is_displayed())
print(ele.is_enabled())
time.sleep(2)


ele = driver.find_element_by_xpath("//*[@id='eid']/input")
print(ele.is_displayed())
print(ele.is_enabled())
ele.send_keys("veera.ratna@gmail.com")
time.sleep(2)

ele = driver.find_element_by_name("radiooptions")
print(ele.is_displayed())
print(ele.is_enabled())
print(ele.is_selected())

time.sleep(2)



driver.close()
