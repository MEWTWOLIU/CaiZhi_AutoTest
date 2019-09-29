from CaiZhiHouTai.ZaoBao.MorningPaperLogin import MorningPaperLogin
from time import sleep
def SendPaper():
    # 登录
    mpDriver = MorningPaperLogin()

    # 点进早报
    mpDriver.find_element_by_class_name("ant-menu-submenu-title").click()
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"/article$Menu\"]/li/a").click()
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"title\"]/div/div[1]/div[1]/div/button").click()
    sleep(1)

    #输入标题、综述、


    # 早报正文、概述、点评、


    # 一日谈


    # 点击预览


    # 点击发布
