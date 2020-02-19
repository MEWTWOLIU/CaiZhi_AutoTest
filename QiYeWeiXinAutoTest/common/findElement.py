from selenium.webdriver.support.ui import WebDriverWait
from QiYeWeiXinAutoTest.common.Mylogger import logger
from QiYeWeiXinAutoTest.common.OpenCaiZhiApplet import OpenApp


# 暂时用不上
class findElement(object) :

   def __init__(self, driver):
       self.driver = driver

   # element_type : 查找元素利用的属性
   # element_value ：查找元素的属性值
   def findElement(self, element_type, element_value):

       try:

           if element_type == "id":
               element = WebDriverWait(self.driver, 10).until(lambda driver:driver.find_element_by_id(element_value), "找不到元素")
               return element
           elif element_type == "path":
               element = WebDriverWait(self.driver, 10).until(lambda driver:driver.find_element_by_xpath(element_value), "找不到元素")
               return element
           elif element_type == "android_text":
               logger.info(self.driver.find_element_by_android_uiautomator('new UiSelector().textContains(' + element_value + ')'))
               element = WebDriverWait(self.driver, 10).until(lambda driver:driver.find_element_by_android_uiautomator('new UiSelector().textContains("' + element_value + '")'), "找不到元素")
               return element
           elif element_type == "css":
               element = WebDriverWait(self.driver, 10).until(lambda driver:driver.find_element_by_css_selector(element_value), "找不到元素")
               return element
           elif element_type == "accessibility_id":
               element = WebDriverWait(self.driver, 10).until(lambda driver:driver.find_element_by_accessibility_id(element_value), "找不到元素")
               return element




       except Exception as e:
           logger.exception(e)


