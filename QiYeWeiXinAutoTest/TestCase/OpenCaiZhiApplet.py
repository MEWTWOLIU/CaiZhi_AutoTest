from QiYeWeiXinAutoTest.common.StartUp import startup
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

xPKeyValue = {
    '新翰财智': '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[14]/android.widget.TextView'

}

driver = startup()

driver.find_element_by_android_uiautomator('text(\"工作台\")').click()



driver.find_elements_by_android_uiautomator('new UiSelector().textContains("新翰财智")')[1].click()

sleep(2)

locator = ('resource-id', '	com.tencent.wework:id/ck')
text = u'新翰财智'
result = ec.presence_of_element_located(locator, text)

if WebDriverWait(driver,10).until(result) :
    print('打开财智小程序')
else:
    print('财智小程序打开失败')

