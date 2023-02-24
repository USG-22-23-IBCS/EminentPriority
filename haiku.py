import random

def main():

    file1 = open("oneSyllable.txt")
    content1 = file1.read()
    oneWord = content1.split()
        
    file2 = open("twoSyllables.txt")
    content2 = file2.read()
    twoWord = content2.split()

    file3 = open("threeSyllables.txt")
    content3 = file3.read()
    threeWord = content3.split()

    file4 = open("fourSyllables.txt")
    content4 = file4.read()
    fourWord = content4.split()

    '''line1 = (random.choice(fourWord)) + " " + random.choice(oneWord)
    line2 = (random.choice(twoWord)) + " " + (random.choice(twoWord)) + " " + (random.choice(threeWord))
    line3 = (random.choice(twoWord)) + " " + (random.choice(threeWord))'''
    
    L = [oneWord, twoWord, threeWord, fourWord]
    x = random.randint(1, 4)
    pick = L[x-1]
    word = random.choice(pick)

    
   
    print(word)

if __name__ == "__main__":
    main()
