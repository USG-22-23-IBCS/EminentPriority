from graphics import *
from Button import *
#from time import *

def main():

    win = GraphWin("Gravity and Object", 800, 700)
    
    Object = Circle(Point(400, 50), 20)
    Object.draw(win)
    
    p = Object.getCenter()
    y = p.getY()

    #B = Button(win, Point(600, 200), Point (700, 300), "red", "Click me!")
    
    while y < 680:
        
        Object.move(0, 10)
        y = Object.getCenter().getY()
        if y < 100:
            time.sleep(0.5)
        elif y < 200:
            time.sleep(0.25)

        elif y < 300:
            time.sleep(0.10)

        elif y < 400:
            time.sleep(0.05)

        elif y < 500:
            time.sleep(0.025)

        elif y < 600:
            time.sleep(0.01)
        
    
if __name__ == "__main__":
    main()
