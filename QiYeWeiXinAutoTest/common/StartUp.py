from appium import webdriver
from QiYeWeiXinAutoTest.common.Mylogger import logger

def startup():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '9',
      #  'deviceName': 'nova4手机',
        'deviceName': 'huaweiMate20',
        'appPackage': 'com.tencent.wework',
        'appActivity': '.launch.LaunchSplashActivity',
        'automationName': 'Appium',
      #  'unid': 'GPGDU19129002582',
         'unid': '66J0219128011699',
        'fullReset': False,
        'noReset': 'true',
        'chromeOptions': {'androidProcess': 'com.tencent.wework'}
    }
    ip = '192.168.0.197'  # 服务器IP地址
    host = 'http://'+ip+':4723/wd/hub'  # appium访问路径
    driver = webdriver.Remote(host,desired_caps)

    # logging.info(type(driver))

    return driver


