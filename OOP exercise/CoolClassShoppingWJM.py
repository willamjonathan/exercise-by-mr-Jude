#the class definition module
class SL_WJM:
#it has 4 atribubtes 
    def __init__(self,food,pounds):
        self.food = food
        self.pounds = pounds
        self.price = 0
        self.total = 0
 #setter function        
    def __PriceListWJM(self):
        if self.food.lower()=="dry cured iberian ham":
            self.set_price(177.8)
        elif self.food.lower()=="wagyu steaks":
            self.set_price(450)
        elif self.food.lower()=="matsutake mushrooms":
            self.set_price(272)
        elif self.food.lower()=="kopi luwak coffee":
            self.set_price(306)
        elif self.food.lower()=="moose cheese":
            self.set_price(487.2)
        elif self.food.lower()=="white truffles":
            self.set_price(3600)
        elif self.food.lower()=="blue fin tuna":
            self.set_price(3603)
        elif self.food.lower()=="le bonnotte potatoes":
            self.set_price(270.81)
        else:
            self.set_price(0)
    #getter function to call price        
    def get_priceWJM(self):
        return self.price
    
    def set_price(self,number):
        self.price = number
       
    def totalWJM(self):
        self.__PriceListWJM()
        self.total = self.price*self.pounds
        return self.total
