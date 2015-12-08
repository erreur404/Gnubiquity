from time import time


class Robot(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
        self.frames = [open('_robotDebugFps/'+str(f) + '.bmp', 'rb').read() for f in range(1,101)]
        self.fps = 15

    def get_frame(self):
        return self.frames[int(time()*self.fps) % len(self.frames)]
