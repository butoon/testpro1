from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_web.page.contact_page import ContactPage
from selenium_web.testcase.basepage import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def goto_contact_page(self):
        #self.find(By.ID, 'menu_contacts').click()
        return ContactPage(self.driver)