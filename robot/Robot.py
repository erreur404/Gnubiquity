# -*- coding: utf-8 -*-

# classe d instanciation des robots
class Robot:
    def __init__(self, name, IPAdress, port, robotState, videoState, type):
        self.name = name
        self.IPAdress = IPAdress      
        self.port = port              # 9559
        self.robotState = robotState
        self.videoState = videoState
        self.type = type
              
class Nao(Robot):
    def __init__(self, NaoIP, NaoPort):
        self.NaoIP = NaoIP
        self.NaoPort = NaoPort
