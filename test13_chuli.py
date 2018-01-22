# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#点击打开搜索设置
driver.find_element_by_name("tj_settingicon").click()

#获取网页上的警告信息
alter = driver.switch_to_alert()

#接收警告信息
alter.accept()

