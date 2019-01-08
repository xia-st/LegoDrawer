from drawer import Pen, Paper

def testPen():
    pen = Pen()
    pen.moveInit()
    pen.adjustUpDown(0)
    pen.up()
    pen.waitUpDown()
    pen.down()
    pen.waitUpDown()
    pen.move(5)
    pen.move(-5)
    pen.move(10)
    pen.moveToLeft()

def testPaper():
    paper = Paper()
    paper.scrollInit()
    paper.scroll(20)
    paper.scroll(-20)
    paper.scroll(20)
