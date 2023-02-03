import math
import random

def problem1(x, y, z):

    mean = (x + y + z)/3

    L = [x, y, z]
    L.sort()
    median = L[1]

    return mean, median

def problem2(num):

    print(num)
    
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return True
    else:
        return False

def problem3(L):

    print(L)

    max = L[0]
    min = L[0]

    for n in L:
        if n > max:
            max = n
        if n < min:
            min = n
    range = max-min
    
    return max, min, range

def problem4(point):

    print(point)

    dist = math.sqrt(int(point[0])**2 + int(point[1])**2)
    angle = math.asin(int(point[1])/dist)
    angleD = (angle/math.pi)*180
    
    L = [dist, angle, angleD]
    
    return L

def problem5(name):

    print(name)
    L1 = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "a", "e", "i", "o", "u", "l", "n", "s", "t", "r"]
    L2 = ["D", "G", "d", "g"]
    L3 = ["B", "C", "M", "P", "b", "c", "m", "p"]
    L4 = ["F", "H", "V", "W", "Y", "f", "h", "v", "w", "y"]
    L5 = ["K", "k"]
    L8 = ["J", "X", "j", "x"]
    L10 = ["Q", "Z", "q", "z"]

    score = 0
    
    for letter in name:
        for elem1 in L1:
            if letter == elem1:
                score = score + 1
        for elem2 in L2:
            if letter == elem2:
                score = score + 2
        for elem3 in L3:
            if letter == elem3:
                score = score + 3
        for elem4 in L4:
            if letter == elem4:
                score = score + 4
        for elem5 in L5:
            if letter == elem5:
                score = score + 5
        for elem8 in L8:
            if letter == elem8:
                score = score + 8
        for elem10 in L10:
            if letter == elem10:
                score = score + 10

    return score
        




    
def main():

    #problem1
    mean, median = problem1(44, 123, -5)
    print(mean)
    print(median)

    #problem2
    num = random.randint(1, 100)
    print(problem2(num))   

    #problem3
    L = []
    for n in range(10):
        n = random.randint(1, 50)
        L.append(n)

    print(problem3(L))

    #problem4
    x = input("Please, enter x: ")
    y = input ("Please, enter y: ")
    point = [x, y]

    print(problem4(point))

    #problem5
    name = input ("Please, enter any name: ")
    print("Your score is: " + str(problem5(name)))
    
    #making list of 1 point, 2 point lists and letters corresponding to them
  
    
if __name__ == "__main__":
    main()
