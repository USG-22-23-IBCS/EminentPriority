# a method which can take in a list of integers and return
# the difference between the largest and smallest integer
# [2, 5, 3, 1, 9, 7] --> 8
# call the paramater for the list
def bigDiff(l):
    maxNum = l[0] #0
    minNum = l[0] #100000
    for elem in l:
        if elem > maxNum:
            maxNum = elem
        if elem < minNum:
            minNum = elem
    return maxNum - minNum
# a method which can take in a list of integers and return
# the mean of all numbers excluding the maximum and minimum
# [2, 5, 3, 1, 9, 7] --> 4.25
def centeredAvg(l):
    maxNum = l[0] 
    minNum = l[0] 
    for elem in l:
        if elem > maxNum:
            maxNum = elem
        if elem < minNum:
            minNum = elem
    l.remove(maxNum)
    l.remove(minNum)

    total = 0
    for elem in l:
        total = total + elem

    return total / len(l)


def main():

    print (bigDiff([2, 5, 3, 1, 9, 7]))  

    myList = [1, 2, 3, 4, 5, 6]
    
    print (centeredAvg(myList))


if __name__ == "__main__":
    main()
