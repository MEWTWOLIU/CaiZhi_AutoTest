# -*-coding:utf-8-*-
from QiYeWeiXinAutoTest.common.Mylogger import logger
import pandas
import os

# 读取ȡExcel
def readExcel(filename):
    try:
        localpath = os.path.dirname(os.path.dirname(__file__))
        filepath = os.path.join(localpath,'./Excel/',filename)

        data = pandas.read_excel(filepath)
        logger.info('成功读取excel文件')
        return data
    except Exception as e:
        logger.exception(e)


# 读取Excel