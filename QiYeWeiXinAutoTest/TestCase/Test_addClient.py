
from QiYeWeiXinAutoTest.common.DoAppium import StartAppium, StopAppium,killadb
from QiYeWeiXinAutoTest.TestCase.qywx.AddClient_Multi import AddClient
from QiYeWeiXinAutoTest.common.getDevices import getDeviceUnid
from QiYeWeiXinAutoTest.TestCase.qywx.AddClient_Multi import AddClient
from QiYeWeiXinAutoTest.common.Mylogger import logger
import multiprocessing
from time import sleep

deviceList = getDeviceUnid()
def appium_process():

    # deviceList = getDeviceUnid()
    appium_process = []

    logger.info(range(len(deviceList)))

    for i in range(len(deviceList)):
        port = 4723 + 2 * i

        appium = multiprocessing.Process(target=StartAppium, args=[port])
        appium_process.append(appium)


    for appium in appium_process:
        appium.start()

    for appium in appium_process:
        appium.join()
    sleep(3)

    logger.info("appium已添加完进程组")

def desired_process():

    desired_process = []
    # deviceList = getDeviceUnid()
    for i in range(len(deviceList)):
        port = 4723 + 2 * i
        logger.info("案例开始加线程组")
        desired = multiprocessing.Process(target=AddClient.test_addclient,
                                          args=["desired_caps_mate20", deviceList[i], port])
        desired_process.append(desired)
    logger.info("案例已加入进程组")

    for desired in desired_process:
        logger.info("启动案例")
        desired.start()
    for desired in desired_process:
        desired.join()
    logger.info("案例全部启动")

def StopAppium_process():

    StopAppium_process = []
    # deviceList = getDeviceUnid()
    for i in range(len(deviceList)):
        port = 4723 + 2 * i
        stopappium = multiprocessing.process(target=StopAppium, args=[port])
        StopAppium_process.append(stopappium)

    for stopappium in StopAppium_process:
        stopappium.start()
    for stopappium in StopAppium_process:
        stopappium.join()



if __name__ == '__main__':
    #
    # for i in range(len(getDeviceUnid())):
    #     port = 4723 + 2 * i
    #     StopAppium(port)
    # killadb()
    #
    # sleep(3)
    # appium_process()

    logger.info("启动appium完成,开始跑案例")

    desired_process()
    # StopAppium(4723)





