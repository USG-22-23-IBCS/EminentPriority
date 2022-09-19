class fav_animal:
    
    def __init__ (self, species, fcolor, ecolor, since_when_favorite, why_favorite):
        self.species = species
        self.fur_color = fcolor
        self.eye_color = ecolor
        self.since_when_favorite = since_when_favorite
        self.why_favorite = why_favorite
    
    def getSpecies(self):
        return self.species
    
    def getFcolor(self):
        return self.fur_color
    
    def setEcolor(self, ecolor):
        self.eye_color = ecolor
        
    def getEcolor(self):
        return self.eye_color
    
    def setSinceWhenFavorite (self, since_when_favorite):
        self.since_when_favorite = since_when_favorite
        
    def getSinceWhenFavorite(self):
        return self.since_when_favorite
    
    def setWhyFavorite(self, why_favorite):
        self.why_favorite = why_favorite

    def getWhyFavorite(self):
        return self.why_favorite        




def main():
    animal1 = fav_animal ("horse", "white", "black", "since 2012", "because horses are very smart")
    animal2 = fav_animal ("cat", "orange", "brown", "since I first saw cat in my life", "cats are the cutest creatures in the world")
    print ("!first animal!")
    print(animal1.getSpecies())
    print (animal1.getFcolor())
    print (animal1.getEcolor())
    print (animal1.getSinceWhenFavorite())
    print (animal1.getWhyFavorite())
    animal1.setWhyFavorite("because horses are gracious")
    print (animal1.getWhyFavorite())
    print ("!second animal!")
    print (animal2.getSpecies())
    print (animal2.getFcolor())
    print (animal2.getEcolor())
    animal2.setEcolor("green")
    print (animal2.getEcolor())
    print (animal2.getSinceWhenFavorite())
    animal2.setSinceWhenFavorite("since the time I took the test 'My favorite animal'")
    print (animal2.getSinceWhenFavorite())
    print (animal2.getWhyFavorite())

if __name__ == "__main__":
    main()
