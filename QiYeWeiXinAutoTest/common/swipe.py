from appium import webdriver



def getScreenSize(driver):

    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


def swipeUp(driver,t):

    L = getScreenSize(driver)
    x_start = int(L[0]*0.5)
    y_start = int(L[1]*0.75)
    y_end = int(L[1]*0.25)
    driver.swipe(x_start,y_start,x_start,y_end,t)

def swipeDown(driver,t):

    L = getScreenSize(driver)
    x_start = int(L[0]*0.5)
    y_start = int(L[1]*0.25)
    y_end = int(L[1]*0.75)
    driver.swipe(x_start,y_start,x_start,y_end,t)

def swipeRight(driver,t):

    L = getScreenSize(driver)
    x_start = int(L[0]*0.5)
    x_end = int(L[0]*0.75)
    y_start = int(L[1]*0.5)
    driver.swipe(x_start,y_start,x_end,y_start,t)

def swipeLeft(driver,t):

    L = getScreenSize(driver)
    x_start = int(L[0]*0.5)
    x_end = int(L[0]*0.1)
    y_start = int(L[0]*0.5)
    driver.swipe(x_start,y_start,x_end,y_start,t)
