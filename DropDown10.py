from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")

dropdown=driver.find_element_by_id('Skills')
ele = Select(dropdown)
print(len(ele.options))

ele.select_by_index(2)

ele.select_by_visible_text('C')

ele.select_by_value('C++')

allOptions = ele.options
for eachvalue in allOptions:
    print(eachvalue.text)

