from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()
driver.get("https://www.ctrip.com/")  # 打开浏览器
driver.implicitly_wait(5)
xt=driver.find_element_by_xpath('/html/body/div[2]/div/ul[2]/li[5]/a/span')
ActionChains(driver).move_to_element(xt).perform()  # 悬停
sleep(2)
driver.find_element_by_link_text('我的优惠券').click()  # 点击我的优惠券

