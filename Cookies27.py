from selenium import webdriver
from selenium.webdriver import ActionChains
import time


driver=webdriver.Chrome(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")

driver.get("https://www.eenadu.net/")

driver.maximize_window()
print("Deleting the cookies ")
driver.delete_all_cookies()
time.sleep(3)

# Getting all the cookies
print("Getting all the cookies ")

totalCookies=driver.get_cookies()
print(len(totalCookies))
print(totalCookies)


# Adding the cookie

print("Adding the cookie ")
newCookie = {'name':'veera','value':'123456'}
driver.add_cookie(newCookie)


# Getting all the cookies
print("Getting all the cookies after adding ")
totalCookies=driver.get_cookies()
print(len(totalCookies))
print(totalCookies)

print("Deleting the cookie ")
# Deleting the cookie
driver.delete_cookie(newCookie)
time.sleep(3)


print("Deleting all the cookies ")
driver.delete_all_cookies()
time.sleep(3)

# Getting all the cookies again
print("Getting all the cookies after deleting the latest ")
totalCookies=driver.get_cookies()
print(len(totalCookies))
print(totalCookies)
driver.close()