# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

"""
#获得cookie信息
cookie = driver.get_cookies()

#将获得的cookie打印
print cookie
"""

#向cookie的name和value添加会话信息
driver.add_cookie({'name':'key-aaaaaaa','value':'value-bbbb'})

#遍历cookie中的name和value信息打印，还有上面添加的信息
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'],cookie['value'])


driver.quit()