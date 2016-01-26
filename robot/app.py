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
<<<<<<< HEAD
=======

>>>>>>> master

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
    #return "received !"
    #return str(request.body)
    print (str(request.form))
    return "0"

@app.route('/say', methods=['POST'])
def say():
    #return "received !"
    #return str(request.body)
    return str(request.form["Say"])
					
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
