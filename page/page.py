import time

import allure

import page
from base.base import Base


class Page(Base):
    def page_click_add(self):
        self.base_click(page.add_btn)
    @allure.step(title="输入姓名")
    def page_input_name(self,name):
        self.base_input(page.name,name)

    def page_input_phone(self,phone):
        self.base_input(page.phone,phone)

    def page_click_back(self):
        self.base_click(page.back_btn)

    def page_get_txt(self):
        return self.base_get_text(page.success_text)

    def page_contact(self,name,phone):
        self.page_click_add()
        self.page_input_name(name)
        self.page_input_phone(phone)
        time.sleep(3)
        self.page_click_back()

