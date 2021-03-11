
import os
import unittest
from HTMLTestRunnerHh import HTMLTestRunner
from datetime import datetime
from test_unittest.untils.d5 import logger

# 这块先空着  后面我们有大用处
@classmethod
def setUpClass(cls):
    pass


# 这块先空着  后面我们有大用处
@classmethod
def tearDownClass(cls):
    pass


# 这块先空着  后面我们有大用处
def setup():
    pass


# 这块先空着  后面我们有大用处
def teardown():
    pass


# 获取测试用例
def getTestCases():
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(os.path.abspath(__file__))
    print(start_dir)
    suite = loader.discover(start_dir)
    return suite


# 时间戳，获取当前时间，主要是用来给自动生成的测试报告命名的
def getNowTime():
    # 注意导入的包是datetime.datetime(date)
    return datetime.now().strftime('%Y%m%d%H%M%S')


# 获取测试报告
def getReport():
    start_dir = os.path.dirname(os.path.abspath(__file__))
    # 获取报告目录
    report_dir = os.path.join(start_dir, '../report')
    logger.info(report_dir)
    # 首先判断一下报告目录是否存在，存在就直接获取，不存在就先创建
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)
    # 拼接一个完整的测试报告名字  报告目录，时间戳+.html后缀
    return os.path.join(report_dir, getNowTime() + '.html')


# 运行方法
def run():
    with open(getReport(),'wb') as f:
        runner = HTMLTestRunner(f,
                                verbosity=2,
                                title='浩浩的测试报告',
                                description='浩浩是单身狗',
                                tester='浩浩')
        runner.run(getTestCases())


if __name__ == '__main__':
    run()