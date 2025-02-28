import random

cards = []
hand = []
values = ["A","K","Q","J", "10", "9", "8", "7", "6","5","4","3","2"]
for value in values:
  cards.append(value + "♥")
for value in values:
  cards.append(value + "♦")
for value in values:
  cards.append(value + "♣")
for value in values:
  cards.append(value + "♠")

random.shuffle(cards)


hand.append(cards[0])
cards.pop(0)
print(hand)
print(cards)
