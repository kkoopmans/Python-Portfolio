'''
Program: Wordle Full Hint Logic
Author: Mrs Koopmans
Date: 2022-02-11
'''

#the random library will be used for choosing a random secret word.
import random
import os

#I've chosen to show the instructions just once at the start of the program.
def welcomeMessage():
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
def chooseWord():
  '''
  ===PART 2===
  Here, you should change the hard-coded list of words I've used to the
  secret word list from the file. You should only read in the file once
  (not every time the program selects a new word)
  '''
  wordList = ["brave", "smart", "pride", "among","charm","elbow", "drive", 
              "plant", "eerie", "spool", "pasta","refer"]
  return random.choice(wordList)

def record():
  '''
  ===Part 3===
  Define and use functions to read in your csv, process and update it,
  display the user's record (formatted) and update the file based on
  the win/loss that just occurred.
  Use this function and helper functions to do these things.
  Note: You can modify the name, parameters and returns of this function
  to better suit your solution
  '''
  pass

def greenClues(guess, secretWord):
  #will track letters we've given clues about
  cluesSoFar = []
  #will contain 5 characters, #, * or -, to tell the player how close their guess is
  hintList = []
  #loop thru 0-4 (indices of letters in a 5 letter word)
  for i in range(0,5):
    #correct letter in the correct spot gets #
    if guess[i] == secretWord[i]:
      hintList.append("#")
      cluesSoFar.append(guess[i])
    else:
      hintList.append("-")

  return hintList, cluesSoFar

def yellowClues(guess, secretWord, hintList, cluesSoFar):
  #loop thru 0-4 (indices of letters in a 5 letter word)
  for i in range(0,5):
    #check for possible stars - ie it's in the word but not in the right place.
    if guess[i] in secretWord and guess[i] != secretWord[i]:
      #count number of occurances of letter in guess and in secret word
      timesInGuess = guess.count(guess[i])
      timesInAns = secretWord.count(guess[i])
      #if there's fewer or equal number of occurances in the guess than the answer
      #or if we haven't given enough clues yet, we'll give a star.
      if timesInGuess <= timesInAns or cluesSoFar.count(guess[i]) < timesInAns:
        hintList[i] = "*"
      #since we've given a hint about this letter now, add it to the list of clues so far
      cluesSoFar.append(guess[i])
  return(hintList)

#generates and returns a 5 character hint based on the user's guess
def generateHint(guess, secretWord):

  #convert both words to lists
  guess = list(guess)
  secretWord = list(secretWord)

  hintList, cluesSoFar = greenClues(guess, secretWord)
  hintList = yellowClues(guess, secretWord, hintList, cluesSoFar)

  #combine hint list into one 5-character string.
  return "".join(hintList)


#checks if the user's guess is valid and prints feedback to the user
#about why their guess is not valid if needed.
'''
===PART 2===
Update isValidGuess to also return false if the word is not in 
the five letter dictionary from part 1.
To do this, you'll need to read in the contents of fiveLetterDict.txt
NOTE: Do not read in the file every time you validate a guess.
The file should only be read once.
'''
def isValidGuess(currGuess, secretWord):
  if len(currGuess) != 5 and currGuess != "":
    print("Your guess must be 5 letters")
  elif currGuess != "" and not currGuess.isalpha():
    print("Your guess must contain only letters")
  elif currGuess != "":
    print(" " * 23 + generateHint(currGuess, secretWord))
    #this is will only be reached if the guess is valid
    return True
  return False

def getGuess(numGuesses, secretWord):
  guess = ""
  while not isValidGuess(guess, secretWord):
    guess = input("Guess a 5 letter word: ").lower()
  numGuesses += 1
  return guess, numGuesses

def playGame():
  numGuesses = 0
  guess = ""
  secretWord = chooseWord()

  while guess != secretWord and numGuesses < 6:
    guess, numGuesses = getGuess(numGuesses, secretWord)

  #once loop has terminated, they either guessed correctly or guessed too many times.
  if guess == secretWord:
    print("That's right!")
    print(f"That took {numGuesses} guesses.")
  else:
    print("Sorry, you've run out of guesses.")
    print(f"The correct answer was {secretWord}")

  record()



#allow game to run first time
play = True

welcomeMessage()
#allows whole game to be re-played.
while play:
  os.system('clear')
  playGame()

  again = input("Do you want to play again? ")
  if again.lower() != "y" and again.lower() != "yes":
      play = False

print ("Thanks for playing!")