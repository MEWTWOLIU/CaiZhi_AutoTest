from selenium import webdriver

Peizhi = {
   # "url": "https://test.tengmoney.com/caizhi_op/#/"
    "url": "https://www.baidu.com"
}

brower = webdriver.Chrome()
print(Peizhi["url"])
brower.get(Peizhi["url"])
# brower.page_source
 brower.implicitly_wait(10) # 10s等待
# brower.quit()