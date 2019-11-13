from QiYeWeiXinAutoTest.common.Mylogger import logger
from QiYeWeiXinAutoTest.common.DoYml import *
import HTMLTestRunner
import os
import time

def sendReport(suite):
    try:

        # 报告文件名称及存放路径
        timestr = time.strftime('%Y%m%d%H%M%S',time.localtime())
        # 存放报告绝对路径
        filepath = 'C:/Users/47557/PycharmProjects/CaiZhi_AutoTest/QiYeWeiXinAutoTest/report/'
        reportPath = filepath + timestr + '.html'

        # 报告title
        title = '腾银自动化测试报告'

        Report = os.path.join(reportPath)
        with open(Report, 'wb') as R:
            runner = HTMLTestRunner.HTMLTestRunner(stream=R,verbosity=2,title=title,description='撰写人：刘洋')
            # 执行测试
            runner.run(suite)
        logger.info("----------测试报告已生成，请前往查看-----------")

    except Exception as e:
        logger.exception(e)
        sys.exit()

