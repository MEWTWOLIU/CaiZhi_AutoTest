from win32crypt import CryptUnprotectData
import sqlite3
import os
import requests
# 获取cookies



def getCookieValue(cookieName):
    # 本体存储cookie的路径
    cookiePath = os.environ['LOCALAPPDATA']+r"\Google\Chrome\User Data\Default\Cookies"
    # 取数sqlite
    sql = "select host_key, name, encrypted_value from cookies where name = '"+cookieName+"'"
    # 连接cookie文件取cookie
    with sqlite3.connect(cookiePath) as conn:
        cu = conn.cursor()
        cookiesValue = {name:CryptUnprotectData(encrypted_value)[1].decode() for host_key,name,encrypted_value in cu.execute(sql).fetchall()}
        return cookiesValue

# 暂时没法用，需要绕过扫码登录
def getCookieFromChrome(url):

    rs = requests.session()
    req = rs.get(url)
    cookieDict = requests.utils.dict_from_cookiejar(req.cookies)
    print(cookieDict)
    return cookieDict
