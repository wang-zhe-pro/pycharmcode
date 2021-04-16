import cv2
import turtle

class ProcessPic:
    def __init__(self, path):
        self.path = path
        self.img = None
        self.edge = None
        self.gray = None
        self.thresh = None
        self.ret = None

    def Imread(self):
        # cv读取图片
        self.img = cv2.imread(self.path, 0)
        # self.img = cv2.resize(self.img, (500, 500))

    # '/home/soleman/桌面/OIP._wR9bwaDSvYv88x5nXx_tQHaGW.jpg'
    def Shape(self):
        return self.img.shape

    def Canny(self):
        # cv中的边缘检测
        if self.img is not None:
            self.edge = cv2.Canny(self.img, 100, 200)
        else:
            print("Wrong!")

    def Gray(self):
        # 进行灰度处理
        if self.edge is not None:
            self.gray = cv2.cvtColor(self.edge, cv2.COLOR_BAYER_BG2GRAY)
        else:
            print("Wrong!")

    def Threshould(self):
        # 获取图像阈值
        if self.edge is not None:
            self.ret, self.thresh = cv2.threshold(self.gray, 180, 255, 0)
        else:
            print("Wrong!")

    def Imshow(self):
        if self.edge is not None:
            cv2.imshow("image_Canny", self.edge)
        if self.gray is not None:
            cv2.imshow("image_gray", self.gray)
        if self.thresh is not None:
            cv2.imshow('image_threshold', self.thresh)

        cv2.waitKey(0)
        # cv2.destroyWindow()


a = ProcessPic('/home/soleman/桌面/1.jpg')
a.Imread()
a.Canny()
a.Gray()
a.Threshould()
# a.Imshow()
contours, hierarchy = cv2.findContours(a.thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
xy = []
for i in range(0,len(contours)):
    x, y, w, h = cv2.boundingRect(contours[i])
    list_xy = [x, y]
    xy.append(list_xy)


def draw(xy):
    turtle.pensize(2)

    turtle.setup(width=500, height=500)

    turtle.speed(1000)

    for array in xy[::-1]:
        turtle.penup()

        turtle.goto((array[0] / 2) - 300, -(array[1] / 2) + 300)

        turtle.pendown()

        turtle.forward(1)

        #print(turtle.pos())

    turtle.done()


draw(xy)
