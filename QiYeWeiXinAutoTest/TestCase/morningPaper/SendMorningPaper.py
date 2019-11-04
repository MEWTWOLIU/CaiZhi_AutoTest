from QiYeWeiXinAutoTest.TestCase.morningPaper import OpenCaiZhiApplet
from time import sleep
from assertpy import assert_that

try:
    xpth = {
        'sendBtn1': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View[19]',
        'sendBtn2': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView[3]'
    }

    driver = OpenCaiZhiApplet.OpenApp()
    print("<--------分享早报案例开始-------->")
    driver.find_element_by_android_uiautomator('new UiSelector().textContains("每日精选")').click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath(xpth['sendBtn1']).click()
    driver.implicitly_wait(3)
    driver.find_element_by_android_uiautomator('new UiSelector().textContains("发给客户")').click()
    sleep(1)
    driver.find_element_by_android_uiautomator('new UiSelector().textContains("八神")').click()
    sleep(1)

    driver.find_element_by_xpath(xpth['sendBtn2']).click()
    driver.implicitly_wait(3)
    # 发送早报后返回早报页面，识别“今日综述”
    result = driver.find_element_by_android_uiautomator('new UiSelector().textContains("今日综述")').id

    assert_that(result).is_true()
    print("分享早报成功")

except AssertionError:
    print("分享早报失败")
finally:
    print("<--------分享早报案例结束-------->")