class GroceryStore:
    def getGroceryName(self):
        return self.Grname

    def getManagerName(self):
        return self.Manname
    
    def __init__(self):
        

        self.groceries = {"potatoes" : 0.75,
                            "tomatoes" : 1.25,
                            "cucumbers" : 1.50,
                            "mushrooms" : 3.50,
                            "carrots" : 0.90,
                            "cabbage" : 0.90,
                            "apples" : 0.50,
                            "bananas" : 1.90,
                            "lemons" : 1.50,
                            "milk" : 2.00,
                            "bread" : 3.50,
                            "eggs" : 0.30,
                            "butter" : 1.25,
                            "cereal" : 3.75,
                            "fish" : 9.50,
                            "water" : 1.75,
                            "yogurt" : 2.25,
                            "orange juice" : 1.50,
                            "apple juice" : 1.50,
                            "lemonade" : 1.75}
        
        self.sold = ["cucumbers", "carrots", "cabbage", "bananas", "bread", "cereal", "eggs", "apples", "yogurt", "apple juice"]

        self.Grname = "Yuliia's Grocery Store"

        self.Manname = "Manager Kiko"

        
    def getAvailableGr(self):
        listofproducts = list(self.groceries.keys())
        productsavailable = []
        for g in listofproducts:
            if g not in self.sold:
                productsavailable.append(g)
        return productsavailable
    
    def getBuying(self):
        buylist = []
        answer2_1 = input("What you would like to buy? Enter 1 product: \n" + str(self.getAvailableGr()))
        total = 0
        for g in self.getAvailableGr():
                    if answer2_1 == g:
                        buylist.append(answer2_1)
                        #buyList = x.split()
                        for b in buylist:
                            val = self.groceries.get(b)
                            total = total + val
                        print("This is your current cart: " + str(buylist))
                        print("This is your current total: " + str(total))
        while True:
            add = input("If you would like to add another product to your cart, type 'yes': \nIf you want to finish buying, type 'no': \n")
            if add == 'yes':
                new = input("What you would like to buy?\n")
                for g1 in self.getAvailableGr():
                    if new == g1:
                        buylist.append(new)
                        for b in buylist:
                            val = self.groceries.get(b)
                            total = total + val
                        print("This is your current cart: " + str(buylist))
                        print("This is your current total: " + str(total))
                    
            if add == "no":
                    False
                    break
        '''total = 0
        for b in buylist:
            price = self.groceries.get(b)
            total = total + price'''
        print("This is your final status of the cart: " + str(buylist))
        print("This is your total sum: " + str(total))
        return buylist, total
            
def main():

    store = GroceryStore()
    
    print("Hello! Welcome to " + str(store.getGroceryName()))
    answer = input("How can I help you?" + "\nPlease pick an option:\n 1. Look on the available options\n 2. Purchase the products\n 3. Talk to the store manager\n")
    if answer == '1':
        print("Here is the list of all the groceries available in the store: " + str(store.getAvailableGr()))
        nextSteps = input("What would you like to do next?\n 1. Purchase the groceries\n 2. Talk to the manager\n")

        if nextSteps == "1":
            store.getBuying()
            
            if nextSteps == "2":
                manager = input("What is your question or concern? You can leave your message here, and our manager, " + str(store.getManagerName()) + "will reach out to you with the answer:)\n")
                print("Thank you for leaving your message: " + str (manager))
                
    if answer == '2':
       store.getBuying()
       
    if answer == "3":
        manager = input("What is your question or concern? You can leave your message here, and our manager will reach out to you with the answer:)\n")
        print("Thank you for leaving your message: " + str (manager) + ". " + str(store.getManagerName()) + " will answer you shortly!")

    print("Thank you for visiting Yuliia's grocery store! Have a good one!")    
            
    
if __name__ == "__main__":
    main()
