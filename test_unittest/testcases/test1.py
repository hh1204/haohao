import unittest


# 我们先打印一下unittest的源码
#print(help(unittest))

# 粘贴出源码里面提供的例子，然后我们总结一下每行代码的意思

# Simple
# usage:
# import unittest  1、使用unittest前，需导入unittest框架

# 2、IntegerArithmeticTestCase这个类必须继承unittest.TestCase，TestCase类，所有测试用例类继承的基类
class IntegerArithmeticTestCase(unittest.TestCase):
    # @classmethod 装饰器，根据名字就知道是类方法，在类运行之前运行，先知道这种用法就行，后面会单独讲一下装饰器的用法
    @classmethod
    # 当类中的测试方法被执行前会被调用的一个类方法。该方法只会在类方法前调用，也就是带有calssmethod装饰器并且没有其他参数的方法。
    def setUpClass(cls):
        print("测试类之前运行")
    @classmethod
    # 当类测试方法被执行完后会被调用的一个类方法。该方法只会在一个类的所有方法执行完成后调用，该方法被调用时，必须有calssmethod装饰器并且除了类以外没有其他参数的方法
    def tearDownClass(cls):
        print("测试类之后运行")
    # setUp函数：初始化环境（执行每条用例之前，都要执行setUp函数下面的代码，每次都要执行）
    # 前置条件。测试方法之前自动运行setup里面的代码，比如在接口自动化中需要先登录的接口就需要频繁获取cookie，这样很不方便，所以就可以把获取cookie的方法写在setup里面
    def setUp(self):
        print("用例执行前置条件")
    # tearDown函数：清洗环境（执行每条用例之后，都要执行tearDown函数下面的代码，每次都要执行)
    # 后置条件。测试方法之后自动运行teardown里面的代码，比如在接口自动化中清理跑完一条case在数据库里产生的垃圾数据就可以写在teardown里面
    def tearDown(self):
        print("用例执行后置条件")
    # 3、类内的方法必须以test开头，比如testAdd或者test_Add
    def testAdd(self):  # test method names begin with 'test'
        # 4、断言：assertEqual用来断言预期结果和实际结果是否一致。当然unittest还包含很多其他断言方法，后面统一介绍
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)
        print("我是第一个方法")
    # 测试用例
    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 4)
        print("我是第二个方法")
# 5、用例执行顺序。在代码中不是写在前面的方法就先执行，如果把testMultiply放在testAdd方法之前，也是先执行testAdd方法，这是因为unittest执行测试用例，默认是根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z，a-z。


if __name__ == '__main__':
    # unittest.main()是运行主函数
    unittest.main(verbosity=2)

# verbosity是一个选项,表示测试结果的信息复杂度，有0、1、2 三个值。verbosity=0 : 你只能获得测试用例数总的结果；verbosity=1 (默认模式): 在每个成功的用例前面有个“.”，表示通过， 每个失败的用例前面有个 “F”，faild表示失败；verbosity=2 (详细模式):测试结果会显示每个测试用例的所有相关的信息。