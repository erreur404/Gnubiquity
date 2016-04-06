################################
#    IMPORTS                   #
################################
from flask import Flask, render_template, Response, request
import time
import wave

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
	
@app.route('/description')
def description():
	return render_template('Description.html')


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

@app.route("/audio_feed")
def audio_feed():
    return ""

@app.route('/command', methods=['POST'])
def command():
    #print(request.form)
    if (request.form["idle"] == 'true'):
        robot.setPositionIdle()
    elif (request.form["rest"] == 'true'):
        robot.setPositionRest()
    elif (request.form["cue"] == 'true'):
        robot.setPositionCue()
    robot.motion(
        {
            'leftx':int(request.form["leftx"]),
            'lefty':int(request.form["lefty"]),
            'rightx':int(request.form["rightx"]),
            'righty':int(request.form["righty"])
        }
    )
    robot.cameraMotion({
        'yaw':int(request.form["yaw"]),
        'pitch':int(request.form["pitch"])
    })
    return "0"

@app.route('/say', methods=['POST'])
def say():
    robot.sayText(request.form["message"])
    return str(request.form["message"])

@app.route('/sound', methods=['POST'])
def replayVoice():
    s = request.files["file"]
    res = wave.open(s, 'r')
    length = res.getnframes()
    res = res.readframes(length)
    print(res.count('\0'))
    robot.playSound(res) #.replace('\0', '')
    return "0"

if __name__ == '__main__':
	host_name = "0.0.0.0"
	if (IPV6):
	    host_name = "::"
	    print("Server running IPV6 on port "+str(host_port))
	else:
            host_name = "0.0.0.0"
        app.run(host=host_name, port=80, debug=True, threaded=True)
