from ev3dev2.motor import MediumMotor, LargeMotor, SpeedPercent
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C
class Pen:
    def __init__(self):
        self.__udm = MediumMotor(OUTPUT_B) # up and down motor
        self.__lrm = LargeMotor(OUTPUT_A)
        self.isUp = False
        self.loading = False
        self.baseSpeed = 40
        self.ll = 0
        self.lr = 5
        pass

    def up(self, d=0.6):
        self.__udm.on_for_rotations(SpeedPercent(75), d)
        self.isUp = True

    def down(self, d=0.6):
        # 放下笔
        self.__udm.on_for_rotations(SpeedPercent(75), -d)
        self.isUp = False

    def load(self):
        if self.loading:
            return

        self.loading = True
        self.__udm.on_for_rotations(SpeedPercent(75), 4)

    def loaded(self):
        if not self.loading:
            return

        self.__udm.on_for_rotations(SpeedPercent(75), -4)
        self.loading = False

    def adjustUpDown(self, angle):
        # 调整放下笔的角度，angle正数为放下，负数为抬起
        pass

    def move(self, d, speed=1):
        # 笔移动距离d，正数向右，负数向左
        if d == 0:
            return
        self.__lrm.on_for_rotations(SpeedPercent(self.baseSpeed*speed), d, block=False)

    def moveToLeft(self):
        # 移动笔的位置到最左边，用于结束绘制后移动到最左边
        pass

    def waitMove(self, t=None):
        # 等待笔左移右移结束
        self.__lrm.wait_until_not_moving(t)

class Paper:
    def __init__(self):
        self.baseSpeed = 40
        self.__r = 0.713 # x = 4.85, y = 6.80, x / y == 0.713
        self.__m = LargeMotor(OUTPUT_C)

    def scroll(self, d, speed=1):
        if d == 0:
            return
        self.__m.on_for_rotations(SpeedPercent(self.baseSpeed*speed*self.__r), -d*self.__r, block=False)

    def scrollOut(self):
        # 把纸张送出去
        pass

    def loadPaper(self):
        # 滚动到读取到纸张的位置，如果读到纸张返回True，不然返回False
        pass

    def waitScroll(self, t=None):
        # 等待滚动完成
        self.__m.wait_until_not_moving(t)

def test():
    import time
    paper = Paper()
    pen = Pen()
    pen.down()

    pen.move(1.5)
    pen.waitMove()
    time.sleep(0.1)

    paper.scroll(1.5)
    paper.waitScroll()
    time.sleep(0.1)

    pen.move(-1.5)
    pen.waitMove()
    time.sleep(0.1)

    paper.scroll(-1.5)
    paper.waitScroll()

    pen.up()

def test2():
    import time
    paper = Paper()
    pen = Pen()
    pen.down()

    pen.move(1.5)
    pen.waitMove()
    time.sleep(0.1)

    paper.scroll(1.5)
    pen.move(-1.5)
    paper.waitScroll()
    pen.waitMove()
    time.sleep(0.1)

    pen.move(1.5)
    pen.waitMove()
    time.sleep(0.1)

    paper.scroll(-1.5)
    pen.move(-1.5)
    paper.waitScroll()
    pen.waitMove()

    pen.up()


if __name__ == '__main__':
    test()

