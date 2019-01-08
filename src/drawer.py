class Pen:
    def __init__(self):
        self.isUp = False
        self.speed = 1
        pass

    def up(self):
        # 抬起笔
        if self.isUp:
            return

        self.isUp = True
        pass

    def down(self):
        # 放下笔
        if not self.isUp:
            return

        self.isUp = False
        pass

    def adjustUpDown(self, angle):
        # 调整放下笔的角度，angle正数为放下，负数为抬起
        pass

    def waitUpDown(self):
        # 等待抬起放下操作结束
        pass

    def move(self, d, speed):
        # 笔移动距离d，正数向右，负数向左
        pass

    def moveToLeft(self):
        # 移动笔的位置到最左边，用于结束绘制后移动到最左边
        pass

    def waitMove(self):
        # 等待笔左移右移结束
        pass

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
