import random
import os

def get_player_ind(turn):
  return (turn + 1) % 2

def create_deck():
  cards = []
  values = ["A","K","Q","J", "10", "9", "8", "7", "6","5","4","3","2"]
  for value in values:
    cards.append(value + "♥")
  for value in values:
    cards.append(value + "♦")
  for value in values:
    cards.append(value + "♣")
  for value in values:
    cards.append(value + "♠")
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

def pair(hand, val, turn):
  global discards
  card_copy = []
  new_hand = hand.copy()
  for card in hand:
    if val in card:
      card_copy.append(card)
      if len(card_copy) == 2:
        if get_player_ind(turn) == 1:
          print(f'Player 2 made a pair of {val if val != "1" else "10"}s')
        for c in card_copy:
          new_hand.remove(c)
          discards[get_player_ind(turn)].append(c)
        break
  return new_hand
    

def start_turn(turn, hands, points):
  curr_player = get_player_ind(turn)
  opp_player = get_player_ind(turn + 1)
  print(f"Player {curr_player+1}'s turn")
  print(f"Player {opp_player+1} has {len(hands[opp_player])} cards left.")
  print(f'Player 1 has {points[0]} points and Player 2 has {points[1]} points.')
  display(hands[curr_player])

def start_game(hands):
  start_turn(1,hands, points)
  hands[0] = ask_for_pair(hands[0])
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
      new_hand = pair(new_hand,val, turn)
      if new_hand != hand:
        print("That's a pair!")
        display(new_hand)
        points[get_player_ind(turn)] +=1
      else:
        print("That's not a pair")
      hand = new_hand.copy()
  return(new_hand)
    
def has_asked_card(handcurr,handopp, guess):
  for card in handopp:
    if guess in card:
      handcurr.append(card)
      handopp.remove(card)
      return True
  return False

def ask_opponent(guess, turn, hands):
  curr_player = get_player_ind(turn)
  opp_player = get_player_ind(turn + 1)
  has_card = False
  while not has_card:
    for card in hands[curr_player]:
      if guess in card:
        has_card = True
    if has_card:
      give = has_asked_card(hands[curr_player], hands[opp_player], guess)
      if give:
        print(f'Player {opp_player+1} has a {guess}')
        display(hands[curr_player])
        hands[curr_player] = ask_for_pair(hands[curr_player])
      else:
        print(f"Player {opp_player+1} doesn't have a {guess if guess != 1 else 10}")
        print("Go fish!")
        hands[curr_player] = draw_a_card(hands[curr_player])
        display(hands[curr_player])
        hands[curr_player] = ask_for_pair(hands[curr_player])
      return None
    else:
      print(f'You don\'t have a {guess if guess != "1" else "10"} - ask for something else.')
      guess = input("Ask for a card: ")[0]

def ai_pairs(hand):
  global points, turn
  new_hand = hand.copy()
  pairs_found = 0
  for card in hand:
    pre_pair = new_hand.copy()
    new_hand = pair(new_hand, card[0], turn)
    if new_hand != pre_pair:
      pairs_found +=1
  points[1] += pairs_found
  return new_hand

def ai_turn(hands):
  display(hands[0])
  ask = random.choice(hands[1])
  print(f'Player 2 says: "Do you have a {ask[0] if ask[0] != "1" else "10"}"')
  give = has_asked_card(hands[1], hands[0], ask[0])
  if give:
    print(f'You gave player 2 your {ask[0] if ask[0] != "1" else "10"}')
  else:
    print('You say: "Go Fish!"')
    print("Player 2 draws a card")
    draw_a_card(hands[1])
  hands[1] = ai_pairs(hands[1])
  display(hands[1])
  return hands[1]
  
  

deck = create_deck()
random.shuffle(deck)
turn = 1
points = [0,0]
hands = [[],[]]
points = [0,0]
discards = [[],[]]
deal()
hands[1] = ai_pairs(hands[1])
start_game(hands)


while hands[0] != [] and hands[1] != []:
  if turn % 2 == 1:
    start_turn(turn, hands, points)
    guess = input("Ask for a card: ")
    ask_opponent(guess, turn, hands)
  else:
    hands[1] = ai_turn(hands)
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