import sys
import math
from Features.Move import *
from Features.Arm import *
from Features.Stop import *
from Features.Head import *

##
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
##


   
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
            exit()
            feature["arm"] = True
            aR.runOnRobot(nao,feature)
            tts.say("bras","French")
            feature["arm"] = False

        def tete():
            feature["head"] = True
            tT.runOnRobot(nao,feature)
            tts.say("tete","French")
            feature["head"] = False

        while(True):
                
           if  feature["stop"]:
               arret()
           elif  feature["forward"] :
               avant()
           elif  feature["backward"] :
               arriere()
           elif feature["right"]:
               droite()
           elif feature["left"] :
               gauche ()
           elif feature["arm"] :
                bras ()
           elif feature["head"] :
                tete ()
           
           

                
            
if __name__ == "__main__":
    main()

