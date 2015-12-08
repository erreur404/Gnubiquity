from time import time


class Robot(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
        self.frames = [open('_robotDebug/'+str(f) + '.jpg', 'rb').read() for f in range(1,10)]

    def get_frame(self):
        #time.sleep(0.5)
        return self.frames[int(time()) % len(self.frames)]
