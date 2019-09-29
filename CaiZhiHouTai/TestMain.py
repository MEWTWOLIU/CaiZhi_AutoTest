from CaiZhiHouTai.common.GetToken import gettoken
from CaiZhiHouTai.common.GetCookies import getCookieFromChrome
from CaiZhiHouTai.common.GetCookies import getCookieValue
from CaiZhiHouTai.ZaoBao.SendMorningPaper import SendPaper

if __name__ == '__main__':

  # main = getCookieFromChrome("https://test.tengmoney.com/caizhi_op/#/")
  main = SendPaper()
  print(main)