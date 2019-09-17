from tkinter import *
from tkinter import messagebox
from win32crypt import CryptUnprotectData
import requests
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

def houmen(corpId,paperId):
    # 定义cookie对象 https://test.qtrade.com.cn   morning_paper_cookie  125ac2a968c0462897bc1b16bf1d8cd5
    host = "https://test.tengmoney.com"
    # 将推送给哪个机构
    VcorpId = corpId   #"ww8c83d949a80b562d"
    # 需要推送的早报id
    VpaperId = paperId  #"125ac2a968c0462897bc1b16bf1d8cd5"
    # 拼接url
    url = host + "/caizhi_manage/api/morning/push/to_corp.do?" + "corpId=" + VcorpId + "&" + "paperId=" + VpaperId


    # ————————————————————推送早报————————————————————

    # 把cookie插入信息头中
    Vcookies = getCookieFromChrome()

    headers = {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "zh-CN,zh;q=0.9",
      "Connection": "keep-alive",
      "Host": "test.qtrade.com.cn",
      "Referer": "https://test.tengmoney.com/caizhi_op/",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }
    # 发送请求
    req = requests.get(url, headers=headers, cookies=Vcookies)
    print(req.text)
    print("corpId: " + VcorpId)
    print("paperId: " + VpaperId)
    if req.text.__contains__("ok") :
      messagebox._show(title=corpId + "&" + paperId, message="已发布早报，稍后请企业微信查看，谢谢~")
    else:
      messagebox._show(title=corpId + "&" + paperId, message=req.text)



# 界面主题
HelloView = Tk()
HelloView.title("发早报后门")
HelloView.geometry('300x150')
# 机构输入框
L1 = Label(HelloView, text="输入要推送早报的机构ID（corpId）")
L1.pack()
corp_text = StringVar()
corp = Entry(HelloView,textvariable = corp_text)
corp.pack()
# 早报输入框
L2 = Label(HelloView,text = "输入要推送的早报Id（paperId）")
L2.pack()
paper_text = StringVar()
paper = Entry(HelloView,textvariable = paper_text)
paper.pack()


# 提交按钮
Button(HelloView, text="发布早报", command=lambda: houmen(corp.get(), paper.get())).pack()

HelloView.mainloop()