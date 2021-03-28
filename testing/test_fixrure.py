import pytest

@pytest.fixture()
def login():
    print('登录操作')
    yield
    print('登出操作')

def test_case1(connectDB):
    print('测试用例1')

def test_case2():
    print('测试用例2')

def test_case3(login):
    print('测试用例3')

@pytest.mark.usefixtures('login')
def test_case4():
    print('测试用例4')