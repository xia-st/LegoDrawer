from ev3dev2.motor import MediumMotor, LargeMotor, SpeedPercent
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C
class Pen:
    def __init__(self):
        self.__udm = MediumMotor(OUTPUT_B) # up and down motor
        self.__lrm = LargeMotor(OUTPUT_A)
        self.isUp = False
        self.loading = False
        self.speed = 1
        self.ll = 0
        self.lr = 5
        pass

    def up(self):
        # 抬起笔
        print('up', self.isUp)
        if self.loading or self.isUp:
            return

        self.__udm.on_for_rotations(SpeedPercent(75), 1)
        self.isUp = True

    def down(self):
        # 放下笔
        print('down', self.isUp)
        if self.loading or not self.isUp:
            return

        self.__udm.on_for_rotations(SpeedPercent(75), -1)
        self.isUp = False
        pass

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

    def move(self, d):
        # 笔移动距离d，正数向右，负数向左
        self.__lrm.on_for_rotations(SpeedPercent(75), d, block=False)

    def moveToLeft(self):
        # 移动笔的位置到最左边，用于结束绘制后移动到最左边
        pass

    def waitMove(self):
        # 等待笔左移右移结束
        self.__lrm.wait_until_not_moving()

class Paper:
    def __init__(self):
        self.speed = 1
        pass

    def scroll(self, d, speed):
        # 滚动距离d，正数向前，复数向后
        pass

    def scrollOut(self):
        # 把纸张送出去
        pass

    def loadPaper(self):
        # 滚动到读取到纸张的位置，如果读到纸张返回True，不然返回False
        pass

    def waitScroll(self, d):
        # 等待滚动完成
        pass

if __name__ == '__main__':
    pen = Pen()
    pen.move(-0.2)
    pen.waitMove()
