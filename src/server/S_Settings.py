class Settings:
    def __init__(self):
        self.svrIp = '0.0.0.0'
        self.svrPort = 9999


    def _restore(self):
        self.svrIp = '0.0.0.0'
        self.svrPort = 9999