import logging.handlers
import datetime

nowTime = datetime.datetime.now().strftime("%Y-%m-%d")
log_path = "C:/Users/47557/PycharmProjects/CaiZhi_AutoTest/QiyeWeiXinAutoTest/log/"
logName = log_path+nowTime+".log"

logger = logging.getLogger()

handler1 = logging.StreamHandler()
handler2 = logging.FileHandler(filename=logName, encoding='utf-8')

logger.setLevel(logging.DEBUG) # 这句干啥用的？
handler1.setLevel(logging.INFO)
handler2.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

logger.addHandler(handler1)
logger.addHandler(handler2)