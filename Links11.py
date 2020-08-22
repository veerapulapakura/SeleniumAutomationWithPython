from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")

totallinks=driver.find_elements(By.TAG_NAME,'a')
print("Total no of links: ",len(totallinks))

for eachvalue in totallinks:
    print(eachvalue.text)

driver.find_element_by_link_text("Video").click()

driver.find_element_by_partial_link_text("Reg").click()
time.sleep(5)

driver.close()