from random_word import RandomWords

r = RandomWords()


class HangmanWord():

    def __init__(self):
        #self.word = r.get_random_word()
        self.word = "happy"
        # print(self.word)
        self.letters = list(self.word)
        #print(self.letters)
        self.guesses = list()
        self.incorrect = list()
        print('I got a word! :)')
        print('You may begin guessing!')
        for item in self.letters:
            print("_", end=" ")
        print("")

    def currentPrinter(self):
        for item in self.letters:
            if (item in self.guesses):
                print(item, end=" ")
            else:
                print("_", end=" ")
        print("")

    def guess(self, guess):
        if len(guess) > 1:
            print("Please enter a single character!")
            return
        checkGuess = guess.lower()
        if (checkGuess in self.guesses):
            print("You have already guessed this!")
            return
        self.guesses.append(checkGuess)

        if (checkGuess in self.letters):
            print("You Guessed correctly!")
            self.currentPrinter()
        else:
            print("Whoops! Wrong answer please try again! You have {} guesses left".format(10 - self.totalIncorrect()))
            self.incorrect.append(checkGuess)
            self.currentPrinter()

    def totalIncorrect(self):
        return len(self.incorrect)

    def totalGuesses(self):
        return len(self.guesses)

    def isCompleted(self):
        for item in self.letters:
            if (item in self.guesses):
                # print(item, end=" ")
                returner = True
            else:
                return False
        return True

    def won(self):
        if self.totalIncorrect() <= 10:
            returner = True
            if self.isCompleted():
                returner = True
                print("Congratulations! The word was {}. You won! You guessed the correct answer in {} guesses!".format(
                    self.word, self.totalGuesses()))
            else:
                returner = False
                print("Oh no! The word was {}. You lost! Better luck next time!".format(
                    self.word))
        else:
            returner = False

        #return returner


def startGame():
    while True:
        game = HangmanWord()
        while game.totalIncorrect() < 10 and game.isCompleted() == False:
            guesser = input("Guess: ")
            game.guess(guesser)

        game.won()
        playagain = input("Would you like to play again? [y]es or [n]o")
        if (playagain == 'n'):
            break

    print("Thanks for playing!")

startGame()

