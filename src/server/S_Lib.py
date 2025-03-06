import random
import pickle


class Lib:
    def __init__(self, mode):
        self.allTiles = ['1万', '2万', '3万', '4万', '5万', '6万', '7万', '8万', '9万',
                         '1条', '2条', '3条', '4条', '5条', '6条', '7条', '8条', '9条',
                         '1筒', '2筒', '3筒', '4筒', '5筒', '6筒', '7筒', '8筒', '9筒',
                         '东', '南', '西', '北', '中', '发', '白']
        self.allTiles *= 4

        self.flowers = ['春','夏','秋','冬','梅','兰','竹','菊']

        self.x1T = []
        self.x2T = []
        self.x3T = []
        self.zT = []

        self.banker = random.randint(0, 3)

        self.playersList = []

        self.tilesZip = {}

        #  分牌
        if mode == 1:
            self.allTiles += self.flowers
        random.shuffle(self.allTiles)
        self.x1T = self.allTiles[:13]
        self.x2T = self.allTiles[13:26]
        self.x3T = self.allTiles[26:39]
        self.zT = self.allTiles[39:53]
        for i in range(53):
            self.allTiles.pop(i)#  发完牌后牌库更新

        #  压缩
        self.x1T_ = pickle.dumps(self.x1T)
        self.x2T_ = pickle.dumps(self.x2T)
        self.x3T_ = pickle.dumps(self.x3T)
        self.zT_ = pickle.dumps(self.zT)

        #  制作压缩包
        self.tilesZip[self.banker] = self.zT_
        xians = [0, 1, 2, 3]
        xians.remove(self.banker)
        self.tilesZip[xians[0]] = self.x1T_
        self.tilesZip[xians[1]] = self.x2T_
        self.tilesZip[xians[2]] = self.x3T_











if __name__ == '__main__':
    lib = Lib()