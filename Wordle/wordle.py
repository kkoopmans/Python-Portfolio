'''
Program: Wordle
Author: Mrs Koopmans
Date: 2022-02-11
'''

#the random library will be used for choosing a random secret word.
import random
import os
import json

#I've chosen to show the instructions just once at the start of the program.
def welcome_message():
  print(f'{"WORDLE":^44}')
  print(f'{"Get 6 chances to guess":^44}')
  print(f'{"a 5-letter word":^44}')
  print("")
  print("How To Play")
  print("Guess the Wordle in 6 tries.")
  print("")
  print(" - Each guess must be a valid 5-letter word.")
  print(" - You will get a clue containing")
  print("   symbols to show how close your")
  print("   guess was to the word.")
  print("")
  print("Example")
  print(f'{"WEARY":^44}')
  print(f'{"#-*--":^44}')
  print(" - W is the first letter of the word")
  print(" - A is somewhere in the word, but not in ")
  print("   the third position")
  print(" - There are no Es, Rs, or Ys in the word")
  print("")
  input("Press enter when you're ready to start!")

#randomly selects the secret word from the list of common 5-letter words
def choose_word():
  global word_list
  return random.choice(word_list)

# calculates changes to the player's record
def record(won, guesses):
  with open("Wordle/record.json") as record_file:
    records = json.load(record_file)

  records["Played"] += 1
  if won:
    records["Current Streak"] += 1
    records[str(guesses)] += 1
  else:
    records["Current Streak"] = 0
  if records["Current Streak"] > records["Max Streak"]:
    records["Max Streak"] = records["Current Streak"]

  display_record(records)

  with open("Wordle/record.json","w") as record_file:
    json.dump(records, record_file)

# displays the player's updated record
def display_record(rec):
  win_percent = (rec["1"]+rec["2"]+rec["3"]+rec["4"]+rec["5"]+rec["6"])*100/rec["Played"]
  print()
  print("STATISTICS")
  print(f'                      Current    Max')
  print(f'  Played    Win %     Streak     Streak')
  print(f'{rec["Played"]:^10}{(str(round(win_percent))+"%"):^10}{rec["Current Streak"]:^10}{rec["Max Streak"]:^10}')
  print()
  print("GUESS DISTRIBUTION")
  print(f'1: {("*"*round(rec["1"]*10/rec["Played"])):<11}{rec["1"]}')
  print(f'2: {("*"*round(rec["2"]*10/rec["Played"])):<11}{rec["2"]}')
  print(f'3: {("*"*round(rec["3"]*10/rec["Played"])):<11}{rec["3"]}')
  print(f'4: {("*"*round(rec["4"]*10/rec["Played"])):<11}{rec["4"]}')
  print(f'5: {("*"*round(rec["5"]*10/rec["Played"])):<11}{rec["5"]}')
  print(f'6: {("*"*round(rec["6"]*10/rec["Played"])):<11}{rec["6"]}')

def green_clues(guess, secret_word):
  #will track letters we've given clues about
  clues_so_far = []
  #will contain 5 characters, #, * or -, to tell the player how close their guess is
  hint_list = []
  #loop thru 0-4 (indices of letters in a 5 letter word)
  for i in range(0,5):
    #correct letter in the correct spot gets #
    if guess[i] == secret_word[i]:
      hint_list.append("#")
      clues_so_far.append(guess[i])
    else:
      hint_list.append("-")

  return hint_list, clues_so_far

def yellow_clues(guess, secret_word, hint_list, clues_so_far):
  #loop thru 0-4 (indices of letters in a 5 letter word)
  for i in range(0,5):
    #check for possible stars - ie it's in the word but not in the right place.
    if guess[i] in secret_word and guess[i] != secret_word[i]:
      #count number of occurances of letter in guess and in secret word
      times_in_guess = guess.count(guess[i])
      times_in_ans = secret_word.count(guess[i])
      #if there's fewer or equal number of occurances in the guess than the answer
      #or if we haven't given enough clues yet, we'll give a star.
      if times_in_guess <= times_in_ans or clues_so_far.count(guess[i]) < times_in_ans:
        hint_list[i] = "*"
      #since we've given a hint about this letter now, add it to the list of clues so far
      clues_so_far.append(guess[i])
  return(hint_list)

#generates and returns a 5 character hint based on the user's guess
def generate_hint(guess, secret_word):

  #convert both words to lists
  guess = list(guess)
  secret_word = list(secret_word)

  hint_list, clues_so_far = green_clues(guess, secret_word)
  hint_list = yellow_clues(guess, secret_word, hint_list, clues_so_far)

  #combine hint list into one 5-character string.
  return "".join(hint_list)


#checks if the user's guess is valid and prints feedback to the user
#about why their guess is not valid if needed.
def is_valid_guess(curr_guess, secret_word):

  global dictionary
  if len(curr_guess) != 5 and curr_guess != "":
    print("Your guess must be 5 letters")
  elif curr_guess != "" and not curr_guess.isalpha():
    print("Your guess must contain only letters")
  elif curr_guess != "" and (curr_guess not in dictionary):
    print("That word is not in my dictionary")
  elif curr_guess != "":
    print(" " * 23 + generate_hint(curr_guess, secret_word))
    #this is will only be reached if the guess is valid
    return True
  return False

def get_guess(num_guesses, secret_word):
  guess = ""
  while not is_valid_guess(guess, secret_word):
    guess = input("Guess a 5 letter word: ").lower()
  num_guesses += 1
  return guess, num_guesses

def play_game():
  num_guesses = 0
  guess = ""
  secret_word = choose_word()

  #for testing
  #print(secret_word)

  while guess != secret_word and num_guesses < 6:
    guess, num_guesses = get_guess(num_guesses, secret_word)

  #once loop has terminated, they either guessed correctly or guessed too many times.
  if guess == secret_word:
    print("That's right!")
    print(f"That took {num_guesses} guesses.")
    win = True
  else:
    print("Sorry, you've run out of guesses.")
    print(f"The correct answer was {secret_word}")
    win = False

  record(win, num_guesses)



#allow game to run first time
play = True

welcome_message()

#read secret word list and dictionary
with open("Wordle/secret_word_list.txt") as wordlist_file:
  word_list = []
  for word in wordlist_file:
    word_list.append(word.strip())

with open("Wordle/five_letter_dict.txt") as dictionary_file:
  dictionary = []
  for word in dictionary_file:
    dictionary.append(word.strip())

#allows whole game to be re-played.
while play:
  os.system('clear')
  play_game()

  again = input("Do you want to play again? ")
  if again.lower() != "y" and again.lower() != "yes":
    play = False

print("Thanks for playing!")