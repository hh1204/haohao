import os
import unittest
# 1、首先导入HTMLTestRunner,注意：HTMLTestRunnerHh是我修改后的，其中Hh是为了区分一下，随便起的名字，哈哈
from HTMLTestRunnerHh import HTMLTestRunner

loader = unittest.TestLoader()
start_dir = os.path.dirname(os.path.abspath(__file__))
suite1 = loader.discover(start_dir)
with open('demo.html', 'wb') as f:
    # 2、我们把unittest里面的TextTestRunner替换成HTMLTestRunner
    # 3、HTMLTestRunner参数，我们看一下源码可知需要的参数 HTMLTestRunner(stream= verbosity=2,title=None,description=None,tester=None)
    # stream= : 输入流 verbosity=2: 不说了 前面写过，可以往前翻翻，title=None:默认None 就是测试报告的标题的名字，description=None:默认None，描述测试报告的，tester=None：测试人是谁
    runner = HTMLTestRunner(f, verbosity=2,title='浩浩的测试报告',description='浩浩是单身狗',tester='浩浩')
    # run()方法是TextTestRunner主要的公共接口，需要一个TestSuite或者TestCase实例作为参数
    runner.run(suite1)

