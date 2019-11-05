import logging.handlers
import datetime

nowTime = datetime.datetime.now().strftime("%Y-%m-%d")
log_path = "C:/Users/47557/PycharmProjects/CaiZhi_AutoTest/QiyeWeiXinAutoTest/log/"
logName = log_path+nowTime+".log"

logging.basicConfig(filename="test.log",
                    filemode="a", ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志 #a是追加模式，默认如果不写的话，就是追加模式
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%Y-%M-%D %H:%M:%S",
                    level=logging.DEBUG)

logger = logging.getLogger("logger")

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