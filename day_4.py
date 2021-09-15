from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("https://www.ctrip.com/")  # 打开浏览器
sleep(2)
driver.find_element_by_link_text('旅游').click()  # 点击旅游
sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[3]/div[1]/div[2]/ul/li[1]/h3/a').click()  # 点击景点
driver.switch_to.window(driver.window_handles[-1])  # 切换页面
driver.implicitly_wait(5)
driver.find_element_by_class_name('date_num').click()  # 点击时间
sleep(2)
driver.switch_to.frame("window_scrollTo(0,800)")  # 滚动
sleep(2)
driver.find_element_by_link_text('立即预订').click()  # 点击立即预定

