from socket import *
from threading import Thread, Lock
from S_Settings import Settings
from S_Lib import Lib
from InnerMsg import InnerMsg, OuterMsg
import random


# 等待客户端加入
def waitForClient(orders, outerMsg, lib, settings):
    while True:
        cliSocket, cliAddr = tcpServer.accept()
        cliT = Thread(target = _dealClient, args = (cliSocket, cliAddr, lib, orders, settings, outerMsg))
        cliT.start()#  客户端子线程开始
        print(f'{cliAddr[0]} entered the game.')
        with lock:
            settings.cliNum += 1
        print(f"Number of players online:{settings.cliNum}")

        if settings.cliNum == 4:
            outerMsg.full = True
            break


#  客户端子线程
def _dealClient(cliSocket, cliAddr, lib, orders, settings, outerMsg):
    tMsg = ''
    innerMsg = InnerMsg()
    recvT = Thread(target = _receive, args = (cliSocket, cliAddr, settings, innerMsg))
    recvT.start() #  开始监听客户端信息
    while True:
        if innerMsg.signal: #  检测（内部）心跳信号
            if outerMsg.full: #检测是否满员
                break
        else: #  客户端断开，结束线程（状态更新没做完）
            cliSocket.close()
            print('A client is now offline.')
            print(f"Number of players online:{settings.cliNum}")
            break
    #  开始游戏
    localOrder = _getOrder(orders)
    localTiles = lib.tilesZip[localOrder]
    cliSocket.send(localTiles) #  发牌




#  接收客户端信息，存入实例
def _receive(cliSocket, cliAddr, settings, innerMsg):
    while True:
        cliData = cliSocket.recv(1024)
        if len(cliData):
            try:
                cliMsg = cliData.decode("UTF-8")
                print(f"{cliAddr[0]}:{cliMsg}")
                innerMsg.r2s = cliMsg

                if (cliMsg == 'exit\n' or cliMsg == 'exit'):  # 客户端退出
                    with lock:
                        settings.cliNum -= 1
                    #  报告客户端退出
                    innerMsg.signal = False
                    break
            except:
                pass


#  获取编号
def _getOrder(orders):
    with lock:
        l = len(orders)
        if l > 1:
            i = random.randint(0,l - 1)
        else:
            i = 0
        orderGot = orders.pop(i)
    return orderGot



if __name__ == '__main__':
    cliNum = 0
    settings = Settings()
    lock = Lock()
    orders = [0, 1, 2, 3]
    outerMsg = OuterMsg()

    # 启动服务器
    tcpServer = socket()
    tcpServer.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    svrAddr = (settings.svrIp, settings.svrPort)
    tcpServer.bind(svrAddr)
    tcpServer.listen(10)
    print('The server is now running.')


    lib = Lib(0)#  后台初始化（无花）
    waitForClient(orders, outerMsg, lib, settings)#  等待客户端加入并开启线程

