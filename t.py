#!/usr/bin/env
# coding:utf-8
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        print('开始')

    def tearDown(self):
        print('结束')

    def test_add(self):
        print('test add')
        self.assertEqual(3, 1 + 1)

if __name__ == '__main__':
    unittest.main()