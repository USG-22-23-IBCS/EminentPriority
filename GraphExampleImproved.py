from Button import*
import random
import time

class Node:
    def __init__(self, x, y, win, name):
        self.center = Point(x, y)
        self.C = Circle(self.center, 30)
        self.neighbors = []
        self.name = name
        self.T = Text(self.center, self.name)
        
    def draw(self, win):
        self.C.draw(win)
        self.T.draw(win)
        
    def getName(self):
        return self.name
    
    def undraw(self):
        self.C.undraw()
        self.T.undraw()

    def addNeighbor(self, n):
        self.neighbors.append(n)

    def calcDegree(self):
        return len(self.neighbors)      

    '''def maxDegree(self):
        self.LDegree = []
        for degree in range(numN):
            LDegree.append(Node.calcDegree())

        self.maxDegree = LDegree[0]
        for elem in LDegree:
            if elem > self.maxDegree:
                self.maxDegree = elem
                
        return self.maxDegree

    def minDegree(self):
        return self.minDegree'''
    
    def getCenter(self):
        return self.center

    def getNeighbors(self):
        return self.neighbors

    def color(self, c):
        self.C.setFill(c)

class Graph:

    def __init__(self, n, e, win):
        self.nodes = []
        self.E = []
        Xpositions = []
        Ypositions = []
        names = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        numN = 0
        while True:
            x = random.randint(140, 740)
            y = random.randint(50, 550)
            foundNode = True
            for posX in Xpositions:
                if x - 70 < posX < x + 70:
                    for posY in Ypositions:
                        if y - 70 < posY < y + 70:
                            foundNode = False
            #creating a node itself
            if foundNode:
                Xpositions.append(x)
                Ypositions.append(y)
                name = names[numN]
                N = Node(x, y, win, name)
                self.nodes.append(N)
                numN += 1

            if numN == n:
                break

        edges = 0
        while edges < e:
            n1 = random.choice(self.nodes)
            n2 = random.choice(self.nodes)
            if n1 != n2:
                if n1 not in n2.getNeighbors():
                    p1 = n1.getCenter()
                    p2 = n2.getCenter()
                    L = Line(p1, p2)
                    self.E.append(L)
                    L.draw(win)
                    edges += 1
                    n1.addNeighbor(n2)
                    n2.addNeighbor(n1)

        for node in self.nodes:
            node.draw(win)
            node.color("white")
            #lDegree.append(node.calcDegree)
            #print(str(lDegree))
            print(str(node.calcDegree()) + " : " + node.getName())
            '''self.LDegree.append(node.calcDegree())
            self.DDegree[node.getName()] = node.calcDegree()

        print(DDegree)
        print(LDegree)'''
        print("Max Degree: " + str(self.getmaxDegree()))
        print("Min Degree: " + str(self.getminDegree()))
        
    def LCalc(self):
        DDegree = {}
        LDegree = []
        for node in self.nodes:
            LDegree.append(node.calcDegree())
            #DDegree[getName()] = calcDegree()
        LDegree.sort()

        return LDegree
    
    def getmaxDegree(self):
        LDegree = self.LCalc()
        maxDegree = LDegree[-1]
        return maxDegree

    def getminDegree(self):
        LDegree = self.LCalc()
        minDegree = LDegree[0]
        return minDegree

    '''def getminDegree(self):

        return minDegree'''
        
    def delete(self):
        for e in self.E:
            e.undraw()
        for n in self.nodes:
            n.undraw()

      
        
def main():

    win = GraphWin("Graph Example", 800, 600)
    Q = Button(win, Point(20, 530), Point(100, 590), "tomato", "QUIT!")
    Gen = Button(win, Point(20, 430), Point(100, 490), "cyan", "Generate!")
    G = Graph(1, 0, win)
    while True:
        m = win.getMouse()
        if Q.isClicked(m):
            break
        if Gen.isClicked(m):
            G.delete()
            #Graph made with the number of nodes and number of edges 
            G = Graph(7, 7, win)
    win.close()

if __name__ == "__main__":
    main()
