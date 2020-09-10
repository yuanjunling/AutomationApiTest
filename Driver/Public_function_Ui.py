from selenium.webdriver.support.wait import WebDriverWait
def webdriverwait_xpath_click(driver,xpath):
    WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath(xpath)
    ).click()

def webdriverwait_xpath_send_keys(driver,xpath,parameter):
    WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath(xpath)
    ).send_keys(parameter)

def is_element_exist(driver,xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
        s = driver.execute_script("arguments[0].click();", element)
        if len(s) == 0:
            return False
        else:
            return True
    except Exception as e:
        e
