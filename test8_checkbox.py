# coding:utf-8
from selenium import webdriver
import os
from time import sleep

driver = webdriver.Firefox()
file_path = 'file://' + os.path.abspath('checkbox.html')
driver.get(file_path)

#选择页面上所有的tag_name为input的元素,第一种方法
"""
inputs = driver.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()
"""
#第二种方法,css方法
checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()

#将最后的一个勾选去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()

sleep(10)

driver.quit()