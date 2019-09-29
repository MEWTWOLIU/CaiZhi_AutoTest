from win32crypt import CryptUnprotectData
import sqlite3
import os
# 获取cookies



def getCookieFromChrome():
    cookiePath = os.environ['LOCALAPPDATA']+r"\Google\Chrome\User Data\Default\Cookies"
    sql = "select host_key, name, encrypted_value from cookies where name = 'morning_paper_cookie'"
    with sqlite3.connect(cookiePath) as conn:
        cu = conn.cursor()
        cookies = {name:CryptUnprotectData(encrypted_value)[1].decode() for host_key,name,encrypted_value in cu.execute(sql).fetchall()}
        return cookies