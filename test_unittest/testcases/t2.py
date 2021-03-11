import unittest
# 导入t1模块的类
from test_unittest.testcases.test1 import IntegerArithmeticTestCase

# TestSuite这个类代表一个测试用例或测试套件的集合，该类描述了一个可以被test runner执行的接口，通过它可以执行任何测试，运行一个TestSuite就相当于将测试套件迭代，然后执行每一个测试
suite = unittest.TestSuite()
# IntegerArithmeticTestCase下的测试用例
cases= [IntegerArithmeticTestCase('testAdd'),
        IntegerArithmeticTestCase('testMultiply')]

# suite = unittest.TestSuite(tests=cases)
# 往套件里添加测试用例   注意：是addTests，不是addTest，addTest是添加一条测试用例
suite.addTests(cases)
# 运行，生成测试报告，我们先生成txt格式的，使用unittest自带的TextTestRunner生成测试报告（文本格式，不推荐使用）
with open('demo.txt', 'w', encoding='utf-8') as f:
    # 初始化runner  runner可以理解为运行器
    runner = unittest.TextTestRunner(f)
    # run()方法是TextTestRunner主要的公共接口，需要一个TestSuite或者TestCase实例作为参数
    runner.run(suite)