from graphics import*
from Button import*

def main():
    
    win = GraphWin("Your Starbucks Drink", 1000, 750)
    win.setBackground("lavenderblush")

    introduction = Text(Point(500, 50), "Hello, Jenny! Welcome to the program Your Starbucks drink!\n Please, press Start if you want to start choosing your drink. Press Quit if you want to close the window.")
    introduction.setSize(15)
    introduction.draw(win)

    #starter buttons
    start = Button(win, Point(20, 10), Point(150, 70), "mediumseagreen", "Start")
    quit = Button(win, Point(860, 670), Point(990, 730), "firebrick", "Quit")

    codes = {1: "Caramel Cold Brew",
             2: "Iced Vanilla Coffee with Milk",
             3: "Iced Brown Sugar Espresso",
             4: "Caffe Latte",
             5: "Iced Cinnammon Latte",
             6: "Earl Grey Tea",
             7: "Iced Matcha Latte"}
    
    drinks = {"Caramel Cold Brew": ["coffee", "caramel", "milk", "cold"],
              "Iced Vanilla Coffee with Milk" : ["coffee", "vanilla", "milk", "cold"],
              "Iced Brown Sugar Espresso" : ["coffee", "brown sugar", "no milk", "cold"],
              "Caffe Latte" : ["coffee", "no add-ons", "milk", "hot"],
              "Iced Cinnammon Latte" : ["coffee", "cinnammon", "milk", "cold"],
              "Earl Grey Tea" : ["tea", "no add-ons", "no milk", "hot"],
              "Iced Matcha Latte" : ["tea", "brown sugar", "milk", "cold"]}
    
    choices = []

    while True:
        m = win.getMouse()
        if start.isClicked(m):

            #Question 1
            Q1 = Text(Point(500, 120), "Question 1")
            Q1.setSize(14)
            Q1.draw(win)
            
            #Question 1 buttons
            Q1A = Button(win, Point(300, 150), Point(400, 200), "slateblue", "Coffee")
            Q1B = Button(win, Point(600, 150), Point(700, 200), "slateblue", "Tea")   

            m = win.getMouse()
            if Q1A.isClicked(m) or Q1B.isClicked(m):

                if Q1A.isClicked(m):
                    choices.append("coffee")
                if Q1B.isClicked(m):
                    choices.append("tea")

                #Question 2
                Q2 = Text(Point(500, 250), "Question 2")
                Q2.setSize(14)
                Q2.draw(win)

                #Question 2 buttons
                Q2A = Button(win, Point(50, 270), Point(150, 320), "slateblue", "No add-ons")
                Q2B = Button(win, Point(250, 270), Point(350, 320), "slateblue", "Brown Sugar")
                Q2C = Button(win, Point(450, 270), Point(550, 320), "slateblue", "Caramel")
                Q2D = Button(win, Point(650, 270), Point(750, 320), "slateblue", "Vanilla Syrup")
                Q2E = Button(win, Point(850, 270), Point(950, 320), "slateblue", "Cinnamon")

                m = win.getMouse()
                if Q2A.isClicked(m) or Q2B.isClicked(m) or Q2C.isClicked(m) or Q2D.isClicked(m) or Q2E.isClicked(m):
                    if Q2A.isClicked(m):
                        choices.append("no add-ons")
                    if Q2B.isClicked(m):
                        choices.append("brown sugar")
                    if Q2C.isClicked(m):
                        choices.append("caramel")
                    if Q2D.isClicked(m):
                        choices.append("vanilla")
                    if Q2E.isClicked(m):
                        choices.append("cinnamon")
                    #Question 3
                    Q3 = Text(Point(500, 370), "Question 3")
                    Q3.setSize(14)
                    Q3.draw(win)

                    #Question 3 buttons
                    Q3A = Button(win, Point(300, 390), Point(400, 440), "slateblue", "No milk")
                    Q3B = Button(win, Point(600, 390), Point(700, 440), "slateblue", "Milk")

                    m = win.getMouse()
                    if Q3A.isClicked(m) or Q3B.isClicked(m):
                        if Q3A.isClicked(m):
                            choices.append("no milk")
                        if Q3B.isClicked(m):
                            choices.append("milk")

                        #Question 4
                        Q4 = Text(Point(500, 490), "Question 4")
                        Q4.setSize(14)
                        Q4.draw(win)

                        #Question 4 buttons
                        Q4A = Button(win, Point(300, 510), Point(400, 560), "slateblue", "Cold")
                        Q4B = Button(win, Point(600, 510), Point(700, 560), "slateblue", "Hot")

                        m = win.getMouse()
                        if Q4A.isClicked(m) or Q4B.isClicked(m):
                            
                            if Q4A.isClicked(m):
                                choices.append("cold")
                            if Q4B.isClicked(m):
                                choices.append("hot")            
                        #print(choices)
                        end = Text(Point(500, 580), "Based on your choices, this is the suggested drink you can try! Enjoy!")
                        end.setSize(15)
                        end.draw(win)

                        your_choices = Text(Point(800, 630), "Your choices:\n" + str(choices))
                        your_choices.setSize(14)
                        your_choices.draw(win)

        #Comparing clicked button values with the values in the dictionary 'drinks'
        result = Text(Point(500, 600), "")

        if choices == drinks.get(codes.get(1)):
            result = Text(Point(500, 600), codes.get(1))
        if choices == drinks.get(codes.get(2)):
            result = Text(Point(500, 600), codes.get(2))
        if choices == drinks.get(codes.get(3)):
            result = Text(Point(500, 600), codes.get(3))
        if choices == drinks.get(codes.get(4)):
            result = Text(Point(500, 600), codes.get(4))
        if choices == drinks.get(codes.get(5)):
            result = Text(Point(500, 600), codes.get(5))
        if choices == drinks.get(codes.get(6)):
            result = Text(Point(500, 600), codes.get(6))
        if choices == drinks.get(codes.get(7)):
            result = Text(Point(500, 600), codes.get(7))

        
        result.setSize(15)
        result.setTextColor("darkviolet")
        result.draw(win)

        if quit.isClicked(m):
            break

    #print(choices)

    win.close()
if __name__ == "__main__":
    main()
