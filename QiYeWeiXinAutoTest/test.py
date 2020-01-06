from QiYeWeiXinAutoTest.TestCase.morningPaper import *
from QiYeWeiXinAutoTest.TestCase.morningPaper.SendMorningPaper import SendMorningPaper
from QiYeWeiXinAutoTest.TestCase.qywx import AddClient_mate20
from QiYeWeiXinAutoTest.common.InstallAPK import installAPK
from QiYeWeiXinAutoTest.common.getDevices import *
from QiYeWeiXinAutoTest.common.StartUpSingle import startup
from QiYeWeiXinAutoTest.common.DoYml import *
from QiYeWeiXinAutoTest.common.sendMail import sendMail
from QiYeWeiXinAutoTest.common.sendReport import sendReport
from QiYeWeiXinAutoTest.TestCase.qywx.AddClient_Multi import AddClient
from QiYeWeiXinAutoTest.common.getHost import getHost
from QiYeWeiXinAutoTest.common.DoAppium import StopAppium, StartAppium, killadb
from QiYeWeiXinAutoTest.common.DoExcel import readExcel
import yaml
import time
from time import sleep
import unittest
import HTMLTestRunner
import pandas as pd
from QiYeWeiXinAutoTest.common.DoAppium import StartAppium,StopAppium


if __name__ == '__main__':

    # suite = unittest.TestSuite()
    # suite.addTest(SendMorningPaper("test_SendMorningPaper"))
    # sendReport(suite)

    StartAppium(4723)

    AddClient_mate20.AddClient

    StopAppium(4723)



















