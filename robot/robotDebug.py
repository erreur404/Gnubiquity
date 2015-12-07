class Robot():
    def __init__(self):
        imagez = []
        for i in range(1,31):
            imagez.append("_robotDebug\\"+str(i)+".jpg")
        print imagez
        self.imgs = []
        self.index = 0
        for name in imagez:
            self.imgs.append(open(name, 'rb'))

    def get_frame(self):
        self.index = (self.index+1)%len(self.imgs)
        return self.imgs[self.index]
