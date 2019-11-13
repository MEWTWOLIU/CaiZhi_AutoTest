from QiYeWeiXinAutoTest.TestCase.morningPaper import *
from QiYeWeiXinAutoTest.TestCase.morningPaper.SendMorningPaper import SendMorningPaper
from QiYeWeiXinAutoTest.common.getDevices import *
from QiYeWeiXinAutoTest.common.StartUp import startup
from QiYeWeiXinAutoTest.common.DoYml import *
from QiYeWeiXinAutoTest.common.sendReport import sendReport
import yaml
import time
import unittest
import HTMLTestRunner



if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest( SendMorningPaper("test_SendMorningPaper"))


    sendReport(suite)
