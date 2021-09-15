from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.alert import Alert
# execute
driver=webdriver.Firefox()
driver.get("https://www.ctrip.com/")  # 打开浏览器
# -----------QQ登录-------------
driver.find_element_by_class_name('set-text').click()  # 点击《您好，请先登录》
sleep(2)  # 强制等待时间
driver.find_element_by_xpath('//*[@id="loginbanner"]/div[2]/a[2]').click()   # 点击QQ登录
driver.implicitly_wait(5)  # 显示等待时间
driver.minimize_window()  # 最小化
driver.maximize_window()  # 最大化
kj = driver.find_element_by_id('ptlogin_iframe')
driver.execute_script(kj)
sleep(2)
driver.find_element_by_css_selector('#switcher_plogin').click()  # 点击账号密码登录
sleep(2)
driver.back()  # 后退
driver.forward()  # 前进
driver.find_element_by_id("u").send_keys("2167863736")
sleep(2)
driver.find_element_by_name("p").send_keys("ji20020812")
sleep(2)
driver.find_element_by_class_name('btn')  # 点击登录
driver.quit()  # 关闭




