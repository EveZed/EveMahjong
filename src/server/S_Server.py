from socket import *
from threading import Thread, Lock
from S_Settings import Settings
from S_Lib import Lib


settings = Settings()
lock = Lock()
orderP1 = ''


#启动服务器
tcpServer = socket()
tcpServer.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
svrAddr = (settings.svrIp, settings.svrPort)
tcpServer.bind(svrAddr)
tcpServer.listen(10)


'''def initialize():
    global lib
    lib = Lib()'''


def waitM(lib):
    while True:
        cliSocket, cliAddr = tcpServer.accept()
        cliT = Thread(target = dealClient, args = (cliSocket, cliAddr, lib))
        print(f'\n{cliAddr[0]} entered the game.')
        with lock:
            lib.cliNum += 1
            lib.playersList.append(cliAddr[0])
        print(f"Number of players online:{lib.cliNum}")
        cliT.start()

        if lib.cliNum == 4:
            break


def dealClient(cliSocket, cliAddr, lib):
    orderL1 = ''
    cliSocket.send('You have entered the game. Please wait for other players...'.encode('UTF-8'))
    waitS(cliSocket, cliAddr, lib)
    localNum = lib.playerslist.index(cliAddr[0])#获取客户端编码
    waitI(orderP1, 'Sending tiles')
    localTiles = lib.tilesZip[localNum]
    cliSocket.send('DeckAck'.encode('UTF-8'))
    waitO(cliSocket, 'OK')
    cliSocket.send(localTiles)#向客户端发牌


def waitS(cliSocket, cliAddr, lib):
    while True:
        cliData = cliSocket.recv(1024)
        if len(cliData):
            cliMsg = cliData.decode("UTF-8")
            print(f"{cliAddr[0]}:{cliMsg}")
            if (cliMsg == 'exit\n' or cliMsg == 'exit'):#客户端退出
                with lock:
                    lib.cliNum -= 1
                    lib.playersList.remove(cliAddr[0])
                print(f'{cliAddr[0]} is offline.(situation 1)')
                print(f"Number of players online:{lib.cliNum}.")
                cliSocket.close()
                break
        else:
            with lock:
                lib.cliNum -= 1
                lib.playersList.remove(cliAddr[0])
            print(f"{cliAddr[0]} is offline.(situation 2)")
            print(f"Number of players online:{lib.cliNum}.")
            cliSocket.close()
            break
        if lib.cliNum == 4:
            break


def waitI(order, msg):
    while True:
        if order == msg:
            break


def waitO(cliSocket,msg):
    while True:
        cliData = cliSocket.recv(1024)
        if len(cliData):
            cliMsg = cliData.decode('UTF-8')
            if cliMsg == msg:
                break


if __name__ == '__main__':
    lib = Lib()
    waitM(lib)
    lib.deal(0)#洗牌+分牌+序列化
    order = 'Sending tiles'