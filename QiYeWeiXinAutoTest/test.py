# -*- coding:utf-8 -*-
import unittest

from QiYeWeiXinAutoTest.TestCase.morningPaper import *
from QiYeWeiXinAutoTest.TestCase.morningPaper.Demo_SendMorningPaper import SendMorningPaper
from QiYeWeiXinAutoTest.TestCase.qywx import AddClient_mate20
from QiYeWeiXinAutoTest.TestCase.qywx.AddClient_Multi import AddClient
from QiYeWeiXinAutoTest.common.getHost import getHost
from QiYeWeiXinAutoTest.common.DoAppium import StopAppium, StartAppium, killadb
from QiYeWeiXinAutoTest.common.Mylogger import logger


from QiYeWeiXinAutoTest.common.DoAppium import StartAppium,StopAppium
from QiYeWeiXinAutoTest.TestCase.qywx.demo_AddClient_mate20 import AddClient

def test():

    StartAppium(4723)
    sucessful_flag = False
    while True:
        try:
            AddClient()
            sucessful_flag = True
        except Exception as e:
            logger.exception(e)
            logger.info("重启程序！")
            continue
        if sucessful_flag:
            break
    StopAppium(4723)

if __name__ == '__main__':

    # suite = unittest.TestSuite()
    # suite.addTest(SendMorningPaper("test_SendMorningPaper"))
    # sendReport(suite)

    # test()
    element_value = "非常好"
    logger.info('new UiSelector().textContains("' + element_value + '")')





















