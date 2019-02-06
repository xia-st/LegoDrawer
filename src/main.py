import json

from canvas import Canvas

def rounds(path):
    maxX = 0
    maxY = 0
    minX = 8192
    minY = 8192
    for point in path:
        x, y = point[0]
        maxX = max(maxX, x)
        maxY = max(maxY, y)
        minX = min(minX, x)
        minY = min(minY, y)

    return minX, minY, maxX, maxY

paths = json.load(open('pig.json'))

maxX = 0
maxY = 0
minX = 8192
minY = 8192
for path in paths:
    for point in path:
        x, y = point[0]
        maxX = max(maxX, x)
        maxY = max(maxY, y)
        minX = min(minX, x)
        minY = min(minY, y)

r = 1.5 / (maxX - minX)

curX = 0
curY = 0

for path in paths:
    for point in path:
        point[0][0] = (point[0][0]-minX)*r
        point[0][1] = (point[0][1]-minY)*r

c = Canvas()
for path in paths:
    _minX, _minY, _maxX, _maxY = rounds(path)
    if _maxX - _minX < 0.03 and _maxY - _minY < 0.03:
        continue

    print(path)
    startPoint = path[0]
    startX, startY = startPoint[0]
    startX = round(startX, 2)
    startY = round(startY, 2)
    c.goto(startX, startY)

    c.penDown()
    for point in path[1:]:
        x, y = point[0]
        c.goto(x, y)
    c.goto(startX, startY)
    c.penUp()

c.goto(0, 0)
c.paper.scroll(-3)
c.paper.waitScroll()
