import sys
import time
import random
import math
import motion
import almath as m # python's wrapping of almath
import almath
import argparse
import Image

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
from Robot import *

class Features:

    def __init__(self, name):
        self.name = name
    
    def runOnRobot(self, Nao, forward, backward, right, left):
        self.run(Nao.NaoIP, forward, backward, right, left)
        
