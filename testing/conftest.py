import os
from typing import List

import pytest
import yaml

from python_code.calc import Calculator


@pytest.fixture(scope='session')
def connectDB():
    print('连接数据库操作')
    yield
    print('断开数据库连接')

@pytest.fixture(scope='class')
def get_calc():
    print('获取计算机实例')
    calc = Calculator()
    return calc


with open('../datas/calc.yaml') as f:
    datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_myid = datas['add']['myid']
    sub_datas = datas['sub']['datas']
    sub_myid = datas['sub']['myid']
    mul_datas = datas['mul']['datas']
    mul_myid = datas['mul']['myid']
    div_datas = datas['div']['datas']
    div_myid = datas['div']['myid']

@pytest.fixture(params=add_datas, ids=add_myid)
def get_add_datas(request):
    print('开始计算加法')
    data = request.param
    print(f'request.param 里面的测试数据是： {data}')
    yield data
    print('计算结束')

@pytest.fixture(params=sub_datas, ids=sub_myid)
def get_sub_datas(request):
    print('开始计算减法')
    data = request.param
    print(f'request.param 里面的测试数据是： {data}')
    yield data
    print('计算结束')

@pytest.fixture(params=mul_datas, ids=mul_myid)
def get_mul_datas(request):
    print('开始计算乘法')
    data = request.param
    print(f'request.param 里面的测试数据是： {data}')
    yield data
    print('计算结束')

@pytest.fixture(params=div_datas, ids=div_myid)
def get_div_datas(request):
    print('开始计算除法')
    data = request.param
    print(f'request.param 里面的测试数据是： {data}')
    yield data
    print('计算结束')

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param pytest.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
    #实现用例反转执行
    #items.reverse()

    # 修改测试用例参数编码格式
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')