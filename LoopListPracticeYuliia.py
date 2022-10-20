def TwoConsecute7(l):
#len(l)-1 becase the last item in the list doesn't have consecutive number
    for i in range (len(l)-1):
        if l[i] == 7 and l[i+1] == 7:
            return True
    return False
                     
    '''for elem in l:
            if elem == 7:
                if (elem + 1) == 7:
                    print("True")
                else:
                   break
            else:
                print("False")
incorrect code because looks for values of items of the list, not the indexes'''
# first five prime numbers: 2, 3, 5, 7, 11           
def SumOfInt(l):
    total = 0
    for elem in l:
        if elem == 2 or elem == 3 or elem == 5 or elem == 7 or elem == 11:
            break
        #else:
        total = total + elem
    return total

def Exclude23(l):
    total = 0
    found2 = False
    for elem in l:
        if elem == 2:
            found2 = True

        if found2 == False:
            total = total + elem
            
        if found2 == True:
            if elem == 3:
                found2 = False
                
#creating the boolean value would be the best option for this kind of question
            '''if elem == 3:
                break
        total = total + elem     
        if elem == 2:
        repeat until (elem == 3):
            total = total + 0'''   
    return total 
            
            
def main():
    
    print(TwoConsecute7([1, 2, 4, 6, 7, 7]))
    print (SumOfInt([1, 20, 12, 8, 5, 8, 10]))
    print (Exclude23([1, 5, 6, 2, 99, 56, 3]))

if __name__ == "__main__":
    main()
