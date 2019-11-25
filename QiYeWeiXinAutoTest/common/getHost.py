import socket

# 通过计算机名称来获取计算机IP地址
def getHost():

    # 获取计算机名称
    PC_name = socket.gethostname()
    # 获取IP地址
    IP = socket.gethostbyname(PC_name)
    return IP