import random, sys
from pathlib import Path

with open("wordList.txt") as f:
    wordList = [line.rstrip() for line in f]

tries = 5

try:
    while True:
        triesLeft = tries
        rand = random.randint(0, len(wordList) - 1)
        word = wordList[rand]

        if len(word) < 4:
            continue
        discovered = [False] * len(word)
        lettersGuessedList = []

        while triesLeft > 0:
            print("Guess the word (" + str(len(word)) + " letters): ", end="")

            for i in range(len(word)):
                if discovered[i] == True:
                    print(word[i], end="")
                else:
                    print("_", end="")

            print(
                "\nYou have " + str(triesLeft) + " tries left. Please enter a letter:",
                end="",
            )
            letterGuessed = input()


            if letterGuessed in lettersGuessedList:
                print('You have already guessed that letter!')
                continue
            elif letterGuessed.isalpha() == False or len(letterGuessed) != 1:
            	print("You will need to enter a valid letter.")
            	continue
            else:
                lettersGuessedList.append(letterGuessed)

            letterCorrect = False
            for i in range(len(word)):
                if word[i].casefold() == letterGuessed.casefold():
                    discovered[i] = True
                    letterCorrect = True

            if letterCorrect == False:
                triesLeft -= 1

            if discovered == [True] * len(word):
                input(word + "\n" + "You win. Congratulations!\n")
                break

        if triesLeft == 0:
            print("You lost! ")
            print("The word was: ", word)

except KeyboardInterrupt:
    sys.exit()
