# 自动获取设备信息
from QiYeWeiXinAutoTest.common.Mylogger import logger
import os,subprocess
import re

def connectDevices():
    try:
        logger.info("--------开始检查手机设备连接情况--------")
        deviceInfo = subprocess.check_output("adb devices")
        if deviceInfo[1] == "":
            logger.info("---没有手机连接这台电脑！---")
            return False
        else:
            logger.info("---发现设备---")
            return True
    except Exception as e:
        logger.info("--------手机设备连接失败--------")
        logger.error(e)



def getDeviceInfo():
    try:
        # 获取手机unid
        if connectDevices():
            deviceInfo = subprocess.check_output('adb devices')
            logger.info("手机unid："+str(deviceInfo))
            return deviceInfo
        else:
            logger.info("---连接超时，请重新连接---")
    except Exception as e:
        logger.error(e)

def getDevicePlatVer():
    try:
        # 获取手机系统版本
        if connectDevices():
            platformVersion = os.popen('adb shell getprop ro.build.version.release')
            logger.info("手机系统为："+str(platformVersion))
            return platformVersion
        else:
            logger.info("--------获取手机系统版本失败，请重试！--------")
    except Exception as e:
        logger.error(e)

def getDeviceName():
    try:
        if connectDevices():
            deviceName = os.popen('adb shell getprop ro.product.name')
            logger.info("手机名称"+str(deviceName))
            return deviceName
        else:
            logger.info("--------获取手机名称失败，请重试--------")
    except Exception as e:
        logger.error(e)
