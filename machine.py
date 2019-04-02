from enum import Enum

class Coin(Enum):
    NICKEL = 5
    DIME = 10
    QUARTER = 25
    DOLLAR = 100

class Rack:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = 0

class Machine:
    def __init__(self, racks):
        self.amount = 0
        self.money = {Coin.NICKEL:10,Coin.QUARTER:10,Coin.DIME:10,Coin.DOLLAR:10}
        self.racks = {}
        for rack in racks:
            self.racks[rack.code]= rack
        self.coins = {}
        for coin in Coin:
            self.coins[coin] = 0

    def refill(self, code, quantity):
        self.racks[code].quantity += quantity

    def insertCoin(self, coin):
        self.coins[coin] += 1
        self.amount += coin.value

    def pressButton(self, code):
        rack = self.racks[code]
        if rack.price <= self.amount:
            rack.quantity -= 1
            self.amount -= rack.price

    def moneyBack(self):
        moneyBack = {}
        if self.amount > 0:
            if self.amount // 100 > 0:
                self.money[Coin.DOLLAR] -= self.amount // 100
                moneyBack[Coin.DOLLAR.value] = self.amount // 100
                self.amount -= Coin.DOLLAR.value * (self.amount // 100)
            elif self.amount // 25 > 0:
                self.money[Coin.QUARTER] -= self.amount // 25
                moneyBack[Coin.QUARTER.value] = self.amount // 25
                self.amount -= Coin.QUARTER.value * (self.amount // 25)
            elif self.amount // 10 > 0:
                self.money[Coin.DIME] -= self.amount // 10
                moneyBack[Coin.DIME.value] = self.amount // 10
                self.amount -= Coin.DIME.value * (self.amount // 10)
            elif self.amount // 5 > 0:
                self.money[Coin.NICKEL] -= self.amount // 5
                moneyBack[Coin.NICKEL.value] = self.amount // 5
                self.amount -= Coin.NICKEL.value * (self.amount // 5)
            else:
                f"No more Money, You lose : {self.amount}, Sorry !!"
        return f"Money Back : {moneyBack.items()}"
       

