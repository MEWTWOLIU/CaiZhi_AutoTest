# -*- coding:utf-8 -*-
from QiYeWeiXinAutoTest.common.Mylogger import logger

import os
# 暂时用不上
def apkinstall(apkname):
    try:
        filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), './apk', apkname)
        logger.info(filepath)
        os.system('adb install' + filepath)
    except Exception as e:
        logger.exception(e)
