import turtle

class Artist:

    def __init__(self, t):
        self.t = t
        
    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.setheading(0)
        self.t.pendown()
        
    def triangle(self, size = 100):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)
            
    def square (self, size = 100):
        for i in range(4):
            self.t.right(90)
            self.t.forward(size)
            
    def circle (self):
        for i in range(360):
            self.t.right(1)
            self.t.forward(1)
            
    def star (self, size = 100):
        for i in range(5):
            self.t.right(144)
            self.t.forward (size)
            
    def polygon (self, size = 45):
        n = int (input ("Number of sides for the polygon\n"))
        for i in range(int(n)):
            self.t.right(360/n)
            self.t.forward (size)

    def star2 (self, size = 45):
        for i in range(5):
            self.t.right(144)
            self.t.forward(size)
            self.t.left(72)
            self.t.forward(size)
            
    def heart (self):
        self.t.left(45)
        self.t.forward(26)
        for i in range(3):
            self.t.right(45)
            self.t.forward(45)
        self.t.right(45)
        for i in range(3):
            self.t.forward(45)
        self.t.right (90)
        for i in range(3):
            self.t.forward(45)
        for i in range(3):
            self.t.right(45)
            self.t.forward(45)
        self.t.right(45)
        self.t.forward(26)
        
    def sun (self):
        for i in range(360):
            self.t.right(1)
            self.t.forward(1)
        for i in range(10):
            for i in range(36):
                self.t.right(1)
                self.t.forward(1)
            self.t.left(90)
            self.t.forward(50)
            self.t.backward(50)
            self.t.right(90)

def main():

    canvas = turtle.Screen()
    canvas.bgcolor("dark sea green")
    canvas.title("Turtle Example")
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(100)
    art = Artist(t)
    
    art.move(-175,250)
    art.triangle()
    
    art.move(-5,250) 
    art.square()
    
    art.move(175,250)
    art.circle()
    
    art.move(-75, 60)
    art.star()
    
    art.move(75,30)
    art.polygon()
    
    art.move (-150,-50)
    art.heart()
    
    art.move (150, -150)
    art.sun()
    
    art.move (-200,-250)
    art.star2()
    
    
    


if __name__ == "__main__":
    main()
