from dema.teacher import LoginTest
import unittest
import os
from HTMLTestRunner import HTMLTestRunner


suite = unittest.TestSuite()
'''suite.addTest(LoginTest("testlogin"))
suite.addTest(LoginTest("testfindAllTeacher"))
suite.addTest(LoginTest("testfindAllMenu"))
suite.addTest(LoginTest("testfindAllStudent"))'''

test = unittest.defaultTestLoader.discover(os.getcwd(),"test*.py")
suite.addTest(test)

f = open("讲师搜索系统测试.html","w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    verbosity=1,
    title = "讲师搜索系统测试"
)
runner.run(suite)