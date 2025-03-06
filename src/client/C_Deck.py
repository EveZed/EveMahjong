class Deck:
    def __init__(self):
        self.tiles = []
        self.wans = []
        self.tongs = []
        self.tiaos = []
        self.fengs = []

    def tidyUp(self):
        for tile in self.tiles:
            if tile[-1] == '万':
                self.wans.append(tile)
            elif tile[-1] == '筒':
                self.tongs.append(tile)
            elif tile[-1] == '条':
                self.tiaos.append(tile)
            else:
                self.fengs.append(tile)

            self.wans.sort()
            self.tongs.sort()
            self.tiaos.sort()
            self.fengs.sort()


    def printTiles(self):
        print(self.wans)
        print(self.tongs)
        print(self.tiaos)
        print(self.fengs)