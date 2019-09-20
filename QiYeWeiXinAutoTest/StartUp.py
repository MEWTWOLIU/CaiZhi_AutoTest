from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

###adb shell dumpsys activity top | grep  ACTIVITY
# ACTIVITY com.tencent.wework/com.tencent.mm.plugin.appbrand.ui.AppBrandUI fd1cae pid=10088

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': '66J0219128011699',
    'appPackage': 'com.tencent.wework',
    'appActivity': '.login.controller.LoginWxAuthActivity',
    'automationName': 'Appium',
  #  'unicodeKeyboard': 'True',
  #  'resetKeyboard': 'True',ps
    'fullReset': False,
    'noReset': 'True',
    'chromeOptions': {'androidProcess': 'com.tencent.wework'}
}
ip = '192.168.0.193'
host = 'http://'+ip+':4723/wd/hub'
driver = webdriver.Remote(host,desired_caps)

time.sleep(10)