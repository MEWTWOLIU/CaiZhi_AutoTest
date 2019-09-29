from selenium import webdriver
from CaiZhiHouTai.common.GetCookies import getCookieValue
import requests

def CookieToCookieDict(cookies):
    cookieDict = {}
    for cookieName, cookieValue in cookies.items():
        cookieDict['name'] = cookieName
        cookieDict['value'] = cookieValue
        # cookieDict['domain'] = 'test.tengmoney.com'
    return cookieDict

Peizhi = {
    "url": "https://test.tengmoney.com/caizhi_op/#/",
    "cookieName": "morning_paper_cookie"
}
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Connection": "keep-alive",
#     "Host": "test.qtrade.com.cn",
#     "Referer": "https://test.tengmoney.com/caizhi_op/",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
# }

getCookies = getCookieValue(Peizhi["cookieName"])
# rs = requests.session()
# rslogin = rs.get(Peizhi["url"], headers=headers, cookies=getCookies, verify=False)
# rslogin.encoding = 'utf-8'
# print(rslogin.text)


driver = webdriver.Chrome()
print(CookieToCookieDict(getCookies))
# 首次加载页面，让selenium识别cookie是谁的
driver.get(Peizhi["url"])
driver.add_cookie(CookieToCookieDict(getCookies))
driver.get(Peizhi["url"])

driver.implicitly_wait("文章管理", 10)






# brower.quit()