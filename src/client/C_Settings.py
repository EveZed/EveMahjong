class Settings:
    def __init__(self):
        self.svrIp = '127.0.0.1'
        self.svrPort = 9999
        self.cliNum = 0


    def _restore(self):
        self.svrIp = '0.0.0.0'
        self.svrPort = 9999


