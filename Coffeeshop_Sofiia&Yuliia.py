class Lander:

    def __init__(self):
        self.Pumkinspicelattte = 5.50
        self.London_fog = 4.50
        self.Cold_Brew = 6.50
        self.Iced_Matcha_Latte = 6
        self.Considine_special_drink = 6.25
        
        self.menu = "\n 1.Pumpkin spice latte\n 2.London fog\n 3.Cold brew\n 4.Iced Matcha latte\n 5.Considine special drink\n"
        self.info = "Choose an option:\n 1.Talk to administrator\n 2.Write a complaint\n"
        self.info1 = "Administrator isn't available right now, please come back after 6pm"
        self.info2 = "Please write a complaint using this email: landercoffee@gmail.com"

    def getMenu(self):
        return self.menu

    def getPumkinspicelattte(self):
        return self.Pumkinspicelattte

    def getLondon_fog(self):
        return self.London_fog

    def getCold_Brew(self):
        return self.Cold_Brew

    def getIced_Matcha_Latte(self):
        return self.Iced_Matcha_Latte

    def getConsidine_special_drink(self):
        return self.Considine_special_drink

    def getInfo(self):
        return self.info

    def getInfo1(self):
        return self.info1

    def getInfo2(self):
        return self.info2


def main():

    Cof = Lander()
    
    input("Hello! Welcome to Lander!")
    name = input("What is your name?")
    answer = input("How can I help you,"+ name + "?" + "\nPlease pick an option:\n 1. Order a coffee\n 2. Ask a question\n")
    if answer == '1':
        answer1 = input("Which drink would you like to order?" + " (Please type the name of the drink)" + Cof.getMenu())
        if answer1 == 'Pumpkin spice latte':
            print("Thank you for coming," + name + "!" + "\nYour order:"+ answer1 + ", " + str(Cof.getPumkinspicelattte()) + " " + "dollars")
        if answer1 == 'London fog':
            print("Thank you for coming," + name + "!" + "\nYour order:"+ answer1 + ", " + str(Cof.getLondon_fog()) + " " + "dollars")
        if answer1 == 'Cold brew':
            print("Thank you for coming," + name + "!" + "\nYour order:"+ answer1 + ", " + str(Cof.getCold_Brew()) + " " + "dollars")
        if answer1 == 'Iced Matcha latte':
            print("Thank you for coming," + name + "!" + "\nYour order:"+ answer1 + ", " + str(Cof.getIced_Matcha_Latte()) + " " + "dollars")
        if answer1 == 'Considine special drink':
            print("Thank you for coming," + name + "!" "\nYour order:"+ answer1 + ", " + str(Cof.getConsidine_special_drink()) + " " + "dollars")
    else:
        answer2 = input(Cof.getInfo())

        if answer2 == '1' or answer2 == 'Talk to administrator':
            print(Cof.getInfo1())
        else:
             print(Cof.getInfo2())          
    print ("Have a good one!")
    
if __name__ == "__main__":
    main()
