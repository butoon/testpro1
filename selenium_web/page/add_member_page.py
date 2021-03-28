from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_web.page.contact_page import ContactPage
from selenium_web.testcase.basepage import BasePage


class AddMemberPage(BasePage):
    _ele_name = (By.ID, 'username')
    _ele_id = (By.ID, 'memberAdd_acctid')
    _ele_phone = (By.ID, 'memberAdd_phone')

    def add_member(self, name, id, phone ):
        self.find(*self._ele_name).send_keys(name)
        self.find(*self._ele_id).send_keys(id)
        self.find(*self._ele_phone).send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return ContactPage(self.driver)