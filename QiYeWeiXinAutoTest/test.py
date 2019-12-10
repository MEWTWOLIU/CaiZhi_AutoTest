from QiYeWeiXinAutoTest.TestCase.morningPaper import *
from QiYeWeiXinAutoTest.TestCase.morningPaper.SendMorningPaper import SendMorningPaper
from QiYeWeiXinAutoTest.common.InstallAPK import installAPK
from QiYeWeiXinAutoTest.common.getDevices import *
from QiYeWeiXinAutoTest.common.StartUp import startup
from QiYeWeiXinAutoTest.common.DoYml import *
from QiYeWeiXinAutoTest.common.sendMail import sendMail
from QiYeWeiXinAutoTest.common.sendReport import sendReport
from QiYeWeiXinAutoTest.TestCase.qywx.AddClient_mate20 import AddClient
from QiYeWeiXinAutoTest.common.getHost import getHost
from QiYeWeiXinAutoTest.common.DoAppium import StopAppium,StartAppium
from QiYeWeiXinAutoTest.common.DoExcel import readExcel
import yaml
import time
from time import sleep
import unittest
import HTMLTestRunner
import pandas as pd


if __name__ == '__main__':

    # path = os.path.join(os.path.dirname(__file__), './TestYaml/morningPaperRunner.yml')
    # f = readYml(path)
    # 有问题，明天接着查 ，addTest里面不能用str，要用具体的TestCase类

    # suite = unittest.TestSuite()
    # suite.addTest(AddClient.test_addclient)
    # sendReport(suite)

    # 启动appium server
    # StartAppium()
    #
    # test = AddClient()
    # test.test_addclient()
    #
    # #关闭appiusm server
    # StopAppium()














