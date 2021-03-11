import unittest
# 导入t1模块的类
from test_unittest.testcases.test1 import IntegerArithmeticTestCase

# IntegerArithmeticTestCase下的测试用例
cases= [IntegerArithmeticTestCase('testAdd'),
        IntegerArithmeticTestCase('testMultiply')]

#  创建测试套件的同时，直接往测试套件里面添加测试用例，省去suite.addTests(cases)
#  如果写上tests参数，那么它必须是一个可迭代对象，用来创建套件的
suite = unittest.TestSuite(tests=cases)

# 运行，生成测试报告，我们先生成txt格式的，使用unittest自带的TextTestRunner生成测试报告（文本格式，不推荐使用）
with open('demo.txt', 'w', encoding='utf-8') as f:
    # 初始化runner  runner可以理解为运行器
    runner = unittest.TextTestRunner(f)
    # run()方法是TextTestRunner主要的公共接口，需要一个TestSuite或者TestCase实例作为参数
    runner.run(suite)