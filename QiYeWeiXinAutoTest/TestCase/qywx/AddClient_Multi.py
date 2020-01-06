from QiYeWeiXinAutoTest.common.Mylogger import logger
from QiYeWeiXinAutoTest.common.StartUpMulti import startup
from QiYeWeiXinAutoTest.common.DoExcel import readExcel
from time import sleep
from QiYeWeiXinAutoTest.common.swipe import getScreenSize
import unittest
import time
import os


class AddClient(unittest.TestCase):

    # 通过手机号查找账户
    def searchPhoneNum(driver, ptelephone):
        try:
            logger.info("开始添加手机号：" + ptelephone)
            sleep(1)
            driver.find_element_by_id("com.tencent.wework:id/ep8").click()

            driver.find_element_by_android_uiautomator('new UiSelector().textContains("加微信")').click()

            driver.find_element_by_id("com.tencent.wework:id/dw4").click()

            driver.find_element_by_id("com.tencent.wework:id/dvn").send_keys(ptelephone)

            driver.find_element_by_android_uiautomator('new UiSelector().textContains("搜索")').click()
            sleep(0.5)
        except Exception as e:
            logger.exception(e)
            os._exit(0)

    # 客户手机同时包含微信账号和企业微信账号时，选择微信账号进行添加
    def bothHaveWechatAndQW(driver, ptelephone):
        try:
            logger.info("同时使用企业微信和微信，选择微信账号")

            driver.find_element_by_id("com.tencent.wework:id/atl").click()
            sleep(0.5)
            # 如果已经添加过此微信用户
            if "发消息" in driver.page_source:
                AddClient.BothhaveAdd(driver, ptelephone)

            else:
                driver.find_element_by_android_uiautomator('new UiSelector().textContains("添加为联系人")').click()

                AddClient.addmessage(driver)

                driver.find_element_by_android_uiautomator('new UiSelector().textContains("发送添加邀请")').click()

                logger.info("添加手机号成功：" + ptelephone)
                sleep(0.5)
                driver.keyevent(4)
                sleep(0.5)
                driver.keyevent(4)
                sleep(0.5)
                driver.keyevent(4)
                sleep(0.5)
                driver.keyevent(4)

                driver.keyevent(4)

        except Exception as e:
            logger.exception(e)
            os._exit(0)

    # 客户只有企业微信账号时，不予添加，直接退出
    def OnlyQw(driver, ptelephone):
        try:
            logger.info("通过手机号{}只能查询到企业微信账号，查询不到微信账号，不予添加！".format(ptelephone))
            driver.keyevent(4)
            sleep(0.5)
            driver.keyevent(4)
            sleep(0.5)
            driver.keyevent(4)
        except Exception as e :
            logger.exception(e)
            os._exit(0)

    # 客户只有微信账号时，直接添加
    def OnlyWechat(driver, ptelephone):
        try:
            if "发消息" in driver.page_source:
                AddClient.haveAdd(driver,ptelephone)

            else:
                logger.info("此人没有同时使用企业微信和微信，可以直接添加手机号")
                driver.find_element_by_android_uiautomator('new UiSelector().textContains("添加为联系人")').click()

                AddClient.addmessage(driver)

                driver.find_element_by_android_uiautomator('new UiSelector().textContains("发送添加邀请")').click()
                sleep(0.5)
                driver.keyevent(4)
                sleep(0.5)
                driver.keyevent(4)
                sleep(0.5)
                driver.keyevent(4)

                driver.keyevent(4)   # 12/16 added by liuyang

        except Exception as e:
            logger.exception(e)
            os._exit(0)

    # 只含有微信账户，且已经添加过这个客户
    def haveAdd(driver, ptelephone):
        try:
            logger.info("手机号{}之前已经添加过，不予添加！".format(ptelephone))
            sleep(0.5)
            driver.keyevent(4)
            sleep(0.5)
            driver.keyevent(4)
            sleep(0.5)
            driver.keyevent(4)


        except Exception as e:
            logger.exception(e)
            os._exit(0)

    # 同时有微信和企业微信账号，而且之前已经添加过此客户
    def BothhaveAdd(driver, ptelephone):
        try:
            logger.info("手机号{}之前已经添加过，不予添加！".format(ptelephone))
            sleep(0.5)
            driver.keyevent(4)
            sleep(0.5)
            driver.keyevent(4)
            sleep(0.5)
            driver.keyevent(4)
            sleep(0.5)
            driver.keyevent(4)


        except Exception as e:
            logger.exception(e)
            os._exit(0)

    # 通过手机号都搜不到微信。。。
    def noWeChat(driver, ptelephone):
        try:
            logger.info("搜索不到手机号{}对应的微信号，无法添加".format(ptelephone))
            driver.find_element_by_id("com.tencent.wework:id/ang").click()
            driver.keyevent(4)
            sleep(0.5)
            driver.keyevent(4)
        except Exception as e:
            logger.exception(e)
            os._exit(0)

    def addmessage(driver):
        try:
            msg = u"添加我的企业微信可以领10块钱现金红包偶~"
            driver.find_element_by_id("com.tencent.wework:id/ze").click()

            driver.find_element_by_id("com.tencent.wework:id/ze").click()

            driver.find_element_by_id("com.tencent.wework:id/zc").send_keys(msg)

            # 点击屏幕中间偏上位置来隐藏输入键盘
            ScreenSize = getScreenSize(driver)
            x = ScreenSize[0]*0.5
            y = ScreenSize[1]*0.1
            driver.tap([(x, y)], 500)



        except Exception as e:
            logger.exception(e)
            os._exit(0)


    def test_addclient(desiredOfPhone, unid, port):
        try:
            # 获取时间
            startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            # 读取excel文件
            f = readExcel('userinfo.xlsx')
            # 启动企业微信
            logger.info("取driver")
            driver = startup(desiredOfPhone, unid, port)
            # 发送总人数计数器
            sendNum = 0

            # 逐行取值
            for name in f['姓名'].values:

                sendNum += 1
                logger.info(str(port) + ":当前添加第" + str(sendNum) + "个客户")
                pname = name
                # 取某行的值，用f[f['列名']=='具体列里面的某个值']，但是返回的是个pandas对象，需要.values取到值，发现竟然是一个
                # numpy.ndarray的数组类型，因此还要转成list类型，再取第一个元素就拿到列的值了，说实话，好麻烦。。。
                ptelephone = str(f[f['姓名'] == name]['手机号'].values.tolist()[0])
                logger.info("姓名为：" + pname)
                logger.info("手机号为：" + ptelephone)

                # 通过手机查客户
                sleep(0.5)
                AddClient.searchPhoneNum(driver, ptelephone)
                sleep(0.5)
                # 如果添加手机号连微信都没有......
                if "该用户不存在" in driver.page_source:
                    AddClient.noWeChat(driver,ptelephone)

                # 如果客户既有微信又有企业微信
                elif "对方同时使用微信和企业微信" in driver.page_source :
                    AddClient.bothHaveWechatAndQW(driver, ptelephone)

                # 如果客户只有企业微信
                elif "企业信息暂时不可见" in driver.page_source :
                    AddClient.OnlyQw(driver, ptelephone)

                # 如果客户只有微信
                else:
                    logger.info("以前没有添加过此手机号，开始添加")
                    AddClient.OnlyWechat(driver, ptelephone)

                logger.info("结束添加客户："+ ptelephone)
                logger.info("------------------------------------------------")

            logger.info("端口" + str(port) +"的所有手机号添加完成！")
            logger.info("员工一共添加" + str(sendNum) + "个客户")



        except Exception as e:
            logger.exception(e)
            os._exit(0)

        finally:
            endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            logger.info("脚本开始时间：" + startTime)
            logger.info("脚本结束时间："+ endTime )

