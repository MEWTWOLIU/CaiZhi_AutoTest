# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from QiYeWeiXinAutoTest.common.Mylogger import logger
from QiYeWeiXinAutoTest.common import swipe
from QiYeWeiXinAutoTest.common.StartUpSingle import startup
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from assertpy import assert_that
from time import sleep



def OpenApp():
    try:
        logger.info("===========================启动小程序=========================")
        xPKeyValue = {
            '新翰财智': '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[14]/android.widget.TextView'

        }

        driver = startup()
        driver.find_element_by_android_uiautomator('text("工作台")').click()
        sleep(1)
        swipe.swipeUp(driver,1000)

        # 因为有重复的元素，采用获取多个结果然后存入数组，取第1个
        driver.find_elements_by_android_uiautomator('new UiSelector().textContains("新翰财智")')[0].click()

        driver.implicitly_wait(10)
        # 通过检验title来检验是否进入小程序首页
        locator = (By.ID, 'com.tencent.wework:id/ck')
        element = ec.presence_of_element_located(locator)
        result = WebDriverWait(driver,5).until(element)
        logger.info(result)
        assert_that(result).is_true()
        logger.info('成功打开财智小程序')
        logger.info("---------开始案例执行---------")
        return driver

    except Exception as e :
        logger.info('财智小程序打开失败')
        logger.error(e)
        return None



