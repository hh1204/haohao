
from mock import Mock
import unittest


def add(a,b):
    """return a + b"""
    """没开发完的接口"""
    pass


test_data = {"a": 3, "b": 4, "expected": 7}


def demo(a,b):
    return a + b


class TestAdd(unittest.TestCase):
    def test_add(self):
        # mock对象赋值给add
        # add = Mock(return_value=test_data['expected'])
        """使用side_effect参数，值为一个函数，mock的这个函数就是用来代替add函数的
            也就是side_effect后面跟一个函数，动态返回值
        """
        add = Mock(side_effect=demo)
        actual = add(test_data["a"],test_data["b"])
        self.assertEqual(test_data["expected"],actual)