from selenium import webdriver
import requests


def gettoken():
    # 测试环境
    host = "http://test.qtrade.com.cn"
    path = "/caizhi_miniapi/index/auth.do"
    userId = "mr.joker"
    corpId = "ww8c83d949a80b562d"

    # chromedrvier.exe存放位置
    chrome_path = r"C:\Users\47557\AppData\Roaming\npm\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win\chromedrvier.exe"

    # 从cookie中获取caizhi_managekey
    Chromeparams = {"userId":userId,"corpId":corpId}
    hosturl = host + path

    # drivers = webdriver.Chrome()
    req = requests.get(url=hosturl,params=Chromeparams)
    print(req.cookies)
    if "caizhi_key" in req.cookies :
        cookies = req.cookies['caizhi_key']
        print("token获取成功: "+cookies)
    else:
        cookies = ""
        print("token获取失败！")
    return cookies

