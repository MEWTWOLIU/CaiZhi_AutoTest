from selenium.webdriver.support.ui import WebDriverWait
# 暂时用不上
class findElement(object) :

   def __init__(self, driver):
       self.driver = driver

   # element_type : 查找元素利用的属性
   # element_value ：查找元素的属性值
   def findElement(self, element_type,element_value):

       if element_type == "id":
           WebDriverWait(self.driver, 5).until(lambda driver:driver.find_element_by_id(element_value))
           element = self.driver.find

