#!/usr/bin/env
# coding = utf-8
import requests
import unittest
from tcs.conf import *

class SelectXmind(unittest.TestCase):
    def setUp(self):
        self.url = host + ':8001'

    def tearDown(self):
        pass

    def test_select(self):
        open('d:/aaa.txt', mode='w', encoding='utf8')
        res = requests.get(self.url)
        statusCode = res.status_code
        self.assertEqual(200, statusCode)
