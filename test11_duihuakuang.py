# coding:utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#点击登录
driver.find_element_by_name("tj_login").click()

#通过二次定位找到用户名输入框
div = driver.find_element_by_class_name("tag-content").find_element_by_name("userName")
div.send_keys("username")

#输入登录密码
driver.find_element_by_name("password").send_keys("password")

#点击登录
driver.find_element_by_id("TANGRAM_PSP_10_submit").click()

driver.quit()