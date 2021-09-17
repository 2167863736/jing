import unittest,HTMLTestRunner_cn
from selenium import webdriver
from Business1 import Base

class cun(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Firefox()
    def tearDown(self) -> None:
        pass
    def test_01(self):
        po=Base(self.driver)
        po.Seal1()
# if __name__ == '__main__':
    # unittest.main()

runner=HTMLTestRunner_cn.HTMLTestRunner(stream=open("1.html","wb"),
                                        title="测试报告",
                                        description="描述一下！")
unittest.main(testRunner=runner)