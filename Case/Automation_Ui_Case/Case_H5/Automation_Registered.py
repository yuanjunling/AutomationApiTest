# coding=utf-8
from selenium import webdriver
import unittest
from time import sleep
from Case.Automation_Ui_Case.Login import Login_H5
from Data.Body.Json_Ui_Data import account_Order
from Driver.Public_function_Ui import is_element_exist, webdriverwait_xpath_click, webdriverwait_xpath_send_keys, \
    is_element, Unblock
from Driver.Operationjson import OperationJson as openjson
opers = openjson()

class Automation_Registered_h5(unittest.TestCase):
    def setUp(self):
        mobileEmulation = {'deviceName': 'iPhone 6/7/8 Plus'}
        options = webdriver.ChromeOptions()
        # options.add_argument('headless') #静默执行
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(chrome_options=options)
        self.order_url = 'http://app-uat.yjdfmall.com/Wap/#/login'
        self.verificationErrors = []
        self.accept_next_alet = True

    @classmethod
    def setUpClass(cls):
        globals()["url"]=None
        globals()["username"]=None
        globals()["tops"]=None
        globals()["estate"]=None

    def tearDown(self):
        self.driver.quit()
    # @unittest.skip('暂时不执行')
    def test_01_Invite_agent_to_register(self):
        '''二级代理邀请代理'''
        driver = self.driver
        driver.get(self.order_url)
        Login_H5.lonin_h5(driver, account_Order['username'], account_Order['pwd'])  # 调用公共登录

        driver.find_element_by_xpath(opers.get_value('商铺中心')).click()

        if is_element_exist(driver, opers.get_value("公告")) == True:
            # 判断有无充值公告有就点击没有就下一步
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/div[3]/button').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/i').click()
            webdriverwait_xpath_click(driver, opers.get_value("邀请代理"))
        else:
            webdriverwait_xpath_click(driver, opers.get_value("邀请代理"))
        sleep(1)
        webdriverwait_xpath_click(driver,opers.get_value('estate')['市级'])
        globals()["estate"]=driver.find_element_by_xpath(opers.get_value('estate')['市级']).text
        # webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[2]/div/div[3]/div/i/div')
        sleep(1)
        webdriverwait_xpath_click(driver,opers.get_value('复制链接'))
        sleep(1)
        globals()["url"]=driver.find_element_by_class_name('van-grid-item').get_attribute('data-clipboard-text')
        print('省代邀请码: {}'.format(globals()["url"]))


    # @unittest.skip('暂时不执行')
    def test_02_Province(self):
        '''邀请省级代理'''
        driver=self.driver
        driver.get(globals()["url"])
        webdriverwait_xpath_send_keys(driver,opers.get_value('请输入手机号码'),account_Order['phone'])
        globals()["username"]=account_Order['phone']
        print('省级代理人账号：{}'.format(account_Order['phone']))
        f = open('/AutomationApiTest//Data//test','a')
        f.write('省级代理人账号：{}'.format(account_Order['phone']))
        f.write("\n")
        f.close()
        sleep(1)
        Unblock(driver,opers.get_value('获取验证码'))
        sleep(1)
        self.assertEqual(driver.find_element_by_xpath('/html/body/div[2]/div').text,'短信发送成功')
        sleep(1)
        webdriverwait_xpath_send_keys(driver,opers.get_value("请输入验证码"),account_Order['Verification_Code'])

        Unblock(driver,opers.get_value('下一步'))

        # self.assertEqual(driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]').text,'邀请人授权码：XX154422 邀请人：快乐的胖子')
        webdriverwait_xpath_send_keys(driver,opers.get_value('填写登录密码'),'a111111')

        webdriverwait_xpath_click(driver,opers.get_value('登录即同意'))

        Unblock(driver,'//*[@id="app"]/div/div[2]/div[3]/button/span')
        sleep(1)
        Unblock(driver,'//*[@id="app"]/div/div[4]/div[2]/button[2]/span')
        sleep(1)
        webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div/input',account_Order['name'])

        webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[2]/div[2]/div[3]/div[2]/div/input',account_Order['Number'])

        webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[2]/div[2]/div[5]/div[2]/div/input',account_Order['IdNumber'])

        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[2]/div[3]/div[1]/div[2]/div/input')
        sleep(1)
        #选择省市区
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[5]/div/ul[2]/li[3]')
        sleep(0.5)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[5]/div/ul[2]/li[3]')
        sleep(0.5)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[5]/div/ul[2]/li[3]')
        sleep(0.5)
        webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[2]/div[3]/div[2]/div[2]/div/textarea',account_Order['Address'])
        sleep(0.5)
        Unblock(driver,'//*[@id="app"]/div/div[3]/button[2]/span')
        sleep(0.5)
    # @unittest.skip('暂时不执行')
    def test_03_Superior_approval(self):
        '''上级升级审批'''
        driver = self.driver
        driver.get(self.order_url)
        Login_H5.lonin_h5(driver, account_Order['username'], account_Order['pwd'])

        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]').click()

        if is_element_exist(driver, '//*[@id="app"]/div/div[1]/div/div[4]/div[1]') == True:
            # 判断有无充值公告有就点击没有就下一步
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/div[3]/button').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/i').click()
            webdriverwait_xpath_click(driver, '//*[@id="app"]/div/div[1]/div/div[2]/div/div[6]/div/div')
        else:
            webdriverwait_xpath_click(driver, '//*[@id="app"]/div/div[1]/div/div[2]/div/div[6]/div/div')
        sleep(0.5)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/ul/li[1]/div[2]')
        sleep(0.5)
        # result=driver.find_elements_by_xpath('//button/span[text()="同意"]')
        for i in range(result:=len(driver.find_elements_by_xpath('//button/span[text()="同意"]'))):
           sleep(0.5)
           Unblock(driver,'//*[@id="app"]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/div/button[2]/span')
           sleep(0.5)

    # @unittest.skip('04暂时不执行')
    def test_04_Recharge(self):
        '''代理升级充值'''
        global tops
        driver = self.driver
        driver.get(self.order_url)
        Login_H5.lonin_h5(driver, globals()["username"], account_Order['pwd'])
        if is_element(driver,'//*[@id="app"]/div/div[2]/div/div[4]') == True:
            Unblock(driver,'//*[@id="app"]/div/div[2]/div/div[4]')
            print('代理{}升级成功'.format(globals()["estate"]))
        elif is_element(driver,'//*[@id="app"]/div/div[2]/div/div[3]')==True:
            Unblock(driver,'//*[@id="app"]/div/div[2]/div/div[3]')
        else:
            print('直接申请升级')
        sleep(1)
        if (exist:=is_element(driver,'//div/button/span[text()="升级中"]'))==True:
            sleep(1)
            Unblock(driver,'//div/button/span[text()="升级中"]')
            sleep(1)
            Unblock(driver,'//span[text()="去充值"]')
            global top_up
            top_up = driver.find_element_by_xpath('//span[text()="去充值"]').text
            sleep(1)
            driver.find_element_by_class_name('van-uploader__input').send_keys(account_Order['img'])
            sleep(1)
            tops = driver.find_element_by_xpath('//span[text()="确认充值"]').text
            webdriverwait_xpath_click(driver,'//span[text()="确认充值"]')

            sleep(1)
        elif (exist1:=is_element(driver,'//span[text()="去充值"]'))==True:
            sleep(1)
            Unblock(driver, '//span[text()="去充值"]')
            sleep(1)
            driver.find_element_by_class_name('van-uploader__input').send_keys(account_Order['img'])
            sleep(1)
            tops = driver.find_element_by_xpath('//span[text()="确认充值"]').text
            Unblock(driver, '//span[text()="确认充值"]')
            sleep(1)
        else:
            print('审核成功')
    # @unittest.skip("05暂时不执行")
    def test_05_Recharge_approved_by_superior(self):
        if tops == '确认充值':
            driver = self.driver
            driver.get(self.order_url)
            if account_Order['username']=='13555555555':
                Login_H5.lonin_h5(driver, account_Order['username'], account_Order['pwd'])  # 调用公共登录

                driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]').click()

                if is_element_exist(driver, '//*[@id="app"]/div/div[1]/div/div[4]/div[1]') == True:
                    # 判断有无充值公告有就点击没有就下一步
                    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/div[3]/button').click()
                    sleep(0.5)
                    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/i').click()
                    webdriverwait_xpath_click(driver, '//div/span[text()="我的审批"]')
                else:
                    webdriverwait_xpath_click(driver, '//div/span[text()="我的审批"]')
                sleep(0.5)
                webdriverwait_xpath_click(driver,'//span[text()="充值审批"]')
                sleep(0.5)
                for i in range(result:=len(driver.find_elements_by_xpath('//span[text()="加入平台充值"]'))):
                    if result == 0:
                        print('审批订单数{}'.format(result))
                    else:
                       sleep(0.5)
                       Unblock(driver,'//*[@id="app"]/div/div[3]/div/div[1]/div[1]/div[2]/button[2]/span')
                       sleep(0.5)
                       Unblock(driver,'//span[text()="确定加入"]')
                sleep(0.5)
                Unblock(driver,'//span[text()="发起平台充值"]')
                sleep(0.5)
                driver.find_element_by_class_name('van-uploader__input').send_keys(account_Order['img'])
                sleep(0.5)
                Unblock(driver,'//span[text()="提交"]')
                sleep(0.5)
            else:
                Login_H5.lonin_h5(driver, account_Order['username'], account_Order['pwd'])  # 调用公共登录

                driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]').click()
                sleep(0.5)
                if is_element_exist(driver, '//*[@id="app"]/div/div[1]/div/div[4]/div[1]') == True:
                    # 判断有无充值公告有就点击没有就下一步
                    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/div[3]/button').click()
                    sleep(0.5)
                    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/i').click()
                    webdriverwait_xpath_click(driver, '//div/span[text()="我的审批"]')
                else:
                    webdriverwait_xpath_click(driver, '//div/span[text()="我的审批"]')
                    sleep(0.5)
                    webdriverwait_xpath_click(driver, '//span[text()="充值审批"]')
                    sleep(0.5)
                    webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[3]/div/div[1]/div/div/div[2]/div[2]')
                    sleep(0.5)
                    driver.find_element_by_class_name('van-uploader__input').send_keys(account_Order['img'])
                    sleep(0.5)
                    Unblock(driver,'//*[@id="app"]/div/div[5]/div/button[2]/span')
                    sleep(0.5)
                    Unblock(driver,'//*[@id="app"]/div/div[1]/div/div[1]/i')
                    sleep(0.5)
                    Unblock(driver,'//*[@id="app"]/div/div/div/div[1]/i')
                    sleep(0.5)
                    Unblock(driver,'//*[@id="app"]/div/div[2]/div/div[4]')
                    sleep(0.5)
                    Unblock(driver,'//span[text()="个人中心"]')
                    sleep(0.5)
                    Unblock(driver,'//*[@id="app"]/div/div[2]/div[text()="退出登录"]')
                    sleep(0.5)
                    Login_H5.lonin_h5(driver, 13555555555, account_Order['pwd'])  # 调用公共登录

                    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]').click()

                    if is_element_exist(driver, '//*[@id="app"]/div/div[1]/div/div[4]/div[1]') == True:
                        # 判断有无充值公告有就点击没有就下一步
                        driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/div[3]/button').click()
                        sleep(0.5)
                        driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/i').click()
                        webdriverwait_xpath_click(driver, '//div/span[text()="我的审批"]')
                    else:
                        webdriverwait_xpath_click(driver, '//div/span[text()="我的审批"]')
                    sleep(0.5)
                    webdriverwait_xpath_click(driver, '//span[text()="充值审批"]')
                    sleep(0.5)
                    for i in range(result := len(driver.find_elements_by_xpath('//span[text()="加入平台充值"]'))):
                        if result == 0:
                            print('审批订单数{}'.format(result))
                        else:
                            sleep(0.5)
                            Unblock(driver, '//*[@id="app"]/div/div[3]/div/div[1]/div[1]/div[2]/button[2]/span')
                            sleep(0.5)
                            Unblock(driver, '//span[text()="确定加入"]')
                    sleep(0.5)
                    Unblock(driver, '//span[text()="发起平台充值"]')
                    sleep(0.5)
                    driver.find_element_by_class_name('van-uploader__input').send_keys(account_Order['img'])
                    sleep(0.5)
                    Unblock(driver, '//span[text()="提交"]')
                    sleep(0.5)
        else:
            print('已升级成功')


if __name__ == '__main__':
    unittest.main()