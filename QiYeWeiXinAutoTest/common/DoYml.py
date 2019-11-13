from QiYeWeiXinAutoTest.common.getDevices import *
from QiYeWeiXinAutoTest.common.Mylogger import *
import yaml

# 配置文件存放路径
# file_path = '../config/desired_caps.yml'
# 读取yaml文件
def readYml(file_path):
    try:
        fopen = open(file_path, encoding='utf-8')
        print(type(fopen))
        fload = yaml.load(fopen, Loader=yaml.FullLoader)
        fopen.close()
        logger.info("读取成功")
        return fload
    except Exception as e:
        logger.exception(e)
        logger.error("读取失败")


# 暂时没用上写的
def writeYml(file_path, dict):
    try:
        fopen = open(file_path,'a+',encoding='utf-8')
        yaml.dump(dict,fopen)
        logger.info("写入成功！")
        fopen.close()
    except Exception as e:
        logger.exception(e)
        logger.error(("写入失败！"))
