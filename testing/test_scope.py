import pytest


@pytest.fixture(scope='class')
def contentDB():
    print('连接数据库')
    a = '123'
    b = '2345'
    yield (a, b)
    print('断开数据库连接')
class TestDemo:
    def test_a(self, contentDB):
        print('测试用例a')

    def test_b(self, contentDB):
        print('测试用例b')