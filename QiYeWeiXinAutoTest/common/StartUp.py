# -*- coding utf-8 -*-
from appium import webdriver
from QiYeWeiXinAutoTest.common.Mylogger import logger
from QiYeWeiXinAutoTest.common.getDevices import *
from QiYeWeiXinAutoTest.common.DoYml import *
from QiYeWeiXinAutoTest.common.getHost import getHost

import yaml
import sys

def startup():
    try:
        # 读取desired_caps配置文件
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), './config/desired_caps.yml')
        desiredDefult = readYml(file_path)

        # 获取手机动态信息
        desiredDynamic = {
            'deviceName': getDeviceName().replace('\n', '').replace('\r', ''),
            'unid': getDeviceUnid().replace('\n', '').replace('\r', ''),
            'platformVersion': getDeviceSysVer().replace('\n', '').replace('\r', '')
        }

        # 把配置文件和动态获取的手机信息合并为desired_caps
        desired_caps = {}
        desired_caps.update(desiredDefult['desired_caps'])
        desired_caps.update(desiredDynamic)
        ip = getHost()

        host = 'http://'+ip+':4723/wd/hub'  # appium访问路径deviceName: 'HUAWEI

        driver = webdriver.Remote(host, desired_caps)

        logger.info("---------企业微信启动成功！----------")

        return driver
    except Exception as e:
        logger.exception(e)
        sys.exit()


