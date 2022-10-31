import random

class House:

    def __init__(self):
        self.rating = random.randint(1,10)

    def getRating(self):
        return self.rating

def randPath(m, num):
    #create an empty path
    p = []

    #try to add coordinates to the path
    #if the path were to get stuck or be 'unfinished' in anyway, try again
    #only finish once a fair path is generated
    while (len(p) < num):
        p = []

        #element with specific coordinate
        #m[x][y] 
      
        #keep track of the value of the path
        #choose a random coordinate to start at
        
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        pVal = m[x][y]
        p.append ([x,y])
        

        #add neighbors to the path at a randomly chosen direction
        #keep track of whether we get stuck. If we get stuck, break
        for i in range(num - 1):
            
            neighbors = [[x+1 , y], [x-1, y], [x, y+1], [x, y-1]]
            bad = []
        #looking for bad neighbor, not good
            for n in neighbors:
                if (n[0] > 4) or (n[0] < 0):
                    bad.append(n)
                elif (n[1] > 4) or (n[1] < 0):
                    bad.append(n)
                elif n in p:
                    bad.append(n)

            for b in bad:
                neighbors.remove(b)

            if len(neighbors) == 0:
                break

            nextHouse = random.choice (neighbors)
            p.append(nextHouse)
            x = nextHouse [0]
            y = nextHouse [1]
            pVal = pVal + m[x][y]

            '''stuck = True
            for n in neighbors:
                if (n[0]<5) and (n[0]>-1):
                    if (n[1]<5) and (n[1]>-1):
                        if n not in p:
                            stuck = False
            if stuck:
                break'''
            
            '''while True:
                neighbor = random.choice(neighbors)
                x=neighbor[0]
                y=neighbor[1]
                if (neighbor[0]<5) and (neighbor[0]>-1):
                    if (neighbor[1]<5) and (neighbor[1]>-1):
                        if neighbor not in p:
                            #print("good neighbor")
                            p.append(neighbor)'''
                        
                #choose a random direction and attempt to add the neighbor
                #do not add the neighbor to the path if it is outside of the 5x5
                #or if the neighbor is already in the path
                #break the while loop if it was a successful addition or if stuck
                
    return pVal, p
                        

def greedyPath(m, num):
    
    bestHouses = []
    houses = []
    coords = []

    for i in range (5):
        for j in range(5):
            houses.append(m[i][j])
            coords.append([i,j])

    for i in range(25):
        maxHouse = houses [0]
        for h in houses:
            if h > maxHouse:
                maxHouse = h

        pos = houses.index(maxHouse)
        bestHouses.append(coords.pop(pos))
        houses.pop(pos)
    
    #print(bestHouses)
    
    #sort the houses in terms of best to worst (create a list of the best houses
    # in a sorted order)


    #try to add coordinates to the path
    #if the path were to get stuck or be 'unfinished' in anyway, try again
    #using a new starting position
    #return once a fair path is generated
    #if no fair path found, return list of zeros as coordinates
    for i in range(len(bestHouses)): #or 25 (25 houses in the matrix)
        p = []



        #keep track of the value of the path
        #pick the next best house to start with

        start = bestHouses[i]
        x = start[0]
        y = start[1]

        pVal = m[x][y]

        p.append(start)
        
        #add neighbors to the path after comparing to see which neighbor is best
        for i in range(num - 1):
            
            #check to see if we are stuck. If we get stuck, break

            neighbors = [[x+1 , y], [x-1, y], [x, y+1], [x, y-1]]
            bad = []
        
            for n in neighbors:
                if (n[0] > 4) or (n[0] < 0):
                    bad.append(n)
                elif (n[1] > 4) or (n[1] < 0):
                    bad.append(n)
                elif n in p:
                    bad.append(n)

            for b in bad:
                neighbors.remove(b)

            if len(neighbors) == 0:
                break


            #check all possible neighbors. Choose the best neighbor
            #add it to the path and add to the value

            bestN = neighbors[0]
            broken = False
            for b in bestHouses:
                if broken:
                    break
                for n in neighbors:
                    if n == b:
                        bestN = n
                        broken = True
                        break

            p.append(bestN)
            x = bestN[0]
            y = bestN[1]
            pVal = pVal + m[x][y]

        #if path is complete, return path and path value

        if len(p) == num:
            return pVal, p
            
    return 0, [[0,0]] #or []

            
  
def main():
    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            h = House()
            l.append(h.getRating())

    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i]) 

    num = int(input("How many houses do you want to visit?\n")) 


    ''' Greedy Path Call '''
    greedyPath(m, num)

    #print(p)
    
    #calculate the average rating of a house in the neighborhood
    ''' Random Path Call '''
    total = 0
    for i in range (5):
        for j in range (5):
            total = total + m[i][j]

    average = total / 25
    
    #while the average of value of the house is greater than the
    #average of the path randomly chosen, try getting another random
    #path. stop, once it is better, and print it.
  
    pVal, p = greedyPath(m, num)

    while (average > pVal/num):
        pVal, p = randPath(m, num)
        
    print(p)

    print("The average value in the path is: " + str(pVal/num))
    print("The average value in the neighbohood is: " + str(average))
    
if __name__ == "__main__":
    main()
