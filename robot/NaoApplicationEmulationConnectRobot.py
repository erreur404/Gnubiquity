#------------------------------------------------ Import
import pygame
from pygame.locals import *
from time import sleep

import time
from Features.Move import *
from Features.Arm import *
from Features.Stop import *
from Features.Head import *
from Features.PhotoCapture import *
##
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
##

import math
from os.path import exists,isdir
from os import getcwd,listdir,chdir,environ
import random

PICT = "watson.jpg" #1000x600


def main(feature):
        'NAOIP_ORANGE: 193.48.125.63'
        'NAOIP_GRIS: 193.48.125.62'  
        robotIP= "193.48.125.63";
        nao = Nao(robotIP,9559)
        tts = ALProxy("ALTextToSpeech", robotIP, 9559)
        tts.setLanguage("French")# attention mise en anglais dans les proxy  a verifier 

        'Initialization of the different features'  
        sT = Stop()
        mO = Move()
        aR= Arm()
        tT= Head()
        pC = PhotoCapture()

        feature_r={
                    "forward":False,
                    "backward":False,
                    "right":False,
                    "left":False,
                    "stop":False,
                    "arm":False,
                    "head":[0.0 ,0.0 ],
                    "photo":False
                    } 

        #------------------------------------------------ CONSTANTS

        XMAX = 1000
        YMAX = 600
        POS = (0, 0)


        #------------------------------------------------ Pygame Init

        pygame.init()
        def get_relativ_pos(rel):
            return (pygame.mouse.get_pos()[0] - rel[0],pygame.mouse.get_pos()[1]-rel[1])
        pygame.mouse.get_relativ_pos = get_relativ_pos #extention of the mouse class to fit my needs
        pygame.display.set_caption("RoboSim")
        clock = pygame.time.Clock()

        ROBOT_TYPE = 'Tank'

        pygame.key.set_repeat(400, 30) #delai avant de repeter une touche

        screen = pygame.display.set_mode((XMAX, YMAX),RESIZABLE)

        sans = pygame.font.SysFont('sans',32)

        #------------------------------------------------ Classes

        class Dot:
            def __init__(self,pos,angle = 0):
                self.pos = pos
                self.angle = angle #en degres
                self.divisor = 1
                self.flag_name = ''
                self.flag_state = False

            def get_angle(self):
                return self.angle

            def set_angle(self, angle):
                self.angle = angle

            def get_pos(self):
                return self.pos

            def set_pos(self,pos):
                self.pos = pos

            def get_scrPos(self):
                return (self.pos[0] + POS[0], self.pos[1] + POS[1])

            def display(self,focus = False): #returns rect
                if focus:
                    rotated = pygame.transform.rotate(robot_ico,self.angle)
                    return workbench.blit(rotated,(self.pos[0]-35-(rotated.get_size()[0] - robot_ico.get_size()[0])/2,
                                            self.pos[1]-35-(rotated.get_size()[1] - robot_ico.get_size()[1])/2))
                else:
                    if self.flag_state :
                        return addRect((workbench.blit(line_flag,(self.pos[0]-42,self.pos[1]-50)),
                                        workbench.blit(line_hitbox,(self.pos[0]-20,self.pos[1]-20))))
                    else :
                        return workbench.blit(line_hitbox,(self.pos[0]-20,self.pos[1]-20))


        THE_ONE = Dot((300,300),0)
        #------------------------------------------------ Fonctions

        def debug(data, color=(255,255,255)):
            screen.blit(sans.render(str(data), True, color,(0,0,0)),(XMAX/2,50))
            recta = sans.size(str(data))
            #print(data)
            pygame.display.update((XMAX/2,50,recta[0],recta[1]))

        def addRect(listRect):
            #add rect tuples
            minX = listRect[0][0]
            minY = listRect[0][1]
            maxX = listRect[0][2]
            maxY = listRect[0][3]
            for i in listRect:
                if i[0] < minX:
                    minX = i[i]
                if i[1] < minY:
                    minY = i[1]
                if i[0]+i[2] > maxX:
                    maxX = i[0]+i[2]
                if i[1]+i[3] > maxY:
                    maxY = i[1]+i[3]
            return (minX,minY,maxX,maxY)

        def textSpot(spot,radius,text,size):
            #cree un texte relie a un point par une ligne
            #spot est un tuple de 2 coordonnees
            #radius est un rayon en pixels autour du point
            #text est la chaine a afficher
            #size est la taille de la police (entier)
            #retourne un doublet de tuple de la zone modifiee
            #retourne False si la souris n'etait pas dans la zone
            global sans
            policy(size)
            mouse = pygame.mouse.get_pos()
            if (mouse[0]-spot[0])**2 + (mouse[1]-spot[1])**2 < radius**2:
                cell_size = sans.size(text)
                cell = pygame.Surface(cell_size)
                cell.fill((255,255,255))
                cell.blit(sans.render(text,False,(0,0,0)),(0,0))
                if mouse[0] - cell_size[0] < 0:
                    x = 0
                elif mouse[0] + cell_size[0] +10 > XMAX:
                    x = XMAX - cell_size[0] - 10
                else:
                    x = mouse[0]
                if mouse[1] - cell_size[1] < 0:
                    y = 0
                elif mouse[1] + cell_size[1] > YMAX:
                    y = YMAX - cell_size[1]
                else:
                    y = mouse[1]
                screen.blit(cell,(x+10,y))
                pygame.draw.line(screen,(255,255,255),spot,\
                                 (pygame.mouse.get_pos()[0]+10,pygame.mouse.get_pos()[1]))
                return (min(mouse[0],spot[0]),\
                        min(mouse[1],spot[1]),\
                        max(mouse[0]+cell_size[0]+10,spot[0])-min(mouse[0],spot[0]),\
                        max(mouse[1]+cell_size[1],spot[1])-min(mouse[1],spot[1]))
            return False
            
        def policy(size):
            global sans,easter
            if easter:
                sans = pygame.font.Font(ICI+'\sga.ttf',size)
            else:
                sans = pygame.font.SysFont('sans',size)

        def angleLigne(line):
            if line.get_x() == 0 and line.get_y() < 0:
                angle = -math.pi/2
            elif line.get_x() == 0 and line.get_y() >= 0:
                angle = math.pi/2
            else:
                angle = math.atan(line.get_y()/line.get_x())

            if line.get_x() >= 0 and line.get_y() <= 0:
                angle = -angle
            elif line.get_x() >= 0 and line.get_y() > 0:
                angle = 2*math.pi-angle
            elif line.get_x() < 0 and line.get_y() <=0:
                angle = math.pi - angle
            elif line.get_x() < 0 and line.get_y() > 0:
                angle = math.pi - angle
            return angle

        def getAngle(line1,line2):
            #angle trigonometrique entre 2 lignes
            angle1 = angleLigne(line1)
            angle2 = angleLigne(line2)
            angle = (angle2 - angle1)%(2*math.pi)
            return angle


        def stop():
            pygame.quit()
            input()

        def fullRefresh(dots_rebuild = True): #============== rafraichit la fenetre principale
            screen.fill((75,75,75))
            if (dots_rebuild):
                workbench.blit(workbench_bg,(0,0))
            if (dots_rebuild):
                THE_ONE.display(focus=True)
            screen.blit(workbench,POS)

        #------------------------------------------------ autres initialisations
        #===== images
        workbench_bg = pygame.image.load(PICT).convert()
        workbench = pygame.image.load(PICT).convert()

        robot_ico = pygame.image.load('robot_ico.png').convert_alpha()

        perso = {
                "x":300.0,
                "y":300.0,
                "orientation":90.0,
                "head":0.0,
                "mcoef":1.0/100,
                "tcoef":1.0/1.0
        }

        def move(s):
             perso["x"] -= s*math.sin(math.pi*2*perso["orientation"]/360)*perso["mcoef"]
             #print("speed :"+str(s)+"speedx : "+str(s*math.sin(math.pi*2*perso["orientation"]/360)*perso["mcoef"]))
             perso["y"] -= s*math.cos(math.pi*2*perso["orientation"]/360)*perso["mcoef"]
             if s > 10:
                 feature_r["forward"] = True
                 mO.runOnRobot(nao, feature_r) 
                 feature_r["forward"] = False
             elif s < -10:
                 feature_r["backward"] = True
                 mO.runOnRobot(nao, feature_r) 
                 feature_r["backward"] = False

        def turn(s):
            perso["orientation"] = (perso["orientation"]+perso["tcoef"]*s*3.6)%360
            if s > 10 :
                feature_r["left"] = True
                mO.runOnRobot(nao, feature_r) 
                feature_r["left"] = False
            elif s < -10 :
                feature_r["right"] = True
                mO.runOnRobot(nao, feature_r)
                feature_r["right"] = False

        
        def arret():
            debug("STOP")
            motionProxy = ALProxy("ALMotion", robotIP, 9559)
            motionProxy.stopMove()
    
        def bras():
            feature["arm"] = True
            debug("BRAS")
            feature["arm"] = False
            feature_r["arm"] = True
            aR.runOnRobot(nao,feature_r)
            feature_r["arm"] = False

        def prisephoto():
            feature_r["photo"] = True
            pC.runOnRobot(nao, feature_r)

        def tete():
            feature["head"] = True

            feature["head"] = False

        pygame.init()

        sound = pygame.mixer.Channel(0)

        looping = True

        while(looping):
                if  feature["stop"]:
                        arret()
                else:
                        move(feature["forward"][0])
                        turn (feature["rotation"])
                if feature["arm"] :
                        bras ()
                if feature["head"] :
                        tete ()
                if feature["sit"] :
                        debug("SITH")
                        feature["sit"] = False
                if feature["stand"] :
                        debug("STAND")
                        feature["stand"] = False

                if feature["sound"] != False:
                        print(type(feature["sound"]))
                        sound.queue(pygame.mixer.Sound(buffer = feature["sound"]))
                        feature["sound"] = False

                THE_ONE.set_angle(perso["orientation"]+perso["head"])
                THE_ONE.set_pos((perso["x"], perso["y"]))

                fullRefresh()

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                looping = False
                                pygame.quit()
                                break

                        if event.type == VIDEORESIZE:
                                screen = pygame.display.set_mode((event.w,event.h),RESIZABLE)
                                XMAX = screen.get_size()[0]
                                YMAX = screen.get_size()[1]
                                fullRefresh()
                if looping:
                        pygame.display.flip()
                        clock.tick(30)
                # blit & flip...
        pygame.quit()
pygame.quit()
