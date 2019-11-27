from QiYeWeiXinAutoTest.common.Mylogger import logger
from QiYeWeiXinAutoTest.common.StartUp import startup
from QiYeWeiXinAutoTest.common.DoYml import readYml
from time import sleep
import unittest
import os


class AddClient(unittest.TestCase):

    # 通过手机号查找账户
    def searchPhoneNum(driver, phoneNum):
        try:
            logger.info("开始添加手机号：" + phoneNum)

            driver.find_element_by_id("com.tencent.wework:id/ep8").click()

            driver.find_element_by_android_uiautomator('new UiSelector().textContains("加微信")').click()

            driver.find_element_by_id("com.tencent.wework:id/dw4").click()

            driver.find_element_by_id("com.tencent.wework:id/dvn").send_keys(phoneNum)

            driver.find_element_by_android_uiautomator('new UiSelector().textContains("搜索")').click()
            sleep(1)
        except Exception as e:
            logger.exception(e)

    # 客户手机同时包含微信账号和企业微信账号时，选择微信账号进行添加
    def bothHaveWechatAndQW(driver, phoneNum):
        try:
            logger.info("同时使用企业微信和微信，选择微信账号")

            driver.find_element_by_id("com.tencent.wework:id/atl").click()

            # 如果已经添加过此微信用户
            if "发消息" in driver.page_source:
                AddClient.haveAdd(driver, phoneNum)

            else:
                driver.find_element_by_android_uiautomator('new UiSelector().textContains("添加为联系人")').click()

                driver.find_element_by_android_uiautomator('new UiSelector().textContains("发送添加邀请")').click()

                logger.info("添加手机号成功：" + phoneNum)

                driver.keyevent(4)
                sleep(1)
                driver.keyevent(4)
                sleep(1)
                driver.keyevent(4)
                sleep(1)
                driver.keyevent(4)
                sleep(1)
                driver.keyevent(4)
        except Exception as e:
            logger.exception(e)

    # 客户只有企业微信账号时，不予添加，直接退出
    def OnlyQw(driver, phoneNum):
        try:
            logger.info("通过手机号{}只能查询到企业微信账号，查询不到微信账号，不予添加！".format(phoneNum))
            driver.keyevent(4)
            sleep(1)
            driver.keyevent(4)
            sleep(1)
            driver.keyevent(4)
        except Exception as e :
            logger.exception(e)

    # 客户只有微信账号时，直接添加
    def OnlyWechat(driver, phoneNum):
        try:
            if "发消息" in driver.page_source:
                AddClient.haveAdd(driver,phoneNum)

            else:
                logger.info("此人没有同时使用企业微信和微信，可以直接添加手机号")
                driver.find_element_by_android_uiautomator('new UiSelector().textContains("添加为联系人")').click()

                driver.find_element_by_android_uiautomator('new UiSelector().textContains("发送添加邀请")').click()

                driver.keyevent(4)
                sleep(1)
                driver.keyevent(4)
                sleep(1)
                driver.keyevent(4)
                sleep(1)
                driver.keyevent(4)

        except Exception as e:
            logger.exception(e)

    def haveAdd(driver, phoneNum):
        try:
            logger.info("手机号{}之前已经添加过，不予添加！".format(phoneNum))
            driver.keyevent(4)
            sleep(1)
            driver.keyevent(4)
            sleep(1)
            driver.keyevent(4)
            sleep(1)
            driver.keyevent(4)

        except Exception as e:
            logger.exception(e)

    def test_addclient(self):
        try:
            # 读取文件中的手机号
            fpath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), './TestYaml/AddClient.yml')
            fopen = readYml(fpath)
            phones = fopen
            driver = startup()

            if phones:
                for phoneNum in phones:
                    # 通过手机查客户
                    AddClient.searchPhoneNum(driver, phoneNum)

                    # 如果客户既有微信又有企业微信
                    if "对方同时使用微信和企业微信" in driver.page_source :

                        AddClient.bothHaveWechatAndQW(driver, phoneNum)

                    # 如果客户只有企业微信
                    elif "企业信息暂时不可见" in driver.page_source :
                        AddClient.OnlyQw(driver, phoneNum)

                    # 如果客户只有微信
                    else:
                        logger.info("以前没有添加过此手机号，开始添加")
                        AddClient.OnlyWechat(driver, phoneNum)

                    logger.info("结束添加客户："+ phoneNum)

                logger.info("所有手机号添加完成！")

            else:
                logger.info("手机号列表中为空，请输入要添加的手机号")

        except Exception as e:
            logger.exception(e)
