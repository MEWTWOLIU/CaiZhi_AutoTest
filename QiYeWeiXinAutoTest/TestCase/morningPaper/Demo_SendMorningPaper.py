# -*- coding:utf-8 -*-
from QiYeWeiXinAutoTest.common.OpenCaiZhiApplet import OpenApp
from time import sleep
from assertpy import assert_that
from QiYeWeiXinAutoTest.common.DoAppium import StartAppium, StopAppium
from QiYeWeiXinAutoTest.common.Mylogger import logger
from QiYeWeiXinAutoTest.common.findElement import findElement

import unittest

class SendMorningPaper(unittest.TestCase):

    def test_SendMorningPaper():
        try:
            xpth = {
                'sendBtn1': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View[22]',
                'sendBtn2': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView[3]',
                'sendBtn3': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View[24]/android.view.View[4]/android.view.View'
            }

            driver = findElement(OpenApp())
            # driver = OpenApp()
            # 还需要调整这个地方的androidtext的识别
            driver.findElement("android_text", "营销").click()

            logger.info("<--------分享早报案例开始-------->")
            sleep(1)
            # driver.find_element_by_android_uiautomator('new UiSelector().textContains("每日早报")').click()
            driver.find_element_by_android_uiautomator('new UiSelector().textContains("午间趣谈")').click()
            sleep(1)
            driver.find_element_by_xpath(xpth['sendBtn1']).click()
            sleep(1)
            driver.find_element_by_android_uiautomator('new UiSelector().textContains("发给客户")').click()
            sleep(1)
            driver.find_element_by_android_uiautomator('new UiSelector().textContains("创建新聊天")').click()
            sleep(1)
            driver.find_element_by_android_uiautomator('new UiSelector().textContains("Mr.JOKER")').click()
            sleep(1)
            driver.find_element_by_android_uiautomator('new UiSelector().textContains("确定")').click()
            sleep(1)

            driver.find_element_by_xpath(xpth['sendBtn2']).click()
            driver.implicitly_wait(3)
            # 发送早报后返回早报页面，识别“今日综述”
            result = driver.find_element_by_android_uiautomator('new UiSelector().textContains("今日综述")').id

            assert_that(result).is_true()
            logger.info("分享早报成功")
            logger.info("<--------分享早报案例结束-------->")

            driver.find_element_by_css_selector()
            driver.find_element_by_ios_uiautomation()
            driver.find_element_by_ios_uiautomation()


        except Exception as e:

            logger.error("分享早报失败")
            logger.exception(e)
            assert_that().is_true()

    def setUpClass(self):

        # 启动appium
        StartAppium(4723)
        print("11111111111111111111")

    def setUp(self):

        print("第一个案例执行开始")
        print("22222222222222222222")

    def tearDown(self):

        print("案例执行结束")
        print("3333333333333333333")

    def tearDownClass(self):

        # 关闭appium
        StopAppium(4723)
        print("44444444444444444444")
