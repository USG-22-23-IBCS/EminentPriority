import math
# IBCS "Find my error" homework!

# Each method below currently does not run properly. Either it throws an error
# or it prints out/returns the wrong thing. Fix each method one by one.
# Comment out the method call in the main to run it and test it.
# You may need to import a library to get something to work!


#formal greeting. get the user's name and formally say hello to them
'''def greet():
    #deleted another definition of name = {}
    name = input("What's your name?\n")
    response = "Hello, {}. It is nice to meet you"
    #syntax of the next statement also changed
    print(response.format(name))'''


#determine the area of a circle given its radius
'''def circleArea(r):
    #need to import math for pi
    if r <= 0:
        return "Invalid circle dimensions"
    else:
        return math.pi*r**2'''

#given a dictionary of students and their grades, print out which students
#need to study more (grade below 73)
'''def studyMore(D):
    for student in D:
        if D.get(student) < 73:
            print(student + " needs to study more.")'''
    
#given a dictionary of students and their grades, calculate
#the mean and median of the grades. print them out
def meanMedian(D):
    listOfGrades = list(D.values())
    listOfGrades.sort()
    total = 0
    for g in listOfGrades:
        total += g
    mean = total/len(listOfGrades)
    index = len(listOfGrades)/2
    median = listOfGrades[round(index) - 1]

    print("Average grade was: " + str(mean))
    print("Median grade was: " + str(median))
    
def main():
    D = {"Jake" : 90,
         "Betty" : 20,
         "Aristotle" : 100,
         "Genghis" : 25,
         "Shirley" : 88,
         "Salt" : 6,
         "Charlie" : 91,
         "Seacrest" : 72,
         "Ryan": 73}
    
    #greet()
    #print(circleArea())
    #studyMore(D)
    meanMedian(D)


if __name__ == "__main__":
    main()
