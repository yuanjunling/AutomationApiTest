# coding=utf-8
import json
import random
import unittest
import string

from Data.Body.body_data import *
from Driver.DoMysql import DoMysql
from Driver.base_request import request
from Driver.GenPass import GenPass
from Driver.handle_init import handle_ini
from Data.Headers.headers_data import *


class Sunscreen(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        rootpath = handle_ini.get_value('uat')
        self.SaveUrl = rootpath + "/mgmt/activity/save"
        self.publish = rootpath + "/mgmt/activity/publish/{}"
        self.applyurl = rootpath + "/activity/apply"
        self.agree = rootpath + "/activity/apply/agree"
        self.mysql = DoMysql("yjdf_mall_orders")

    def tearDown(self):
        print('测试结束')

    def test_01_Save(self):
        '''添加活动'''
        global activityName
        activityName = "jcx活动来一发{0}".format(random.randint(6, 999999))
        print("活动名称："+activityName)
        json_Save['activityName']=activityName
        res = request.run_main('post',url=self.SaveUrl,headers=headers_Sunscreen_web,json=json_Save)
        json_res = res
        try:
            self.assertEqual(json_res["success"], True)
            print(json.dumps(json_res, indent=2, ensure_ascii=False))
        except Exception as e:
            print(json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
    def test_02_publish(self):
        '''活动上架'''
        Activityname=activityName
        sql = "SELECT id FROM t_activity_info WHERE activity_name = '{}'".format(Activityname)
        global result
        result = self.mysql.fetchAll(sql)
        publish=self.publish.format(result[0]['id'])
        res = request.run_main('get', url=publish, headers=headers_Sunscreen_web)
        json_res=res
        try:
            self.assertEqual(json_res["success"], True)
            print(json.dumps(json_res, indent=2, ensure_ascii=False))
        except Exception as e:
            print(json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
    def test_03_apply(self):
        '''市级代理活动报名'''

        json_apply['receiverName'] =GenPass()
        json_apply['activityId']=result[0]['id']
        json_apply['receiverPhone']=random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        res = request.run_main('post', url=self.applyurl, headers=headers_Sunscreen_h5, json=json_apply)
        json_res = res
        try:
            self.assertEqual(json_res["success"], True)
            print(json.dumps(json_res, indent=2, ensure_ascii=False))
        except Exception as e:
            print(json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e

    def test_04_agree(self):
        '''省级审批通过'''
        sql = "SELECT id,user_id FROM t_activity_apply_info WHERE activity_id = '{}'".format(result[0]['id'])
        results = self.mysql.fetchAll(sql)
        json_agree['activityId']=result[0]['id']
        json_agree['applyId']=results[0]['id']
        json_agree['applyUserId'] =results[0]['user_id']
        res = request.run_main('post', url=self.agree, headers=headers_Sunscreen_h5_01, json=json_agree)
        json_res = res
        try:
            self.assertEqual(json_res["success"], True)
            print(json.dumps(json_res, indent=2, ensure_ascii=False))
        except Exception as e:
            print(json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
if __name__ == '__main__':
    unittest.main()