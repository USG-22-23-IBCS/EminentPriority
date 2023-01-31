from graphics import *
from Button import *

def main():

    win = GraphWin("madlibs", 800, 600)

    N = Entry(Point(300, 100), 15)
    N.draw(win)

    N2 = Entry(Point(300, 150), 15)
    N2.draw(win)

    V = Entry(Point(300, 200), 15)
    V.draw(win)

    A = Entry(Point(300, 250), 15)
    A.draw(win)

    E = Entry(Point(300, 300), 15)
    E.draw(win)

    T = Text(Point(400, 30), "Welcome the Mad Lib Simulation in Python! You can generate your short story here!")
    T.draw(win)

    T1 = Text(Point(400, 45), "See the instructions below. Enjoy!")
    T1.draw(win)

    NT = Text(Point(125, 100), "Enter your first noun in the box to the right:")
    NT.draw(win)

    NT2 = Text(Point(125, 150), "Enter your second noun in the box to the right:")
    NT2.draw(win)

    VT = Text(Point(125, 200), "Enter your verb in the box to the right:")
    VT.draw(win)

    AT = Text(Point(125, 250), "Enter your adjective in the box to the right:")
    AT.draw(win)

    ET = Text(Point(125, 300), "Enter your exclamation in the box to the right:")
    ET.draw(win)
    
    BT = Text(Point(650, 175), "Click the button below if you finished\n"
              "entering the words for the story!")
    BT.draw(win)
    
    B = Button(win, Point(600, 200), Point (700, 300), "red", "Click me!")


    while True:

        m = win.getMouse()

        if B.isClicked(m):
            noun = N.getText()
            noun2 = N2.getText()
            verb = V.getText()
            adj = A.getText()
            excl = E.getText()
            Story = Text(Point(400, 400), "Hi! I suppose you were thinking about " + noun + " today? That's interesting!\n"
                  "I remember you talking about " + noun2 + " too! That information was crucial for better understanding. " + adj + ", right?\n"
                 "Are you going to " + verb + " later? If yes, " + excl + "!")
            Story.draw(win)
            B = Button(win, Point(600, 200), Point (700, 300), "green", "Click me!")
            
if __name__ == "__main__":
    main()
