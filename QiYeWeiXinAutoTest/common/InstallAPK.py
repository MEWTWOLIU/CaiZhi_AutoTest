import os
from QiYeWeiXinAutoTest.common.Mylogger import logger

# 读取放在apk文件夹下的“.apk”文件，然后在手机上弹出安装界面，需要手动确认安装，后面可以结合appium进行优化，暂时先不做
def installAPK(apkname):

    apkpath = os.path.join(os.path.dirname(os.path.dirname(__file__)), './apk/', apkname)
    logger.info(apkpath)
    os.system('adb install {}'.format(apkpath))
