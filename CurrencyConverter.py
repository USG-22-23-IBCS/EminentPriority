
class CurrencyConverter:

    #constructor method, necessary for ANY class
    def __init__(self):
        self.countries = ["Australia", "France", "Japan", "Republic of Korea", "Spain", "The Netherlands", "The United Kingdom", "The United States of America", "Ukraine"]

        self.currency = {1: "Australian Dollar",
                         2: "British Pound",
                         3: "Euro",
                         4: "Japanese Yen",
                         5: "South Korean Won",
                         6: "Ukrainian Hryvnia",
                         7: "US Dollar"}
    
        self.corresponding = {"Australia" : 1,
                              "France": 3,
                              "Japan": 4,
                              "Republic of Korea": 5,
                              "Spain": 3,
                              "The Netherlands": 3,
                              "The United Kingdom": 2,
                              "The United States of America": 7,
                              "Ukraine": 6}
        
        self.rates = {"Australian Dollar": 1.439827,
                      "British Pound": 0.82519,
                      "Euro": 0.931584,
                      "Japanese Yen": 131.587436,
                      "South Korean Won": 1264.906459,
                      "Ukrainian Hryvnia": 36.720199,
                      "US Dollar": 1}


    def getCountries(self):
        return self.countries

    def getCorrespondingCurrency(self, country):
        corresponding = self.corresponding.get(country)
        currency = self.currency.get(corresponding)

        return currency
    
    def getRates(self, currency):
        rates = self.rates.get(currency)
        return rates
    
    def getCalcRates(self, country1, country2, amount):

        conversion = country2 / country1
        final = amount * conversion

        return country1, country2, final
        
        
def main():
    
    C = CurrencyConverter()
    while True:
        print("Hello! Countries available for exchange: \n")
        print(C.getCountries())
        countryinput = input("Please, enter the name of the country from the list that you want to convert money from: \n")
        countryoutput = input("Please, enter the name of the country from the list that you want to convert money into: \n")
        print(C.getCorrespondingCurrency(countryinput) +
              " to " + C.getCorrespondingCurrency(countryoutput))
        print("Ratio: " + str(C.getRates(C.getCorrespondingCurrency(countryinput))) +
                                     " to " + str(C.getRates(C.getCorrespondingCurrency(countryoutput))))
        money = int(input("How much of your initial currency do you want to convert: "))
        print(C.getCalcRates(C.getRates(C.getCorrespondingCurrency(countryinput)), C.getRates(C.getCorrespondingCurrency(countryoutput)), money))
        
        yesOrno = input ("Would you like to continue converting the money? \nYes or No\n")
        if yesOrno == "No" or "no":
              break
    #print(C.getCalcRates(C.getRates(C.getCorrespondingCurrency("Ukraine")), C.getRates(C.getCorrespondingCurrency("Spain")), 100))

if __name__ == "__main__":
    main()
    
