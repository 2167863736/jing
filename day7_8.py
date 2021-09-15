from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get("https://www.ctrip.com/")  # 打开浏览器
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="nav_gentuan"]').click()  # 点击跟团游
driver.implicitly_wait(5)
# driver.find_element_by_class_name("s_vca_no_dest").click()
driver.find_element_by_class_name("search_txt").send_keys('秦皇岛')
sleep(1)
driver.find_element_by_css_selector('.search_txt').send_keys(Keys.CONTROL,'A')  # 全选
sleep(2)
driver.find_element_by_css_selector('.search_txt').send_keys(Keys.CONTROL,'C')  # 复制
sleep(2)
driver.find_element_by_link_text('自由行').click()  # 点击自由行
sleep(2)
driver.find_element_by_class_name('search_txt').send_keys(Keys.CONTROL,'V')  # 粘贴
sleep(2)
driver.find_element_by_class_name('search_txt').send_keys(Keys.ENTER)  # 输入框做回车