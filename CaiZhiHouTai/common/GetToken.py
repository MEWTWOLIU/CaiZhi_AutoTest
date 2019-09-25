import requests
from http import cookiejar
import urllib3


def gettoken():
    # 测试环境
    host = "test.qtrade.com.cn"
    path = "/caizhi_miniapi/index/auth.do"
    userId = "mr.joker"
    corpId = "ww8c83d949a80b562d"

    # 从cookie中获取caizhi_managekey
    params = {"userId":userId,"corpId":corpId}
    url = host + path
    r = requests.get(url,params)
    print(r)

    if "caizhi_managekey" in r.cookies :
        token = r.cookies

    print("token获取成功！")
    return token

