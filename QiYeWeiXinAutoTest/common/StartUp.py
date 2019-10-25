from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

###adb shell dumpsys activity top | grep  ACTIVITY
# ACTIVITY com.tencent.wework/com.tencent.mm.plugin.appbrand.ui.AppBrandUI fd1cae pid=10088
# com.tencent.wework/.login.controller.LoginWxAuthActivity
def startup()
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '9',
        'deviceName': 'nova4手机',  #
        'appPackage': 'com.tencent.wework',
        'appActivity': '.launch.LaunchSplashActivity',
        'automationName': 'Appium',
        'unid': 'GPGDU19129002582',
      #  'unicodeKeyboard': 'True',
      #  'resetKeyboard': 'True',ps
        'fullReset': False,
        'noReset': 'true',
        'chromeOptions': {'androidProcess': 'com.tencent.wework'}
    }
    ip = '192.168.0.192'  # 服务器IP地址
    host = 'http://'+ip+':4723/wd/hub'  # appium访问路径
    driver = webdriver.Remote(host,desired_caps)

    return driver


