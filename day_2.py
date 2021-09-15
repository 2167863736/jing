from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.alert import Alert

driver=webdriver.Firefox()
driver.get("https://www.ctrip.com/")  # 打开浏览器
sleep(2)
driver.find_element_by_id('_allSearchKeyword').send_keys('西安')  # 输入西安
sleep(2)
driver.find_element_by_xpath('//*[@id="search_button_global"]').send_keys(Keys.ENTER)  # 回车事件

