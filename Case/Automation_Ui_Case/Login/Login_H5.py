# coding=utf-8
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from Driver.Public_function_Ui import Unblock, is_element


def lonin_h5(driver,name,pwd):
    if is_element(driver,'//*[@id="app"]/div/div[2]/button[1]/span') == True:
        sleep(1)
        print(1111)
        Unblock(driver,'//*[@id="app"]/div/div[2]/button[2]/span')
        sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div[1]/div/div/input").send_keys(name)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div/div/input').send_keys(pwd)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/button').click()
        sleep(2)
        Action = ActionChains(driver)
        Action.move_by_offset(200, 100).click().perform()
    else:
        print(22222)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div[1]/div/div/input").send_keys(name)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div/div/input').send_keys(pwd)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/button').click()
        sleep(2)
        Action = ActionChains(driver)
        Action.move_by_offset(200, 100).click().perform()
