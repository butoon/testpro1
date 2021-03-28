import allure
import pytest
import yaml

from python_code.calc import Calculator

# @pytest.fixture(scope='class')
# def get_calc():
#     print('获取计算机实例')
#     calc = Calculator()
#     return calc


class TestCalc:
    # def setup_class(self):
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print('运算结束')

    # 加法
    @pytest.mark.add

    @allure.story('测试加法')
    def test_add(self, get_calc, get_add_datas):
        result = None
        try:
            with allure.step("计算两个数的相加和"):
                result = get_calc.add(get_add_datas[0], get_add_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_add_datas[2]

    #减法
    # @pytest.mark.parametrize(
    #     "a, b, expect",  get_datas()['sub']['datas'], ids=get_datas()['sub']['myid']
    # )
    def test_sub(self, get_calc, get_sub_datas):
        result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
        if  isinstance(result, float):
            result = round(result, 2)
        assert result == get_sub_datas[2]

    #乘法
    @allure.story('测试乘法')
    # @pytest.mark.parametrize(
    #     "a, b, expect", get_datas()['mul']['datas'], ids=get_datas()['mul']['myid']
    # )
    def test_mul(self, get_calc,get_mul_datas):
        result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_mul_datas[2]

    #除法
    # @pytest.mark.parametrize(
    #     "a, b, expect", get_datas()['div']['datas'], ids=get_datas()['div']['myid']
    # )
    def test_div(self, get_calc,get_div_datas):
        try:
            result = get_calc.div(get_div_datas[0], get_div_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception:
            print(' 除数不为00 ')
        finally:
            assert result == get_div_datas[2]

    @pytest.mark.sss
    def test_hh(self):
        print('这是一个测试的打印')