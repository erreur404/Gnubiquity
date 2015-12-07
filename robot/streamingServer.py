#!/usr/bin/env python
from flask import Flask, render_template, Response
import os
   

class StreamingServer():
    def __init__(self, robot):
        app = Flask(__name__)
        self.robot = robot

        @app.route('/')
        def index():
            #raise NameError(os.getcwd())
            return render_template('index.html')

        def gen(camera):
            while True:
                frame = self.robot.get_frame()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        @app.route('/video_feed')
        def video_feed():
            print "getting image"
            return Response(self.robot,
                            mimetype='multipart/x-mixed-replace; boundary=frame')

        self.app = app

    def run(self):
        print "running server"
        self.app.run(host='0.0.0.0', debug=True, threaded=True)
