import random

class Card:

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def getName(self):
        return self.name

    def getSuit(self):
        return self.suit

    def getCard(self):
        #card is represented not only by name, but also by suit (why list though?)
        return [self.suit, self.name]

class Deck:

    def __init__(self):
        self.cards = []
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        for s in suits:
            #purpose of name: keeping track of cards in the deck
            for i in range(1, 14):
                if i == 1:
                    name = "Ace"
                elif i == 11:
                    name = "Jack"
                elif i == 12:
                    name = "Queen"
                elif i == 13:
                    name = "King"
                else:
                    name = str(i)

                C = Card(s, name)
                self.cards.append(C)

    def getCards(self):
        return self.cards

    def dealCard(self):
        #method to deal a card
        newCard = random.choice(self.cards)
        #choosing a random card form the deck
        self.cards.remove(newCard)
        #as we give a card to the player or the dealer, it is removed from the deck
        return newCard

def calcHandValue(hand):
    #total is 0 because it's the beginning of the counting
    total = 0
    for h in hand:
        name = h[1]
        #hand holds cards, hand = [card1, card2] = [[card1suit (represents 0), card1name (represents 1)], [card2suit, card2name]]
        if name == "Ace":
            total = total + 11
            if total > 21:
                #we are minusing 10 because +1 would not work - only if we would set it as a intial command
                total = total - 10
            #purpose of name: checking their value
        elif name == "King" or name == "Queen" or name == "Jack" :
            total = total + 10
        else:
            total = total + int(name)
        
    return total
        

def main():

    print("Welcome to Blackjack!\n") 

    D = Deck()

    userHand = [D.dealCard().getCard(), D.dealCard().getCard()]
    dealerHand = [D.dealCard().getCard(), D.dealCard().getCard()]

    print("Dealer hand:")
    print(dealerHand)
    print("")
    print("User hand:")
    print(userHand)
    print("Your hand's value is :" + str(calcHandValue(userHand)))
    print("")

    while True:
        option = input("Type 1: Hit  or 2: Stand\n")
        if option == "1":
            userHand.append(D.dealCard().getCard())
        if calcHandValue(userHand) > 21:
            print(calcHandValue(userHand))
            print("User bust!")
            break
        else:
            break
        
    print("")
    print(userHand)
    print("Your hand's value is :" + str(calcHandValue(userHand)))
    print("")   
    if calcHandValue(userHand) > 21:
            print ("The game is over. Dealer wins!")
    else:
        print("")
        print("Dealer hand:")
        print(dealerHand)
        print("Dealer hand's value is :" + str(calcHandValue(dealerHand)))
        print("")
    
        while True:
            if calcHandValue(dealerHand) < 17:
                print("Dealer hits!\n")
                dealerHand.append(D.dealCard().getCard())
                print("Dealer hand:")
                print(dealerHand)
                print("Dealer hand's value is :" + str(calcHandValue(dealerHand)))
                print("")
            else:
                print("Dealer stands!\n")
            break
            if calcHandValue(dealerHand) > 21:
                print("Dealer bust!")
            break

    


if __name__ == "__main__":
    main()
