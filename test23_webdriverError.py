# coding=utf-8
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")

#捕捉异常
try:
    browser.find_element_by_id("kwss").send_keys("selenium")
    browser.find_element_by_id("su").click()

except:
    browser.get_screenshot_as_file("C:\Users\jiao.fang.jiaofang\Desktop\error.png")

browser.quit()