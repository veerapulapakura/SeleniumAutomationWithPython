from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver=webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")
#driver.get("https://newtours.demoaut.com/")

# driver = webdriver.Firefox(
#     executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\geckodriver.exe")
# driver.get("https://www.google.co.uk/")

driver = webdriver.Ie(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\IEDriverServer.exe")


driver.get("https://www.google.co.uk/")

print(driver.current_url)
print(driver.title)
driver.quit()