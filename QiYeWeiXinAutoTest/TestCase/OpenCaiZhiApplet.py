from selenium.webdriver.common.by import By

from QiYeWeiXinAutoTest.common import swipe
from QiYeWeiXinAutoTest.common.StartUp import startup
from selenium.webdriver.support import expected_conditions as ec
from assertpy import assert_that
from time import sleep



try:
    print("------------案例执行开始------------")
    xPKeyValue = {
        '新翰财智': '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[14]/android.widget.TextView'

    }

    driver = startup()

    driver.find_element_by_android_uiautomator('text(\"工作台\")').click()

    swipe.swipeUp(driver,1000)

    driver.find_elements_by_android_uiautomator('new UiSelector().textContains("新翰财智")')[1].click()

    sleep(5)

    locator = (By.ID, '	com.tencent.wework:id/ck')
    text = u'新翰财智'
    result = ec.presence_of_element_located(locator, text)

    assert_that(result).is_true()
    print('成功打开财智小程序')

except AssertionError :
    print('财智小程序打开失败')

finally:
    print("------------案例执行结束------------")

