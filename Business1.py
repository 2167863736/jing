from time import sleep
from Test_run import base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Base(base):
    jd = (By.CLASS_NAME, 'link-login')
    jd1 = (By.LINK_TEXT, 'QQ')
    jd2 = (By.NAME, 'ptlogin_iframe')
    jd3 = (By.ID, 'switcher_plogin')
    jd4 = (By.CSS_SELECTOR, '#u')
    jd5 = (By.XPATH, '//*[@id="p"]')
    # ----------搜索----------
    ss = (By.ID, 'key')
    ss1 = (By.CLASS_NAME, 'button')

    def gr(self):
        self.find_element(*self.jd).click()  # 点击登录

    def qqdl(self):
        self.find_element(*self.jd1).click()  # 点击QQ登录

    def kuan(self):
        jia = self.find_element(*self.jd2)  # frame框架
        self.driver.switch_to.frame(jia)

    def zhmm(self):
        self.find_element(*self.jd3).click()  # 点击账号密码登录

    def zhang(self):
        self.find_element(*self.jd4).send_keys('2167863736')  # 输入账号

    def mima(self):
        self.find_element(*self.jd5).send_keys('ji20020812')  # 输入密码

    def dengl(self):
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located((By.ID, 'login_button'))).click()
        self.driver.switch_to.default_content()
    def Seal1(self):# -----------------登录----------------------
        self.open_url("https://www.jd.com/")
        self.gr()
        sleep(2)
        self.qqdl()
        sleep(2)
        self.kuan()
        sleep(2)
        self.zhmm()
        sleep(2)
        self.zhang()
        sleep(2)
        self.mima()
        sleep(2)
        self.dengl()