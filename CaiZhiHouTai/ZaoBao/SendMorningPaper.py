from CaiZhiHouTai.ZaoBao.MorningPaperLogin import MorningPaperLogin
from CaiZhiHouTai.common.findToast import findToast
from time import sleep

import datetime


def SendPaper():
    # 登录
    mpDriver = MorningPaperLogin()

    timestemp = datetime.datetime.now().strftime('%Y-%m-%d')

    # 早报内容
    inputs = {
        'title': '这是第' + timestemp + '期自动发送的测试早报',
        'summary1': '这是第一条综述',
        'summary2': '喜提热搜的背后\n蕴含着我们每一个深圳人对祖国的热爱\n对自己是一个中国人而感到骄傲',
        'summary3': '我爱我的国，我爱我的家，有了强的国，才有富的家。虽然你并不完美，但我们仍然热爱这片土地，一代代坚持不懈的努力完善祖国。爱我中华！中国，加油！',
        'TextHGSS': {'url': 'https://mp.weixin.qq.com/s/ZipMalAIf5xANCKggsbQaQ',
                     'summary': '中奖的也太爽了！羡慕啊',
                     'comment': '哈哈哈哈哈哈，多多关注我们龙华COCO City的活动哟，说不定下一个锦鲤就是你'
                     },
        'TextJRSC': {'url': 'https://mp.weixin.qq.com/s/oT_HeVmPfrAI6K6kw_qwIw',
                     'summary': '嗯？你们七夕礼物都这么多花样？\n但小麻逗我安排的「乌龙的朗读者」见面会也很有趣！\n小麻逗又要来跟你们面基啦\n详情戳第3条推送^_^',
                     'comment': '一直都是一个人过七夕，今天早上在蛋糕店，老板给我打了七七折，还送了杯豆浆'
                     },
        'TextHYDS': {'url': 'https://mp.weixin.qq.com/s/QxcWqlKQc4PyKHSSE2XJSg',
                     'summary': '最新报道:小麻逗已被领导移出开心麻花剧组群！',
                     'comment': '哈哈哈哈哈哈哈哈哈哈哈哈你最好笑\n海报太敷衍，本月奖金扣除\n'
                     },
        'TextLCGC': {'url': 'https://mp.weixin.qq.com/s/fHRrpbT36NLKNjDjYypNWg',
                     'summary': '人人都爱马悦勋',
                     'comment': '太可惜了，这次去不了正好出去玩儿了……下次有这种活动肯定得来啊！'
                     },
        'TextDCLS': {'url': 'https://mp.weixin.qq.com/s/M8LgdL87JOXW1X5Tvgytlg',
                     'summary': '想知道各个演员的名字 现场说的太快没记住',
                     'comment': '潘龙、王雨姝、罗月宁、林瀚青'
                     },
        'TextQQSJ': {'url1': 'https://mp.weixin.qq.com/s/1kj0goT6sHekSbbyqSICzg',
                     'summary1': '转发本文至朋友圈并集10个赞，截图并发送至小麻花客服号：szxiaomahua，得到确认后就可以参与抽奖啦！人人有份！（开奖时间：9月12日 16：00）',
                     'comment1': '不转，反正中不到！！',
                     'url2': 'https://mp.weixin.qq.com/s/9muYOWvPBdAnKHYGFEhjQQ',
                     'summary2': '《乌龙山伯爵》每一个笑点都精心设计，服务于人物，爆笑却毫无突兀感。除了主角戏份精彩，配角也同样笑点十足。',
                     'comment2': '作为开心麻花最经典的一部作品，看《乌龙山伯爵》已经成了万千开心麻花戏迷心中的情结。'
                     },
        'OneDayTalk': '有观众曾经连刷82次，有观众提前3个月买票，有观众在网上分享剧中台词被多次转载，有观众专程飞到临近的演出城市看戏，有观众曾戏言：\n没看过《乌龙山伯爵》，都不算真正看过开心麻花。'
    }

    # 点进早报
    mpDriver.find_element_by_class_name("ant-menu-submenu-title").click()
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"/article$Menu\"]/li/a").click()
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"title\"]/div/div[1]/div[1]/div/button").click()
    sleep(1)



    # 输入标题、综述、
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[2]/div/div/span/input").send_keys(inputs['title'])
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[4]/div/div/span/div/textarea").send_keys(inputs['summary1'])
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[4]/div/div/span/div/i").click()
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[4]/div/div/span/div[2]/textarea").send_keys(inputs['summary2'])
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[4]/div/div/span/div[2]/i[2]").click()
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[4]/div/div/span/div[3]/textarea").send_keys(inputs['summary3'])
    sleep(1)


    # 滚屏操作 核心思想是用selenium执行js代码
    mpDriver.execute_script("window.scrollBy(0,10000)")
    sleep(1)


    # 早报正文、概述、点评、
    # 宏观时事

    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[6]/div/div/span/div/button[1]").click()
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[6]/div/div/span/div/i").click()
    sleep(1)
    mpDriver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/form/div[1]/div[2]/div/span/input").send_keys(inputs['TextHGSS']['url'])
    sleep(1)
    for n in range(3):
        mpDriver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[1]").click()
        mpDriver.implicitly_wait(10)
        findToast(mpDriver,"获取成功")



    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[7]/div/div/span/div/textarea").send_keys(inputs['TextHGSS']['summary'])
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[7]/div/div/span/div/div[1]/div[2]/div/span/textarea").send_keys(inputs['TextHGSS']['comment'])
    sleep(1)

    #金融市场
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[6]/div/div/span/div/button[2]").click()
    sleep(1)
    mpDriver.find_element_by_xpath( "//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[6]/div/div/span/div/i").click()
    sleep(1)
    mpDriver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/form/div[1]/div[2]/div/span/input").send_keys(inputs['TextJRSC']['url'])
    sleep(1)
    mpDriver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[1]").click()
    mpDriver.implicitly_wait(10)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[7]/div/div/span/div/textarea").send_keys(inputs['TextJRSC']['summary'])
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[7]/div/div/span/div/div[1]/div[2]/div/span/textarea").send_keys(inputs['TextJRSC']['comment'])
    sleep(1)


    # 行业大事
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[6]/div/div/span/div/button[3]").click()
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[6]/div/div/span/div/i").click()
    sleep(1)
    mpDriver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/form/div[1]/div[2]/div/span/input").send_keys(inputs['TextHYDS']['url'])
    sleep(1)
    mpDriver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[1]").click()
    mpDriver.implicitly_wait(10)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[7]/div/div/span/div/textarea").send_keys(inputs['TextHYDS']['summary'])
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[7]/div/div/span/div/div[1]/div[2]/div/span/textarea").send_keys(inputs['TextHYDS']['comment'])
    sleep(1)


    # 理财观察
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[6]/div/div/span/div/button[4]").click()
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[6]/div/div/span/div/i").click()
    sleep(1)
    mpDriver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/form/div[1]/div[2]/div/span/input").send_keys(inputs['TextLCGC']['url'])
    sleep(1)
    mpDriver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[1]").click()
    mpDriver.implicitly_wait(10)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[7]/div/div/span/div/textarea").send_keys(inputs['TextLCGC']['summary'])
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[7]/div/div/span/div/div[1]/div[2]/div/span/textarea").send_keys(inputs['TextLCGC']['comment'])
    sleep(1)


    # 地产楼市
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[6]/div/div/span/div/button[5]").click()
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[6]/div/div/span/div/i").click()
    sleep(1)
    mpDriver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/form/div[1]/div[2]/div/span/input").send_keys(inputs['TextDCLS']['url'])
    sleep(1)
    mpDriver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[1]").click()
    mpDriver.implicitly_wait(10)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[7]/div/div/span/div/textarea").send_keys(inputs['TextDCLS']['summary'])
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[7]/div/div/span/div/div[1]/div[2]/div/span/textarea").send_keys(inputs['TextDCLS']['comment'])
    sleep(1)


    # 全球视角
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[6]/div/div/span/div/button[6]").click()
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[6]/div/div/span/div/i").click()
    sleep(1)
    mpDriver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/form/div[1]/div[2]/div/span/input").send_keys(inputs['TextQQSJ']['url1'])
    sleep(1)
    mpDriver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[1]").click()
    mpDriver.implicitly_wait(10)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[7]/div/div/span/div/textarea").send_keys(inputs['TextQQSJ']['summary1'])
    sleep(1)
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[7]/div/div/span/div/div[1]/div[2]/div/span/textarea").send_keys(inputs['TextQQSJ']['comment1'])
    sleep(1)


    # 一日谈
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[9]/div/div/span/textarea").send_keys(inputs['OneDayTalk'])


    # 点击保存
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[10]/div/div/span/div/div/div/div/span/button[2]").click()
    mpDriver.implicitly_wait(10)


    # 点击预览
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[10]/div/div/span/div/div/div/div/span/button[1]").click()
    mpDriver.implicitly_wait(10)
    mpDriver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/button").click()
    sleep(1)


    # 点击发布
    mpDriver.find_element_by_xpath("//*[@id=\"RewriteNewspaper\"]/div[1]/div/div/form/div[10]/div/div/span/div/div/div/div/span/button[3]").click()
    mpDriver.implicitly_wait(10)