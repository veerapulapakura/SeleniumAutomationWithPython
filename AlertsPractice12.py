from selenium import webdriver
import time

driver= webdriver.Chrome(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\drivers\\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()

time.sleep(6)

#driver.switch_to_alert().accept()

#driver.switch_to_alert().dismiss()

driver.switch_to.alert.dismiss()

driver.close()