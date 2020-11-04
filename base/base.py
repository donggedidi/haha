from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver=driver

    def base_fine_element(self,loc,timeout=10,poll_frequency=1):
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(*loc))

    def base_click(self,loc):
        self.base_fine_element(loc).click()

    def base_input(self,loc,value):
        self.base_fine_element(loc).send_keys(value)

    def base_get_text(self,loc):
        return self.base_fine_element(loc).text