from CaiZhiHouTai.ZaoBao.MorningPaperLogin import MorningPaperLogin

def SendPaper():
    # 登录
    mpDriver = MorningPaperLogin()
    # 点进早报
    mpDriver.find_element_by_xpath("/html/body/div/div/div/section/aside/div/div/ul/li/div[1]/span/span").click()
    mpDriver.implicitly_wait(3)
    mpDriver.find_element_by_xpath("/html/body/div/div/div/section/aside/div/div/ul/li/ul/li/a/span").click()
    mpDriver.implicitly_wait(3)
    mpDriver.find_element_by_xpath("/html/body/div/div/div/section/section/div/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div/button").click()
    mpDriver.implicitly_wait(3)
