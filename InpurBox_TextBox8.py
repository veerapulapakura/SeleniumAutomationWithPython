from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
inputboxes=driver.find_elements(By.CLASS_NAME,'veeera')
print(len(inputboxes))
driver.implicitly_wait(5)
driver.close()
