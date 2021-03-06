# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Firefox()
file_path = 'file://' + os.path.abspath('level_locate.html')
driver.get(file_path)

#点击Link1链接
driver.find_element_by_link_text('Link1').click()

#在父亲元件下找到link为Action的子元素
menu = driver.find_element_by_id('dropdown1').find_element_by_link_text('Another action')

#将鼠标移动到子元素上
ActionChains(driver).move_to_element(menu).perform()
time.sleep(5)

driver.quit()
