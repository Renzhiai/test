# coding:utf-8
import unittest
import HTMLTestRunner

if __name__ == '__main__':
    path = './'
    file_path = 'd:/test.html'
    # 不支持数字开头
    ts = unittest.defaultTestLoader.discover(path, pattern='TC*.py')
    # ts = unittest.defaultTestLoader.discover(path, pattern='select*.py')
    f = open(file_path, mode='wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='用例执行情况')
    runner.run(ts)
    f.close()