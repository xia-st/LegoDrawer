from drawer import Pen, Paper
import math
import time

class Canvas:
    def __init__(self):
        self.pen = Pen()
        self.paper = Paper()
        self.curX = 0
        self.curY = 0
        self.maxX = 1.5
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
        time.sleep(0.1)

    def penDown(self):
        self.pen.down()
        time.sleep(0.1)

    def goto(self, x, y):
        if x > self.maxX:
            print('x too large')
            x = self.maxX

        if x < 0:
            print('x too small')
            x = 0

        if y < 0:
            print('y too small')
            y = 0

        dx = x - self.curX
        dy = y - self.curY
        print('dxy', dx, dy)

        # if abs(dx) < 0.01: # remove too short route
        #     x = self.curX
        #     dx = 0

        # if abs(dy) < 0.01:
        #     y = self.curY
        #     dy = 0

        l = math.sqrt(dx*dx+dy*dy)
        if l == 0:
            return

        # if (dx == 0 or dy == 0) and l < 0.07:
        #     return

        speedX = abs(self.speed * (dx / l))
        speedY = abs(self.speed * (dy / l))
        if speedX > speedY:
            speedY = speedY / speedX
            speedX = 1
        else:
            speedX = speedX / speedY
            speedY = 1
        self.paper.scroll(dy, speedY)
        self.pen.move(dx, speedX)
        self.pen.waitMove(int(l*30000))
        self.paper.waitScroll(int(l*30000))
        self.curX = x
        self.curY = y
        time.sleep(0.2)

def main():
    c = Canvas()
    c.penDown()
    c.goto(1.5, 0)
    c.goto(1.5, 1.5)
    c.goto(0, 1.5)
    c.goto(0, 0)
    # t = 40
    # x = 0
    # y = 0
    # l = 1.5 / t
    # for i in range(0, t):
    #     x += l
    #     c.goto(x, y)
    #     y += l
    #     c.goto(x, y)
    # c.goto(0, 1.5)
    # c.goto(0, 0)
    c.penUp()


if __name__ == '__main__':
    main()
