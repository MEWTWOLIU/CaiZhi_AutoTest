# -*- coding:utf-8 -*-
from QiYeWeiXinAutoTest.common.Mylogger import logger
import os,subprocess
import re
import sys


def connectDevices():
    try:
        logger.info("--------开始检查手机设备连接情况--------")
        output = subprocess.check_output('adb devices')
        deviceInfo = output.decode()
        deviceUnid = re.findall('\r\n(.+?)\t', deviceInfo)

        if not deviceUnid :
            logger.info("---没有手机连接这台电脑！---")
            sys.exit()
        else:
            logger.info("---发现设备---")
            return True
    except Exception as e:
        logger.error("--------手机设备连接失败--------")
        logger.exception(e)
        quit()



def getDeviceUnid():
    try:
        # 获取手机unid
        if connectDevices():
            output = subprocess.check_output('adb devices')
            deviceInfo = output.decode()
            deviceUnid = re.findall('\r\n(.+?)\t', deviceInfo)
            # logger.info("手机unid："+deviceUnid[0]+'\n')
            # return deviceUnid[0]
            logger.info(deviceUnid)
            return deviceUnid
        else:
            logger.info("---连接超时，请重新连接---")
    except Exception as e:
        logger.error(e)

def getDeviceSysVer():
    try:
        # 获取手机系统版本
        if connectDevices():
            file = os.popen('adb shell getprop ro.build.version.release')
            platformVersion = file.read()
            logger.info("手机系统为："+platformVersion+'\n')
            return platformVersion
        else:
            logger.info("--------获取手机系统版本失败，请重试！--------")
    except Exception as e:
        logger.exception(e)

def getDeviceName():
    try:
        if connectDevices():
            file = os.popen('adb shell getprop ro.product.brand')
            deviceName = file.read()
            logger.info("手机名称: "+deviceName+'\n')
            return deviceName
        else:
            logger.info("--------获取手机名称失败，请重试--------")
    except Exception as e:
        logger.exception(e)


