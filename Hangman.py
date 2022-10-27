import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def getUserInput():
    userGuess = ""
    while not(userGuess.isalpha() and len(userGuess) == 1):
        userGuess = input("Enter a letter: ").lower()

    return userGuess

def checkGuess(userGuess):
    if(userGuess in word):

        if(userGuess in correctGuesses):
            print("You have already guessed {}".format(userGuess))
        else:
            print("{} was in the word!".format(userGuess))
            correctGuesses.append(userGuess)

    else:
        print("{} is not in the word".format(userGuess))
        return False
    
    return True

def displayGuessedLetters():
    output = ""
    for letter in word:
        if(letter not in correctGuesses):
            letter = "_"
        output += letter

    print(HANGMANPICS[-lives])
    print(output + "\n")


############################### Main Program ###############################
while(True):
    lives = 7
    word = words[random.randint(0, len(words))].lower()
    correctGuesses = []
    print("The word is {length} letters long".format(length = len(word)))
    wordGuessed = False

    #Main Gameplay Loop
    while(lives > 0 and not wordGuessed):

        displayGuessedLetters()

        userGuess = getUserInput()
        if(not checkGuess(userGuess)): lives -= 1

        wordGuessed = (len(correctGuesses) == len(set(word)))

    #Win/Loss Message
    if (wordGuessed):
        print("\nCongratulations you guessed the word. The word was {}".format(word))
    else:
        print("\nYou ran out of lives, the word was {}".format(word))

    #Play again?
    userQuit = input("Type q to quit. Type anything else to play again: ").lower()
    if(userQuit == "q"): break
