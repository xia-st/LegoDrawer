from drawer import Pen, Paper
import math

class Canvas:
    def __init__(self):
        self.pen = Pen()
        self.paper = Paper()
        self.curX = 0
        self.curY = 0
        self.speed = 1

    def reset(self):
        self.curX = 0
        self.curY = 0

    def init(self):
        self.pen.up()
        self.waitUpDown()

    def startDraw(self):
        '''
        抬起笔，载入纸张，准备画图
        '''
        self.penUp()
        self.paper.loadPaper()
        self.paper.waitScroll()

    def stopDraw(self):
        '''
        抬起笔，送出纸张，结束画图
        '''
        self.penUp()
        self.paper.scrollOut()
        self.paper.waitScroll()

    def penUp(self):
        self.pen.up()
        self.pen.waitUpDown()

    def penDown(self):
        self.pen.down()
        self.pen.waitUpDown()

    def goto(self, x, y):
        dx = x -curX
        dy = curY
        l = math.sqrt(dx*dx+dy*dy)
        speedX = self.speed * (dx / l)
        speedY = self.speed * (dy / l)
        self.pen.move(dx, speedX)
        self.paper.scroll(dy, speedY)
        self.pen.waitMove()
        self.paper.waitScroll()
        curX = x
        curY = y
