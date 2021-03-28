import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_web.testcase.basepage import BasePage


class ContactPage(BasePage):
    def click_add_member(self):
        from selenium_web.page.add_member_page import AddMemberPage
        # ele = (By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
        ele = (By.CSS_SELECTOR, '.index_service_cnt .index_service_cnt_itemWrap')
        self.wait_for_click(ele, 10)
        while True:
            self.find(By.CSS_SELECTOR, '.index_service_cnt .index_service_cnt_itemWrap').click()
            element = self.finds(By.ID, 'username')
            if len(element) > 0:
                break
        return AddMemberPage(self.driver)

    def get_member(self):
        time.sleep(1)
        eles = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        name_list = []
        for value in eles:
            print(value.get_attribute('title'))
            name_list.append(value.get_attribute('title'))
        return name_list