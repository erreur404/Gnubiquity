import socket
import json
import sys
import math
from Tkinter import *
from Features.Move import *
from Features.Arm import *
from Features.Stop import *
from Features.Head import *

##
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
##


class NaoApplication:
    def __init__(self):
        self.features = []
        self.robots = []
        
    def main():
            'Initialization of a new NaoApplication instance'         
            na = NaoApplication()
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
            
            'Adding the features to the list of features of the NaoAppliaction instance'

            na.features.append(sT)
            na.features.append(mO)
            na.features.append(aR)
            na.features.append(tT)
            

            "Getting a list of Features name"
            NaoFeaturesList = []
            for i in range (0, len(na.features)):
                featureName = na.features[i].name
                NaoFeaturesList.append(featureName)
            print ("Nao Features List:")

            'Adding the robot to the list of robots of the NaoApplication instance'
            na.robots.append(nao)

            'JSON Object Initialization '
            data_ident = {'From':'193.48.125.67', 'To':'193.48.125.64', 'MsgType':'Ident', 'EquipmentType':'Robot'}
            'Serializing Object Data to a JSON formated str'
            result_ident = json.dumps(data_ident)
            'New Socket Initialization'
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
        # creation d une instance de la classe TK, que lon affecte a l objet "root"
            root = Tk()
            champ_label = Label(root, text=" Gnubiquity ")
            champ_label.pack()
            feature={
                    "forward":False,
                    "backward":False,
                    "right":False,
                    "left":False,
                    "stop":False,
                    "arm":False,
                    "head":False}
            

            def clavier():
                touche = event.keysym
                print(touche)
            # Fenetre recueration touche    
            canvas = Canvas(root, width=500, height=500)
            canvas.focus_set()
            canvas.bind("<Key>", clavier)
            canvas.pack()




            def avant():
                 feature["forward"] = True
                 mO.runOnRobot(nao, feature)
                 tts.say("avant","French")
                 feature["forward"] = False
             
            def arriere():
                feature["backward"] = True
                mO.runOnRobot(nao, feature) 
                tts.say("arriere","French")
                feature["backward"] = False

            def gauche():
                feature["left"] = True
                mO.runOnRobot(nao, feature) 
                tts.say("gauche","French")
                feature["left"] = False

            def droite():
                feature["right"] = True
                mO.runOnRobot(nao, feature)
                tts.say("droite","French")
                feature["right"] = False
            
            def arret():
                print("arret demande")

                motionProxy = ALProxy("ALMotion", robotIP, 9559)
                motionProxy.stopMove()
            

        
            def bras():
                feature["arm"] = True
                aR.runOnRobot(nao,feature)
                tts.say("bras","French")
                feature["arm"] = False

            def tete():
                feature["head"] = True
                tT.runOnRobot(nao,feature)
                tts.say("tete","French")
                feature["head"] = False


            # Recuperation touches clavier
            root.bind("<KeyRelease>", arret) # relache touches 
            root.bind("<Up>", avant) # Fleche haut
            root.bind("<Down>",arriere) # Bas
            root.bind("<Left>", gauche) # Gauche
            root.bind("<Right>", droite) # Droite
            root.bind("<space>", bras) # barre despace

            while(True):
               
               # root.mainloop()

##               tete()
##               time.sleep(5)
##              
##               avant()
##               time.sleep(5)               
##               arret()
##               time.sleep(2)
##               droite()
##               time.sleep(2)
##               arret()
##               time.sleep(2)
##               arriere()
##               time.sleep(2)
##               arret()
##               time.sleep(2)
##
               if stop:
                   arret()
               elif av :
                   avant()
               elif ar :
                   arriere()
               elif dr :
                   droite()
               elif ga :
                   gauche ()
               elif br :
                    bras ()
               elif tt :
                    tete ()
               
               

                
            
    if __name__ == "__main__":
                main()

