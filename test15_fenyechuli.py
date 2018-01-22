# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://pan.baidu.com/")

#登录系统
driver.find_element_by_id("userName").click()
driver.find_element_by_id("userName").send_keys("username")
driver.find_element_by_id("user_pwd").clear()
driver.find_element_by_id("user_pwd").send_keys("password")
driver.find_element_by_id("user_pwd").click()

#获取所用分页的数量，并打印
total_pages = len(driver.find_elements_by_tag_name("select").find_elements_by_tag_name("option"))


#再次获取所分页，并执行循环翻页操作
pages = driver.find_elements_by_tag_name("select").find_elements_by_tag_name("option")
for page in pages:
    page.click()
    time.sleep(3)

driver.quit()