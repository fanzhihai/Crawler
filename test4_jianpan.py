# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")
time.sleep(5)

#删除多余的m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(5)

#输入空格键+教程
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
time.sleep(5)

#ctrl+a 全选
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")
time.sleep(5)

#ctrl+x 剪切
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"x")
time.sleep(5)

#ctrl+v 重新输入
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"v")
time.sleep(5)

#enter命令
driver.find_element_by_id("kw").send_keys(Keys.ENTER)
time.sleep(5)

driver.quit()