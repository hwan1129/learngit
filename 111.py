from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import unittest
driver = webdriver.Chrome()


class Baidu_Test(unittest.TestCase):


    def test_login(self):

        driver.get("http://www.baidu.com/")
        #driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
        denlu = (By.XPATH, '//*[@id='u1']/a[7]')
        denlu.click()
        time.sleep(5)
        driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
        time.sleep(2)
        driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("hwan1129")
        time.sleep(2)
        driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("Hwan@1129")
        driver.find_element_by_name('memberPass').click()  # 去掉记住密码
        # 点击登录按钮
        time.sleep(2)
        driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
        time.sleep(2)

    def test_logout(self):

        uname = driver.find_element_by_id("s_username_top")
        ActionChains(driver).move_to_element(uname).perform()  # 移动鼠标到我的账号
        time.sleep(2)
        out=driver.find_element_by_class_name("quit")
        ActionChains(driver).move_to_element(out).perform()  # 移动鼠标到退出按钮
        time.sleep(2)
        out.click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[9]/div[2]/div[2]/div/div[3]/a[3]").click()


if __name__ == '__main__':
    unittest.main()


