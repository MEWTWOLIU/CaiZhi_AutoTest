from QiYeWeiXinAutoTest.TestCase.morningPaper import *
from QiYeWeiXinAutoTest.TestCase.morningPaper.SendMorningPaper import SendMorningPaper
from QiYeWeiXinAutoTest.common.getDevices import *
from QiYeWeiXinAutoTest.common.StartUp import startup
from QiYeWeiXinAutoTest.common.DoYml import *
from QiYeWeiXinAutoTest.common.sendMail import sendMail
from QiYeWeiXinAutoTest.common.sendReport import sendReport
from QiYeWeiXinAutoTest.TestCase.qywx.AddClient import AddClient
import yaml
import time
import unittest
import HTMLTestRunner


if __name__ == '__main__':

    # path = os.path.join(os.path.dirname(__file__), './TestYaml/morningPaperRunner.yml')
    # f = readYml(path)
    # 有问题，明天接着查 ，addTest里面不能用str，要用具体的TestCase类

    suite = unittest.TestSuite()
    suite.addTest(AddClient.test_addclient())
    sendReport(suite)

