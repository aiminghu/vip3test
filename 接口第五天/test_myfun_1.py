#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/10 0010 上午 11:47 
# @Author : aiminhu
# @File : test_myfun.py 
# @Software: PyCharm
import unittest
from  接口第五天.myfun import *

'''
坑1：集成unittest.TestCase类时，光标最好放到main函数执行
'''
class TestMyFun(unittest.TestCase):
    # TestCase基类方法，所有case执行之前自动执行
    @classmethod
    def setUpClass(cls):
        print("~~这里是所有测试用例前的准备工作")

    # TestCase基类方法，所有case执行之后自动执行
    @classmethod
    def tearDownClass(cls):
        print("~~这里是所有测试用例后的清理工作")

    #Testcase基类方法，每次执行case前自动执行
    def setUp(self):
        print("***这里是一个测试用例前的准备工作***")


    #Testcase基类方法，每次执行case后自动执行
    def tearDown(self):
        print("***这里是一个测试用例后的清理工作***")

    def test_add(self):
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(3,add(2,2)) #测试业务方法add
        print('this is add')

    def test_minus(self):
        self.assertEqual(1,minus(3,2)) #测试业务方法minus
        print('this is minus')

    def test_multi(self):
        self.assertEqual(6,multi(2,3)) #测试业务方法multi
        print('this is multi')

    def test_divide(self):
        self.assertEqual(2,divide(6,3)) #测试业务方法divide
        print('this is divide')


if __name__ == '__main__':
    pass
    # unittest.main(verbosity=2)
    # suit = unittest.TestSuite()
    # suit.addTest(TestMyFun('test_add'))
    # suit.addTest(TestMyFun("test_divide"))
    # runner = unittest.TextTestRunner() #实例化TextTestRunner类
    # runner.run(suit)  #调用