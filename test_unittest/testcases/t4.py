import unittest
# 导入t1模块的类
from test_unittest.testcases import test1

# IntegerArithmeticTestCase下的测试用例
# cases= [IntegerArithmeticTestCase('testAdd'),
#        IntegerArithmeticTestCase('testMultiply')]

# TestLoader用来加载测试用例的
# 我们可以根据模块加载，也可以根据测试类加载，自己定义规则，让他自动发现
loader = unittest.TestLoader()
# 根据测试类去加载测试用例
# cases1 = loader.loadTestsFromTestCase(IntegerArithmeticTestCase)

# 根据模块去加载测试用例
cases2 = loader.loadTestsFromModule(test1)

suite = unittest.TestSuite()
# suite.addTests(cases1)
suite.addTests(cases2)

# 运行，生成测试报告，我们先生成txt格式的，使用unittest自带的TextTestRunner生成测试报告（文本格式，不推荐使用）
with open('demo.txt', 'w', encoding='utf-8') as f:
    # 初始化runner  runner可以理解为运行器
    runner = unittest.TextTestRunner(f)
    # run()方法是TextTestRunner主要的公共接口，需要一个TestSuite或者TestCase实例作为参数
    runner.run(suite)