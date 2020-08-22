from datetime import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()
print(driver.current_url)
print("Veera Automation")
print("Veera Pulapakura is a nice person")
print("Mahitha Pulapakura is Dummy ")
print("Manogna Pulapakura is Dummy too")
print("Madhuri Sundarapalli is Dummy too")

time.sleep(5)
driver.close()


