from Button import*
import random
import time
import math

def main():
    win = GraphWin("Graph Example", 800, 700)
    c = Circle(Point(300, 400), 60)
    center = c.getCenter()
    x2 = center.getX()
    y2 = center.getY()
    print(x2)
    print(y2)
    c.draw(win)
    while True:
        m = win.getMouse()
        x1 = m.getX()
        y1 = m.getY()
        d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if d <= 60:
            print("The point is within the circle")
        else:
            print("The point is not within the circle")
                    
        print("The distance from center to the point: " + str(d))
if __name__ == "__main__":
    main()
