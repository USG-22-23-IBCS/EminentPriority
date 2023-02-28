import random

def genLine(syl, val, includeC):
    #empty string for generating the line
    line = ""
    while True:
        #1 to 4 numbers are the files with 1 to 4 syllables
        v = random.randint(1,4)
        if val - v >= 0:
            #v is the random number from 1 to 4, implementing the list with one to four syllables
            #splitting the list of syllable words so er could
            #actually access the words
            myList = syl.get(v).split()
            word = random.choice(myList)
            while includeC not in word:
                 word = random.choice(myList)
            else:
                word = word
            line = line + word + " "
            #recording the number of syllables we are taking in to the line to then
            #substract that value from the overall value in the line we should have
            val = val - v
        if val == 0:
            break
    
    return line

def main():
    f1 = open("oneSyllable.txt")
    f2 = open("twoSyllables.txt")
    f3 = open("threeSyllables.txt")
    f4 = open("fourSyllables.txt")
    readOne = f1.read()
    readTwo = f2.read()
    readThree = f3.read()
    readFour = f4.read()
    syl = {1 : readOne,
           2 : readTwo,
           3 : readThree,
           4 : readFour}
    number = input("How many Haikus do you want to generate?\n")
    remove = input("What character(s) you want to be in your word?\n")
    for i in range(int(number)):
        print(genLine(syl, 5, remove))
        print(genLine(syl, 7, remove))
        print(genLine(syl, 5, remove))
        #if the user says 6, it will go from 0 to 5, but it shouldn't print anything
        #after the last Haiku, so we need to say (number-1)
        if i < (int(number)-1):
            print("-----")
        else:
            break
            

if __name__ == "__main__":
    main()
