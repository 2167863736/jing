class base():
    def __init__(self,driver):
        self.driver=driver
    def open_url(self,url):
        self.driver.get(url)
    def find_element(self,*col):
        return self.driver.find_element(*col)

