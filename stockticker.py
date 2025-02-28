#todo:
#make it so that if a player loses everything, they are removed from the playerlist and playercount is reduced by one.

import random

stocks = {"gold":float(1),
          "silver":float(1),
          "oil":float(1),
          "bonds":float(1),
          "industrial":float(1),
          "grain":float(1) }


stockdie = ["gold", "silver", "oil", "bonds", "industrial", "grain"]
actiondie = ["up", "up", "down", "down", "dividends","dividends"]
numberdie = [5, 5, 10, 10, 10, 20]
'''

#test dice
stockdie = ["gold", "gold", "gold", "silver", "silver", "silver"]
actiondie = ["down", "down", "down", "down", "down","down"]
numberdie = [5, 5, 10, 10, 10, 20]
'''

print("Welcome to Stock Ticker")
print("")
playercount = int(input("How many players are there? "))
length = int(input("How many rounds would you like to play for? "))

def helpmenu():
    print ("Exchange Instructions:")
    print ("Type buy/sell, then a number, then a stock.")
    print ("Trades must be in groups of 500 stocks.")
    print ('Type "see prices" to see the current stock prices. Type "end" to stop trading for the round.')
    print("")

def gamestate():
    print("Game State:")
    print("Gold:", '{:.2f}'.format(stocks["gold"]), "  Silver:    ", '{:.2f}'.format(stocks["silver"]), "  Oil:  ", '{:.2f}'.format(stocks["oil"]))
    print("Bonds:", '{:.2f}'.format(stocks["bonds"]), "  Industrial:",'{:.2f}'.format(stocks["industrial"]), "  Grain:", '{:.2f}'.format(stocks["grain"]))

class Player:

    def __init__(self):
        self.name = ""
        self.cash = 5000
        self.portfolio = { "gold" : 0,
                  "silver" : 0,
                  "oil" : 0,
                  "bonds" : 0,
                  "industrial" : 0,
                  "grain" : 0 }
    
    def display(self):
        print(self.name + "'s inventory:")
        print("Cash:", int(self.cash))
        print("Gold:", self.portfolio["gold"], "  Silver:", self.portfolio["silver"], "  Oil:", self.portfolio["oil"])
        print("Bonds:", self.portfolio["bonds"], "  Industrial:",self.portfolio["industrial"], "  Grain:", self.portfolio["grain"])

    
    def exchange(self):
        self.display()
        print("")
        trade = ""
        while trade == "":
            trade = input("Enter your trade (or type help): ")
        trade = trade.lower()
        trade = trade.split()
        action = trade[0]
        if len(trade) >= 3:
            number = trade[1]
            stock = trade[2]
        else:
            number = "1000"
        while action != "end":
            try:
                number = int(number)
                if action == "see":
                    print("")
                    gamestate()
                elif action == "help":
                    helpmenu()
                elif (stock not in ["gold","silver","oil","bonds","industrial","grain"]):
                    print("Sorry, I don't understand. Try again.")
                elif number % 500 != 0:
                    print("Must buy/sell a multiple of 500.")
                elif action == "buy":
                    cost = stocks[stock]*number
                    if self.cash >= cost:
                        self.cash -= cost
                        self.portfolio[stock] += number
                        self.display()
                    else:
                        print("Sorry, you can't afford that.")
                elif action == "sell":
                    value = stocks[stock]*number
                    if number <= self.portfolio[stock]:
                        self.cash += value
                        self.portfolio[stock] -= number
                        self.display()
                    else:
                        print("Sorry, you don't have enough to sell.")
                else:
                    print("Sorry, I don't understand. Try again.")
            except:
                print("Sorry, I don't understand. Try again.")
            
            print("")
            trade = ""
            while trade == "":
                trade = input("Enter your trade (or type help): ")
            trade = trade.lower()
            trade = trade.split()
            action = trade[0]
            if len(trade) >= 3:
                number = trade[1]
                stock = trade[2]
            else:
                number = "1000"
        print("You have finished trading, thank you.")
        print("")                

playerlist = []

for i in range(playercount):
    newplayer = Player()
    playerlist.append(newplayer)

for i, currplayer in enumerate(playerlist):
    currplayer.name = input("What is your name, player "+str(i+1)+"? ")
    print("")
    print("OK, "+currplayer.name+'. Time to buy some stocks. Type "buy", a number, then a stock name.')
    print('You may buy or sell multiples of 500 stocks at a time. All stocks currently cost 1.')
    print('Type "end" to stop trading for the turn.')
    print("")
    currplayer.exchange()

def roll(die):
    num = random.randint(0,5)
    return die[num]

def split(stock):
    print("The "+stock+" stock has split!")
    for pl in playerlist:
        if pl.portfolio[stock] != 0:
            pl.portfolio[stock]=pl.portfolio[stock]*2
            print(pl.name, "now has", pl.portfolio[stock], stock)
    stocks[stock]=1
    return()

def bust(stock):
    print("The "+stock+" stock has bust!")
    for pl in playerlist:
        if pl.portfolio[stock] != 0:
            pl.portfolio[stock]=0
            print(pl.name, "has lost all their", stock)
        '''
        #issue: playercount is a local variable - I want to change the global variable.
        if pl.cash == 0 and pl.portfolio == { "gold" : 0,"silver" : 0,"oil" : 0,"bonds" : 0,"industrial" : 0,"grain" : 0 }:
            print(pl.name, "has no assets and has been removed from the game! :(")
            playerlist.remove(pl)
            playercount-=1
            if playercount == 0:
                print("No players remain... Game over!")
                quit()
        '''
            
    stocks[stock]=1
    return()

def divvies(stock, percent):
    for pl in playerlist:
        if pl.portfolio[stock] !=0:
            divvie=pl.portfolio[stock]*percent
            pl.cash += divvie
            print(pl.name, "has earned", int(divvie), "in dividends.")
            print(pl.name, "current cash:", int(pl.cash))
    return()


def turn():
    print("==========")
    for i in [1,2,3]:
        stock = roll(stockdie)
        action = roll(actiondie)
        number = roll(numberdie)/100

        print("Roll "+str(i)+":", stock, action, number*100)
        if action == "up":
            stocks[stock] += number
            if stocks[stock] >= 2:
                split(stock)
        elif action == "down":
            stocks[stock] -= number
            if stocks[stock] <= 0:
                bust(stock)
        elif action == "dividends":
            if stocks[stock]>=1:
                divvies(stock, number)
            else:
                print("Dividends are not paid, as the stock is worth less than 1")

        
    print("")
    gamestate()
    print("")
    print("==========")
    print("")

#gameplay

for r in range(length):
    print("")
    print("Round ", r+1, "-", length-r-1, "rounds remaining.")
    print("")
    for currplayer in playerlist:
        print(currplayer.name + "'s turn:")
        turn()
        if r+1 == length and currplayer == playerlist[playercount-1]:
            print("Last turn, no exchange phase.")
        else:
            print("Exchange Phase:")
            for explayer in playerlist:
                print(explayer.name, "may now exchange.")
                print("Type end to quit trading.")
                explayer.exchange()
                print("")
    print("xxxxxxxxxx")

print("")
print("The game is now over. Final scores:")


#end game scoring
hiscore = 0
winner = ""

for currplayer in playerlist:
    score = currplayer.cash
    for key in currplayer.portfolio:
        if currplayer.portfolio[key] != 0:
            value=currplayer.portfolio[key]*stocks[key]
            print(currplayer.name,"had",currplayer.portfolio[key],"stocks in",key,"worth", int(value))
            score+=value
    print(currplayer.name,"scored", int(score), "points.")
    print("")
    if score > hiscore:
        hiscore = score
        winner = currplayer.name
    elif score == hiscore:
        winner = currplayer.name +" and "+ winner

#fix for multiple winners
print(winner,"is the winner!")
