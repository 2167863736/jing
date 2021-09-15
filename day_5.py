from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get("https://www.ctrip.com/")  # 打开浏览器
sleep(2)
driver.find_element_by_link_text('自由行').click()  # 点击自由行
sleep(2)
driver.find_element_by_css_selector('.search_txt').click()
sleep(2)
driver.find_element_by_class_name('search_txt').send_keys('南京')
sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/div/div[2]/a').click()



