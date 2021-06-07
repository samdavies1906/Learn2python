import random
import os

playing = True
while playing:

    # Clear console each run
    os.system('cls||clear')

    # Variables
    wordToGuess = ""
    wordMask = []
    lives = 10
    wordGuessed = False
    guesses = ""


    def split(word):
        return [char for char in word]

    # Pick a random word from a text file
    with open("hangmanWords.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))

    wordToGuess = random.choice(words).lower()
    wordToGuess = split(wordToGuess)
    print("".join(wordToGuess))

    # Make a word mask with *** of the same length as the word to guess
    for x in wordToGuess:
        wordMask = wordMask + ["*"]

    # Let the player know how long the word is
    print("The word is " + str(len(wordToGuess)) + " letters long")
    print("".join(wordMask))

    # Play game
    while lives > 0:

        # Guess a letter
        validGuess = False
        while validGuess == False:
            validGuess = True
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                validGuess = False
                print("Only enter 1 character")
            
            if not guess.isalpha():
                validGuess = False
                print("Only an alphabetical character")

            if (guess in guesses):
                validGuess = False
                print("Already guessed " + guess + " Try again")

        guesses += guess

        # Look for letter in word
        locationOfLetters = []
        for index, letter in enumerate(wordToGuess, start = 0):
            if (letter == guess):
                locationOfLetters.append(index)

        for pos in locationOfLetters:
            wordMask[pos] = guess

        # If len is 0 letter not in word, lose life
        if len(locationOfLetters) == 0:
            lives -= 1
            print("Wrong, " + str(lives) + " lives remaining")

        print("".join(wordMask))

        # Check if word to guess and the mask ever match
        if "".join(wordToGuess) == "".join(wordMask):
            wordGuessed = True
            break

    # On exit of loop checking game conditions
    if wordGuessed == True:
        print("Well done you WIN!!!")
    else:
        print("You ran out of lives, better luck next time")

    playAgain = input("Do you want to play again YES(y) or NO(n): ").lower()
    if playAgain == "n" or playAgain == "NO":
        playing = False
            
exit()
    