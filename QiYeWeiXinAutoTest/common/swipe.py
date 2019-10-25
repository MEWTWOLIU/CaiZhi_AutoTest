from appium import webdriver



def getScreenSize(driver):

    driver = webdriver.Remote()
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


def swipeUp(driver,t):
    l = getScreenSize(driver)