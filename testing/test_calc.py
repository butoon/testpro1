import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)['add']
    print(datas)
    add_datas = datas['datas']
    myid = datas['myid']
    print(datas)


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    def teardown_class(self):
        print('运算结束')

    @pytest.mark.parametrize(
        "a, b, expect", add_datas, ids=myid
    )
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect
