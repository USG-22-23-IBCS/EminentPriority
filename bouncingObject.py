from graphics import *
from Button import *
#from time import *

def main():

    win = GraphWin("Bouncing Object", 800, 700)
    
    Object = Circle(Point(400, 50), 20)
    Object.draw(win)
    
    p = Object.getCenter()
    y = p.getY()
    
    #B = Button(win, Point(600, 200), Point (700, 300), "red", "Click me!")
    
    while y < 680:
        Object.move(0, 10)
        y = Object.getCenter().getY()
        x = Object.getCenter().getX()
        if y == 680:
            for i in range (15):
                Object.move(5, -10)
                y = Object.getCenter().getY()
                x = Object.getCenter().getX()
                if x == 780:
                    break
        if x == 780:
            break
            '''if y == 680:
                Object.move(5, -5)
                y = Object.getCenter().getY()
                time.sleep(0.25)'''
                    
        if y < 100:
            time.sleep(0.25)
            
        elif y < 200:
            time.sleep(0.15)

        elif y < 300:
            time.sleep(0.1)

        elif y < 400:
            time.sleep(0.05)

        elif y < 500:
            time.sleep(0.025)

        elif y < 600:
            time.sleep(0.01)
#can put the bounce after the while loop to change the speed of the circle to bounce
    
if __name__ == "__main__":
    main()

