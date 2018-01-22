# coding=utf-8
from selenium import webdriver
import os,time

driver = webdriver.Firefox()
file_path = "file://" + os.path.abspath("drop_down.html")
driver.get(file_path)
time.sleep(5)

#先定位到下拉框ShippingMethod
m = driver.find_element_by_id("ShippingMethod")
#再点击下来框中的选项
m.find_element_by_xpath("//option[@value='11.61']").click()
time.sleep(4)

driver.quit()