# coding=utf-8
from selenium import webdriver
import time,os

driver = webdriver.Firefox()
file_path = "file://" + os.path.abspath("upload_file.html")
driver.get(file_path)

#定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('C:\Users\jiao.fang.jiaofang\PycharmProjects\untitled1\upload_file.txt')
time.sleep(3)

driver.quit()