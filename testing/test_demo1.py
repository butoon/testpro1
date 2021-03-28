import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo1(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, 'kw').click()
        self.driver.find_element(By.ID, 'kw').send_keys('霍格沃兹测试学院')
        self.driver.find_element(By.ID, 'su').click()
        #time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, '霍格沃兹测试学院 – 测试开发工程师的黄埔军校').click()

def test_wework():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    driver.find_element_by_id('menu_contacts').click()
    ele = (By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(ele))
    while True:
        driver.find_element(*ele).click()
        element = driver.find_elements_by_id('username')
        if len(element) > 0:
            break
    #  driver.find_elements_by_xpath('//*[@class="ww_operationBar"]/a')[0].click()
    # self.driver.find_element_by_link_text('添加成员').click()
    driver.find_element_by_id('username').send_keys('uuss')
    # driver.find_element_by_id('memberAdd_english_name').click()
    driver.find_element_by_id('memberAdd_english_name').send_keys('sdyuvweo2')
    driver.find_element_by_id('memberAdd_acctid').send_keys('123es72')
    driver.find_element_by_id('memberAdd_phone').send_keys('13612832391')
    driver.find_element_by_id('memberAdd_title').send_keys('测试员05')
    #driver.find_element_by_link_text('保存').click()
    driver.find_element_by_css_selector('.js_btn_save').click()
    time.sleep(1)
    eles = driver.find_elements_by_css_selector('.member_colRight_memberTable_td:nth-child(2)')
    name_list = []
    for value in eles:
        print(value.get_attribute('title'))
        name_list.append(value.get_attribute('title'))
    assert 'uuss' in name_list
    print(name_list)



class TestAddUser():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_get_cookie(self):
        #self.driver.get('https://work.weixin.qq.com/')
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        cookies = driver.get_cookies()
        with open('data.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(cookies, f)
    def test_login(self):
        # /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
        # self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        # with open("data.yaml", encoding='utf-8') as f:
        #     cookies = yaml.safe_load(f)
        # for cookie in cookies:
        #     # 把cookie传给driver
        #     self.driver.add_cookie(cookie)
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id('menu_contacts').click()
        while True:
            ele = self.driver.find_element_by_css_selector('.ww_operationBar .js_add_member')
            ele.click()
            element = self.driver.find_element_by_id('username')
            if element > 0:
                break
        #  driver.find_elements_by_xpath('//*[@class="ww_operationBar"]/a')[0].click()
        #self.driver.find_element_by_link_text('添加成员').click()
        self.driver.find_element_by_id('username').send_keys('babby1')
        # driver.find_element_by_id('memberAdd_english_name').click()
        self.driver.find_element_by_id('memberAdd_english_name').send_keys('sdyueo2')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('123s72')
        self.driver.find_element_by_id('memberAdd_phone').send_keys('13612839300')
        self.driver.find_element_by_id('memberAdd_title').send_keys('测试员04')
        time.sleep(2)
        self.driver.find_element_by_link_text('保存').click()
        assert '测试成功'
    #
    # def test_adduser(self):
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #     self.driver.find_element_by_id('menu_contacts').click()
    #     time.sleep(1)
    #     # driver.find_elements_by_xpath('//*[@class="ww_operationBar"]/a')[0].click()
    #     self.driver.find_element_by_link_text('添加成员').click()
    #     self.driver.find_element_by_id('username').send_keys('SUN')
    #     # driver.find_element_by_id('memberAdd_english_name').click()
    #     self.driver.find_element_by_id('memberAdd_english_name').send_keys('summer')
    #     self.driver.find_element_by_id('memberAdd_acctid').send_keys('638234')
    #     self.driver.find_element_by_id('memberAdd_phone').send_keys('13612839356')
    #     self.driver.find_element_by_id('memberAdd_title').send_keys('测试员02')
    #     time.sleep(2)
    #     self.driver.find_element_by_link_text('保存').click()
    #     assert '测试成功'




















