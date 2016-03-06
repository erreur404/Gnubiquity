# -*- coding: utf-8 -*-from NaoApplication import *from naoqi import ALProxyclass Stop(Features):    def __init__(self, robotProxy):        self.name = "Stop"        self.bot = robotProxy    def run(self, robotIP, feature):               # Instanciation proxy pour la posture initiale         postureProxy = self.bot.gMotionProxy                   # Instanciation proxy pour les mouvements des bras lors de la marche        motionProxy = self.bot.gPostureProxy        # Arret des mouvements et mise en position initiale                  motionProxy.stopMove()        postureProxy.goToPosture("StandInit", 0.5)        