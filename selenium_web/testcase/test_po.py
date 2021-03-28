import pytest

from selenium_web.page.main_page import MainPage


class TestLogin:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize('name, id, phone', [('lisi', 'iwde', '13546738293')])
    def test_login(self, name, id, phone):
        name_list = self.main.goto_contact_page().click_add_member().add_member(name, id, phone).get_member()
        print(name_list)[]
        assert name in name_list