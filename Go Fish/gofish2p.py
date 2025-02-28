import random
import os

def get_player_ind(turn):
  return (turn + 1) % 2

def create_deck():
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
  return cards

def draw_a_card(hand):
  global deck, discards
  if deck == []:
    random.shuffle(discards)
    deck.append(discards)
  hand.append(deck.pop(0))
  return hand

def deal():
  global hands
  global deck
  for i in range(7):
    hands[0] = draw_a_card(hands[0])
    hands[1] = draw_a_card(hands[1])

def pair(hand, val):
  global discards
  card_copy = []
  new_hand = hand.copy()
  for card in hand:
    if val in card:
      card_copy.append(card)
      if len(card_copy) == 2:
        for c in card_copy:
          new_hand.remove(c)
          discards.append(c)
        break
  return new_hand


def start_turn(turn, hands):
  curr_player = get_player_ind(turn)
  opp_player = get_player_ind(turn + 1)
  print(f"Player {curr_player+1}'s turn")
  print(f"Player {opp_player+1} has {len(hands[opp_player])} cards left.")
  display(hands[curr_player])

def start_game(hands):
  start_turn(1,hands)
  hands[0] = ask_for_pair(hands[0])
  input("Press enter to continue.")
  os.system("clear")
  start_turn(2,hands)
  hands[1] = ask_for_pair(hands[1])
  input("Press enter to continue.")
  os.system("clear")

def display(hand):
  for card in hand:
    print(card,end = " ")
  print("\n")

def ask_for_pair(hand):
  global points, turn
  val = "0"
  new_hand = hand.copy()
  while val != "-":
    val = input("What pair do you have (- if none)? ")
    if val != "-" and val != "":
      new_hand = pair(new_hand,val)
      if new_hand != hand:
        print("That's a pair!")
        display(new_hand)
        points[get_player_ind(turn)] +=1
      else:
        print("That's not a pair")
      hand = new_hand.copy()
  return(new_hand)


def ask_opponent(guess, turn, hands):
  curr_player = get_player_ind(turn)
  opp_player = get_player_ind(turn + 1)
  has_card = False
  while not has_card:
    for card in hands[curr_player]:
      if guess in card:
        has_card = True
    if has_card:
      for card in hands[opp_player]:
        if guess in card:
          print(f'Player {opp_player+1} has a {guess}')
          hands[curr_player].append(card)
          hands[opp_player].remove(card)
          display(hands[curr_player])
          hands[curr_player] = ask_for_pair(hands[curr_player])
          return None
      print(f"Player {opp_player+1} doesn't have a {guess if guess != 1 else 10}")
      print("Go fish!")
      hands[curr_player] = draw_a_card(hands[curr_player])
      display(hands[curr_player])
      hands[curr_player] = ask_for_pair(hands[curr_player])
      return None
    else:
      print(f"You don't have a {guess if guess != 1 else 10} - ask for something else.")
      guess = input("Ask for a card: ")



deck = create_deck()
turn = 1
points = [0,0]
hands = [[],[]]
points = [0,0]
discards = []
deal()
start_game(hands)

while hands[0] != [] and hands[1] != []:
  start_turn(turn, hands)
  guess = input("Ask for a card: ")
  ask_opponent(guess, turn, hands)
  turn += 1
  input("Press enter to continue.")
  os.system('clear')

print("Someone's out of cards!")
print(f'Player 1 has {points[0]} pairs')
print(f'Player 2 has {points[1]} pairs')
if points[0] > points[1]:
  print('Player 1 wins')
elif points[1] > points[0]:
  print("Player 2 wins")
else:
  print("It's a tie")