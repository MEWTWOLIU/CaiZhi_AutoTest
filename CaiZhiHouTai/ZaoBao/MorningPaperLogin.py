from selenium import webdriver
from CaiZhiHouTai.common.GetCookies import getCookieValue

def CookieToCookieDict(cookies):
    cookieDict = {}
    for cookieName, cookieValue in cookies.items():
        cookieDict['name'] = cookieName
        cookieDict['value'] = cookieValue
        # cookieDict['domain'] = 'test.tengmoney.com'
    return cookieDict


def MorningPaperLogin():
    Configuration = {
        "url": "https://test.tengmoney.com/caizhi_op/#/",
        "cookieName": "morning_paper_cookie"
}

    getCookies = getCookieValue(Configuration["cookieName"])
    # rs = requests.session()
    # rslogin = rs.get(Peizhi["url"], headers=headers, cookies=getCookies, verify=False)
    # rslogin.encoding = 'utf-8'
    # print(rslogin.text)


    driver = webdriver.Chrome()
    print("chrome本地登录cookie为：" + str(CookieToCookieDict(getCookies)))
    # 首次加载页面，让selenium识别cookie是谁的
    driver.get(Configuration["url"])
    driver.maximize_window()
    driver.add_cookie(CookieToCookieDict(getCookies))
    driver.get(Configuration["url"])

    driver.implicitly_wait(10)
    try:
        assert "文章管理" in driver.page_source
        print("登录成功！")
        return driver
    except AssertionError as e:
        return "登录失败！"
