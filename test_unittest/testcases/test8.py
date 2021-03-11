import unittest
import ddt


# 装饰类，也就是继承自TestCase的类,可以理解为给这个类戴了个帽子
@ddt.ddt
class IntegerArithmeticTestCase(unittest.TestCase):
    # 装饰测试方法。参数是文件名。文件可以是json 或者 yaml类型。
    # 注意，如果文件以”.yml”或者”.yaml”结尾，ddt会作为yaml类型处理，其他所有文件都会作为json文件处理。
    # 如果文件中是列表，每个列表的值会作为测试用例参数，同时作为测试用例方法名后缀显示。
    # 如果文件中是字典，字典的key会作为测试用例方法的后缀显示，字典的值会作为测试用例参数
    @ddt.file_data('d1.json')
    @ddt.unpack
    # 每次运行都会从 data中取出一组数据，动态生成一个独立的测试用例方法
    def testAdd(self,first,second,values):
        self.assertEqual( (first+ second), values)


if __name__ == '__main__':
    unittest.main(verbosity=2)

