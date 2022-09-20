class horse:
    
    def __init__ (self, breed, gender, fcolor, ecolor, purpose):
        self.breed = breed
        self.gender = gender
        self.fur_color = fcolor
        self.eye_color = ecolor
        self.purpose = purpose
    
    def getBreed(self):
        return self.breed
    
    def getGender(self):
        return self.gender
    
    def setFcolor(self, fcolor):
        self.fur_color = fcolor
    
    def getFcolor(self):
        return self.fur_color
    
    def setEcolor(self, ecolor):
        self.eye_color = ecolor
        
    def getEcolor(self):
        return self.eye_color
    
    def setPurpose(self, purpose):
        self.purpose = purpose

    def getPurpose(self):
        return self.purpose
def main ():
    animal1 = horse ("Clydestale", "male", "white and brown", "black", "because these horses are very strong")
    animal2 = horse ("Appaloosa", "female", "caramel with white spots", "dark brown", "these horses are good in speed-running, will be very fast during the race") 
    print ("!first animal!")
    print(animal1.getBreed())
    print(animal1.getGender())
    print(animal1.getFcolor())
    print(animal1.getEcolor())
    print(animal1.getPurpose())
    animal1.setPurpose("they are useful for society in different ways, for example, farming")
    print(animal1.getPurpose())

    print ("!second animal!")
    print (animal2.getBreed())
    print(animal2.getGender())
    print (animal2.getFcolor())
    animal2.setFcolor("white with black spots")
    print (animal2.getFcolor())
    print (animal2.getEcolor())
    print(animal2.getPurpose())

if __name__ == "__main__":
    main()
