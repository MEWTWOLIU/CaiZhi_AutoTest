from QiYeWeiXinAutoTest.common.getDevices import *
from QiYeWeiXinAutoTest.common.Mylogger import *
import yaml

# 配置文件存放路径
# 参数：
# file_path =  例：'../config/desired_caps.yml'
# 读取yaml文件
# 编写人：刘洋
# 创建时间：2019-11-4
def readYml(file_path):
    try:
        fopen = open(file_path, encoding='utf-8')
        if not fopen :
            logger.error("文件为空或文件路径不正确！")
            sys.exit()
        fload = yaml.load(fopen, Loader=yaml.FullLoader)
        fopen.close()
        logger.info("文件读取成功")
        return fload
    except Exception as e:
        logger.exception(e)
        logger.error("文件读取失败")


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
