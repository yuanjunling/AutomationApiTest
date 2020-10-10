# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://app-uat.yjdfmall.com/Web/#/memberManage/exitAgent')
driver.execute_script('sessionStorage.setItem("token","4raqbhralk9tke3vvtktbff6d2")')
driver.refresh()#刷新

