# coding=utf-8
import json
import random
import unittest
import string

from Data.Body.body_data import *
from Driver.DoMysql import DoMysql
from Driver.base_request import request
from Driver.GenPass import GenPass
from Driver.handle_excle import handle
from Driver.handle_init import handle_ini
from Driver.hashlib_md5 import md5_hb
from Data.Headers.headers_data import *

class Sunscreen(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        rootpath = handle_ini.get_value('uat')
        self.SaveUrl = rootpath + "/mgmt/activity/save"
        self.publish = rootpath + "/mgmt/activity/publish/{}"

    def tearDown(self):
        print('测试结束')

    def test_01_Save(self):
        '''
        添加活动
        '''
        res = request.run_main('post',url=self.SaveUrl,headers=headers_Sunscreen,json=json_Save)
        json_res = res
        try:
            self.assertEqual(json_res["success"], True)
            print(json.dumps(json_res, indent=2, ensure_ascii=False))
        except Exception as e:
            print(json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
    def test_02_publish(self):
        '''活动上架'''
        mysql = DoMysql("yjdf_mall_orders")
        Activityname=activityName
        sql = "SELECT id FROM t_activity_info WHERE activity_name = '{}'".format(Activityname)
        result = mysql.fetchAll(sql)
        print(result[0]['id'])
        publish=self.publish.format(result[0]['id'])
        res = request.run_main('get', url=publish, headers=headers_Sunscreen)
        json_res=res
        try:
            self.assertEqual(json_res["success"], True)
            print(json.dumps(json_res, indent=2, ensure_ascii=False))
        except Exception as e:
            print(json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e

if __name__ == '__main__':
    unittest.main()