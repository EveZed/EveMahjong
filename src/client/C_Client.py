from socket import *
from C_Deck import Deck
from C_Settings import Settings
from threading import Thread


settings = Settings()
tcpServer = socket()
tcpServer.connect((settings.svrIp, settings.svrPort))


deck = Deck()


def receive(deck):
    while True:
        svrData = tcpServer.recv(1024)
        if len(svrData):
            svrMsg = svrData.decode('UTF-8')
            print(f'Server:{svrMsg}')
            if svrMsg == 'DeckAck':
                tcpServer.send('OK'.encode('UTF-8'))
                while True:
                    svrDeck = tcpServer.recv(2048)
                    if len(svrDeck):
                        deck.tiles = svrDeck.loads(svrDeck)
                        break


def send(deck):
    while True:
        cliMsg = str(input('Local:'))
        tcpServer.send(cliMsg.encode('UTF-8'))
        if cliMsg == 'exit' or cliMsg == 'exit\n':
            print('You are offline.')
            tcpServer.close()
            break


if __name__ == '__main__':
    rcvT = Thread(target = receive, args = (deck))
    send(deck)