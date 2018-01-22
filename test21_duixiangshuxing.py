# coding=utf-8
from selenium import webdriver
import os,time


source = open("C:\Users\jiao.fang.jiaofang\PycharmProjects\untitled1\data.txt")
values = source.readlines()
source.close()

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
for value in values:
    driver.find_element_by_id("kw").send_keys(value)
    driver.find_element_by_id("su").click()
    time.sleep(5)
    driver.find_element_by_id("kw").clear()

driver.quit()

