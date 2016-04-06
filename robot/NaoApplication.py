import sysimport mathimport timeimport osfrom Features.Move import *from Features.Arm import *from Features.Stop import *from Features.Head import *from Features.Rest import *from Features.Stand import *from Features.PhotoCapture import *from naoqi import ALProxyfrom naoqi import ALBrokerfrom naoqi import ALModuleclass ProxyBot:    gMotionProxy = False    gPostureProxy = False    gNavigationProxy = False   def main(feature):        'NAOIP_ORANGE: 193.48.125.63'        'NAOIP_GRIS: 193.48.125.62'          robotIP= "193.48.125.62"        nao = Nao(robotIP,9559)        robotProxy = ProxyBot()        timeLastMove = time.time()        # Instanciatoin des differents proxys communs aux features        try:            tts = ALProxy("ALTextToSpeech", robotIP, 9559)            tts.setLanguage("French")        except Exception, e:            print "Could not create proxy to ALTextToSpeech"            print "Error was: ", e                'Initialization of the shared proxys'        try:            robotProxy.gMotionProxy = ALProxy("ALMotion", robotIP, 9559)        except Exception, e:            print "Could not create proxy to ALMotion"            print "Error was: ", e                try:            robotProxy.gPostureProxy = ALProxy("ALRobotPosture", robotIP, 9559)        except Exception, e:            print "Could not create proxy to ALRobotPosture"            print "Error was: ", e        try:            robotProxy.gNavigationProxy = ALProxy("ALNavigation", robotIP, 9559)        except Exception, e:            print "Could not create proxy to ALRobotPosture"            print "Error was: ", e        try:                       gAutonomousLife = ALProxy("ALAutonomousLife", robotIP, 9559)        except Exception, e:            print "Could not create proxy to ALAutonomousLife"            print "Error was: ", e                    'Initialization of the different features'        tT= Head(robotProxy)        rT= Rest(robotProxy)        sU= Stand(robotProxy)        sT = Stop(robotProxy)        mO = Move(robotProxy)        aR= Arm(robotProxy)        pC = PhotoCapture()        gAutonomousLife.setState("disabled")                                       # fonction appelant les proxys en fonction de la demande du serveur        def avant():            timeLastMove = time.time()            if robotProxy.gMotionProxy and robotProxy.gPostureProxy:                mO.runOnRobot(nao, feature)          def rotation():            timeLastMove = time.time()            if robotProxy.gMotionProxy and robotProxy.gPostureProxy:                mO.runOnRobot(nao, feature)         def arret():            print("arret demande")            feature["stop"] = True            sT.runOnRobot(nao,feature)            motionProxy = ALProxy("ALMotion", robotIP, 9559)            motionProxy.stopMove()            feature["stop"] = False                            def bras():            feature["arm"] = True            if robotProxy.gMotionProxy and robotProxy.gPostureProxy:                aR.runOnRobot(nao,feature)            feature["arm"] = False        def tete():            timeLastMove = time.time()-1            if robotProxy.gPostureProxy:                tT.runOnRobot(nao,feature)        def prisephoto(definition):            feature["photo"] = True            print("definition : "+str(definition))            pC.runOnRobot(nao, feature)                    def repos():            feature["sit"] = True            if robotProxy.gPostureProxy:                rT.runOnRobot(nao, feature)            feature["sit"] = False                    def debout():            timeLastMove = time.time()-2            feature["stand"] = True            if robotProxy.gPostureProxy:                sU.runOnRobot(nao, feature)            feature["stand"] = False        # recuperation ordres serveur        while(True):            if  feature["stop"]:                print "je marrete"                arret()            elif  feature["forward"][0]!=0.0 or feature["forward"][1]!=0.0  :                avant()                          elif  feature["sit"] :                repos()            elif  feature["stand"] :                debout()            elif feature["rotation"]!=0:                rotation()            elif feature["arm"] :                bras ()            elif  feature["head"]["yaw"]!=0.0 or feature["head"]["pitch"]!=0.0  :                tete ()                feature["head"]["yaw"]=0.0                feature["head"]["pitch"]=0.0            elif feature["text"] != "" :                tts.say(str(feature["text"]))                feature["text"] = ""            if feature["photo"] == True:                prisephoto(min(int(time.time() - timeLastMove), 3))                                                         if __name__ == "__main__":    main(feature)