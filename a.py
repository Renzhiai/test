# coding:utf-8
import unittest
import HTMLTestRunner

class Test(unittest.TestCase):
    def setUp(self):
        print('开始')

    def tearDown(self):
        print('结束')

    def test_add(self):
        print('test add')
        self.assertEqual(3, 1 + 2)

if __name__ == '__main__':
    # 定义一个测试容器
    test = unittest.TestSuite()
    # 将测试用例，加入到测试容器中
    test.addTest(Test('test_add'))
    # 定义报告存放的路径，支持相对路径
    file_path = "/root/result.html"
    file_result = open(file_path, mode='wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title='测试报告', description='用例执行情况')
    # 运行测试用例
    runner.run(test)
    file_result.close()