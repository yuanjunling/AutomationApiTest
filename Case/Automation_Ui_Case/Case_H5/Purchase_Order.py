# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import choice
import unittest,random,hashlib
from selenium.webdriver.support.wait import WebDriverWait
from Case.Automation_Ui_Case.Login import Login_H5
from time import sleep
from Driver.Public_function_Ui import is_element_exist, webdriverwait_xpath_click,webdriverwait_xpath_send_keys


class Purchase_order(unittest.TestCase):
    def setUp(self):
        mobileEmulation = {'deviceName': 'iPhone 6/7/8 Plus'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(chrome_options=options)
        self.order_url='http://app-uat.yjdfmall.com/Wap/#/login'
        self.verificationErrors=[]
        self.accept_next_alet=True
    def test_01_order(self):
        '''采购订单'''
        driver=self.driver
        driver.get(self.order_url)
        Login_H5.lonin_h5(driver,13577777777,'a111111')#调用公共登录
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]').click()
        sleep(2)
        if  is_element_exist(driver,'//*[@id="app"]/div/div[1]/div/div[4]/div[1]')==True:
            #判断有无充值公告有就点击没有就下一步
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/div[3]/button').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/i').click()
            webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[2]/div/div')
        else:
            webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[2]/div/div')
        #搜索
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[1]/div/div[3]/div/i')
        webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[1]/div/div[2]/form/div/div/div/div[2]/div/input','姬存希官方正品水光清透隔离防晒乳隔离紫外线面部身体小晶钻新品')
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[1]/div/div[3]/span')

        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[2]/div/div[2]/button')

        webdriverwait_xpath_click(driver, '//*[@id="app"]/div/div[1]/div/div[1]/i')
        sleep(1)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[4]/button')#普通进货单
        sleep(1)
        element = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/button')
        driver.execute_script("arguments[0].click();", element)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[4]/button')
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[4]/div[2]/div[2]/div[3]/button')
        sleep(1)
        for i in range(6):
            webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[4]/div[3]/div[2]/div[2]/div[2]/ul/li[1]')
        sleep(2)
        #截取当前窗口，并指定截图图片的保存位置
        now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time())) #生成时间
        file_path = 'E://AutomationApiTest//Report//Img//'
        wwwa=file_path+now+'selenium_img.png'
        driver.get_screenshot_as_file(wwwa)
        sleep(5)
        driver.quit()
        if __name__ == '__main__':
            unittest.main()





