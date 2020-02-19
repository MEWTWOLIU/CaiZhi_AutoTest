# -*- coding:utf-8 -*-
from QiYeWeiXinAutoTest.common.Mylogger import logger
import datetime
import os
import re
from time import sleep

def CheckAppium(port):
    try:
        Start_port = str(port)
        findport = os.popen('netstat -aon | findstr {}'.format(Start_port)).read()
        if findport:
            logger.info("有Appium在运行，先kill掉")
            StopAppium(Start_port)


    except Exception as e:
        logger.exception(e)

def StartAppium(port):
    try:
        # Start_port = str(port)
        # findport = os.popen('netstat -aon | findstr {}'.format(Start_port)).read()
        # if findport:
        #     logger.info("有Appium在运行，先kill掉")
        #     StopAppium(Start_port)
        Start_port = str(port)
        logger.info("启动Appium")

        # 设置appium日志存储路径
        path = 'Appium_' + datetime.datetime.now().strftime("%Y-%m-%d") + '.log'
        AppiumLogPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), './log/', path)

        # 命令行启动appium
        os.system('start /b appium -a 0.0.0.0 -p ' + Start_port +' --log ' + AppiumLogPath +' --local-timezone')
        sleep(3)

    except Exception as e:
        logger.exception(e)


def StopAppium(port):
    try:
        # 查询appium进程端口
        killProcess(port)
        logger.info("Appium已关闭")




    except Exception as e:
        logger.exception(e)


def killProcess(port):
    try:
        # 查询appium进程端口
        command ='netstat -aon | findstr '+str(port)
        findport = os.popen(command).read()
        if findport:
            getportlist = re.split(r' +', findport)
            processNum = getportlist[5]

            # 杀掉对应进程
            os.system('taskkill /f /pid ' + processNum)
        else:
            logger.info(str(port) + "端口没有启动，不需要关闭")

    except Exception as e:
        logger.exception(e)

def killadb():
    try:
        # 查询adb.exe端口
        killProcess(5037)
        logger.info("adb.exe已关闭")

    except Exception as e:
        logger.exception(e)
