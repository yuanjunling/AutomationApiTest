# coding=utf-8
import json
import random
import unittest
import string
from Driver.base_request import request
from Driver.GenPass import GenPass
from Driver.handle_excle import handle
from Driver.handle_init import handle_ini
from Driver.hashlib_md5 import md5_hb

class JcxApi(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        rootpath = handle_ini.get_value('uat')
        self.url = rootpath+"/user/warrant"

    def tearDown(self):
        print('测试结束')

    def test_01_warrant(self):
        headers = {
            "Content-Type": "application/json",
            "token":"MTU5NTMxMDM0MTo0NTk3MTo0NTk3MTVmMTY4MTA1Y2ZlNGI=",
            "userId":"45971"
        }
        res = request.run_main('get',url=self.url,headers=headers)
        json_res = res
        print(json.dumps(json_res, indent=2, ensure_ascii=False))
if __name__ == '__main__':
    unittest.main()