import os
from QiYeWeiXinAutoTest.common.Mylogger import logger

# ��ȡ����apk�ļ����µġ�.apk���ļ���Ȼ�����ֻ��ϵ�����װ���棬��Ҫ�ֶ�ȷ�ϰ�װ��������Խ��appium�����Ż�����ʱ�Ȳ���
def installAPK(apkname):

    apkpath = os.path.join(os.path.dirname(os.path.dirname(__file__)), './apk/', apkname)
    logger.info(apkpath)
    os.system('adb install {}'.format(apkpath))
