# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    guessed = True
    for char in secretWord:
        if char not in lettersGuessed:
            guessed = False
            break
    return guessed


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    out = ''
    for char in secretWord:
        if char in lettersGuessed:
            out = out + char
        else:
            out = out + '_ '
    return out


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alph = list(string.ascii_lowercase)
    for char in lettersGuessed:
        alph.remove(char)
    out = ''.join(alph)
    return out



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    import string

    # welcome message
    print('Welcome to the game, Hangman!')

    # indicate length of secret word
    word_len = len(secretWord)
    print('I am thinking of a word that is {0} letters long.'.format(word_len))
    #print('-------------')

    num_guess_left = 8
    letters_guessed = []
    chars_remaining = getAvailableLetters(letters_guessed)
    finished = isWordGuessed(secretWord, letters_guessed)

    while num_guess_left > 0 and not finished:
        print('-------------')
        print('You have {0} guesses left.'.format(num_guess_left))
        print('Available letters: {0}'.format(chars_remaining))

        guess = input('Please guess a letter:')
        guess = guess.lower()

        guessed_state = getGuessedWord(secretWord, letters_guessed)
        if guess in letters_guessed:
            print("Oops! You've already guessed that letter: {0}".format(guessed_state))
        else:  # new guess
            letters_guessed.append(guess)
            chars_remaining = getAvailableLetters(letters_guessed)
            if guess in secretWord:
                guessed_state = getGuessedWord(secretWord, letters_guessed)
                print("Good guess: {0}".format(guessed_state))
                finished = isWordGuessed(secretWord, letters_guessed)
            else: # new guess is not in secret word
                num_guess_left -= 1
                print("Oops! That letter is not in my word: {0}".format(guessed_state))

    # decide if user won or lost
    print("-----------")
    if num_guess_left > 0:
        print('Congratulations, you won!')
    else:
        print("Sorry, you ran out of guesses. The word was {0}.".format(secretWord))



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
secretWord = 'sea'
hangman(secretWord)
