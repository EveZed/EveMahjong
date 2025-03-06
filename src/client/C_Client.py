from socket import *
from C_Deck import Deck
from C_Settings import Settings
from threading import Thread
import pickle


settings = Settings()
tcpServer = socket()
tcpServer.connect((settings.svrIp, settings.svrPort))


deck = Deck()


def receive(deck):
    #print(1)
    while True:
        svrData = tcpServer.recv(1024)
        if len(svrData):
            try: #  接收信息
                svrMsg = svrData.decode('UTF-8')
                print(f'Server:{svrMsg}')
            except UnicodeDecodeError: #  接收牌组
                deck.tiles = pickle.loads(svrData)
                if len(deck.tiles) == 14:
                    print('You are chosen randomly to be the banker and please discard first.')
                else:
                    print('You are not the banker. Please wait for other players to discard.')
                deck.tidyUp()
                deck.printTiles()


def sendMsg():
    while True:
        cliMsg = str(input('Local:'))
        tcpServer.send(cliMsg.encode('UTF-8'))
        if cliMsg == 'exit' or cliMsg == 'exit\n':
            print('You are offline.')
            tcpServer.close()
            break


if __name__ == '__main__':
    rcvT = Thread(target = receive, args = (deck,))
    rcvT.start()
    sendMsg()