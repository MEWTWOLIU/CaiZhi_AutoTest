import HTMLTestRunner
import os
import time

def reportConfig():

    # 报告文件名称及存放路径
    timestr = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    reportPath = '../report/' + timestr + '.html'

    # 报告title
    title = '腾银自动化测试报告'

    Report = os.path.join(reportPath)
    with open(Report, 'wb') as R:
        runner = HTMLTestRunner.HTMLTestRunner(stream=R,verbosity=2,title=title,description='撰写人：刘洋')

    # 执行测试
    runner.run()