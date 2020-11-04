import pytest
import os,sys
sys.path.append(os.getcwd())
from base.base_driver import base_driver
from page.page import Page
from base.base_analyse import base_analyse
import time

class TestContact:
    def setup(self):
        self.driver=base_driver()
        self.page=Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args",base_analyse("data.yaml","test_contact"))
    def test_contact(self,args):
        self.page.page_contact(args["name"],args["phone"])
        print(self.page.page_get_txt())
        print(args["name"])
        assert args["name"]==self.page.page_get_txt()

