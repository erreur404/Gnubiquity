################################
#    IMPORTS                   #
################################
from flask import Flask, render_template, Response, request
import time

# emulated camera
from robotDebug import Robot


#*****************************#
#     CONSTANTS & CONFIG      #
#*****************************#
FPS_LIMIT = 15
IPV6 = False



#=========================#
#    OBJECTS              #
#=========================#
app = Flask(__name__)

robot = Robot()


#------------------------#
#    FLASK APP           #
#------------------------#

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Video streaming home page."""
    return render_template('AboutUs.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        a = time.clock()
        frame = camera.get_frame() # fetching 1 image from the robot
        delta = time.clock()-a # time elapsed during request to robot
        delta = (1.0/FPS_LIMIT) - delta # diff between time elapsed and FPS limit period
        if (delta > 0): # delta > 0 => frame acquisition faster than FPS period
            time.sleep(delta)
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(robot),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/command', methods=['POST'])
def command():
    #print(request.form)
    if (request.form["idle"] == 'true'):
        robot.setPositionIdle()
    elif (request.form["rest"] == 'true'):
        robot.setPositionRest()
    elif (request.form["cue"] == 'true'):
        robot.setPositionCue()
    robot.moveForward(int(request.form["avancer"]))
    robot.turn(int(request.form["tourner"]))
    """
    print("idle : "+str(request.form["idle"])+"\n"+
          "rest : "+str(request.form["rest"])+"\n"+
          "cue : "+str(request.form["cue"]))
    """
    return "0"

@app.route('/say', methods=['POST'])
def say():
    #return "received !"
    #return str(request.body)
    return str(request.form["Say"])

if __name__ == '__main__':
	host_name = "0.0.0.0"
	if (IPV6):
	    host_name = "::"
	    print("Server running IPV6 on port "+str(host_port))
	else:
            host_name = "0.0.0.0"
        app.run(host=host_name, port=80, debug=True, threaded=True)
