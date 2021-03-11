import os
import unittest


suite = unittest.TestSuite()
# TestLoader用来加载测试用例的
# 我们可以根据模块加载，也可以根据测试类加载，自己定义规则，让他自动发现
loader = unittest.TestLoader()

start_dir = os.path.dirname(os.path.abspath(__file__))
# 自动发现测试用例的方法  从指定的start_dir（起始目录）递归查找所有子目录下的测试模块，并返回一个TestSuite对象。只有符合pattern模式匹配的测试文件才会被加载。模块名称必须有效才能被加载。
suite1 = loader.discover(start_dir)
# 运行，生成测试报告，我们先生成txt格式的，使用unittest自带的TextTestRunner生成测试报告（文本格式，不推荐使用）
with open('demo.txt', 'w', encoding='utf-8') as f:
    # 初始化runner  runner可以理解为运行器
    runner = unittest.TextTestRunner(f, verbosity=2)
    # run()方法是TextTestRunner主要的公共接口，需要一个TestSuite或者TestCase实例作为参数
    runner.run(suite1)

