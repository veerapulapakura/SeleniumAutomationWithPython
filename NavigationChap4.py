from datetime import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")
# driver.get("http://demo.automationtesting.in/Register.html")
driver.get("https://www.google.co.uk/")
print(driver.title)
time.sleep(5)
driver.get("http://www.pavantestingtools.com/")
driver.maximize_window()
print(driver.title)
time.sleep(5)

driver.back()

print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)

time.sleep(5)
driver.close()
