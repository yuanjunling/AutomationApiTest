# coding=utf-8

import unittest
import HTMLTestRunner_PY3
import time
import sys
sys.path.append('E:\AutomationApiTest')
# from Case.Test_Demo import ZNcase_01
from Driver.handle_init import handle_ini
# from Case.Jcx_Case.Sunscreen_Case import Sunscreen_Api
from Case.Automation_Ui_Case.Case_H5.Automation_Registered import Automation_Registered_h5 as h5
from Case.Automation_Ui_Case.Case_web.Test_Demo import Automation_Registered_web as web

suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(Sunscreen_Api.Sunscreen))
suite.addTest(unittest.makeSuite(h5))

now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
rootpath = handle_ini.get_value('rootpath')
file_path = rootpath + "/Report/"

wwwa = file_path + now + "report.html"
with open(wwwa, 'wb') as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(
        f, verbosity=2, title='注册/升级', description='执行人：袁军令')
    runner.run(suite)
    f.close()
