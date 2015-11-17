class Robot:

    def __init__(self, name, IPAdress, port, robotState, videoState, type):
       
        self.name = name
        self.IPAdress = IPAdress      # "127.0.0.1"
        self.port = port             # 9559
        self.robotState = robotState
        self.videoState = videoState
        self.type = type
              

class Nao(Robot):
    'Common base class for all Nao'
    
    def __init__(self, NaoIP, NaoPort):
        
        self.NaoIP = NaoIP
        self.NaoPort = NaoPort