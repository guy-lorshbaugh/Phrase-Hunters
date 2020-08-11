# Create your Game class logic in here.
import random
from phrasehunter.phrase import Phrase

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("Life is like a box of chocolates"),
            Phrase("Tomorrow is another day"),
            Phrase("May the Force be with you"),
            Phrase("Go away or I shall taunt you a second time"),
            Phrase("Sometimes you eat the bear sometimes the bear eats you"),
        ]

        self.active_phrase = random.choice(self.phrases)
        self.guesses = [" "]

    def welcome(self):
        stars = "*" * 39
        print(f"""
        {stars}
          Welcome to Python Wheel of Fortune!
              (except without the wheel)     
        {stars}
        """)

    def start(self):
        self.welcome()
        print("Your category today is Movie Quotes.\n")
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(f"\nYou have used {self.missed} of 5 incorrect guesses.\n")
            self.active_phrase.display(self.guesses)
            self.user_guess = self.get_guess()
            self.guesses.append(self.user_guess)
            if not self.active_phrase.check_guess(self.user_guess):
                self.missed += 1
                print(f"\nSorry, '{self.user_guess}' is not in the phrase!\n")
        self.game_over()

    def get_guess(self):
        self.guess = None
        self.guess = input("Guess a letter!  ")
        while len(self.guess) > 1 or self.guess.isalpha() is False:
            self.guess = input("\nOOPS!  Please enter only one alphabetical character.\nGuess a letter!  ")
        return self.guess 

    def game_over(self):
        if self.missed == 5:
            print("""
        Sorry, GAME OVER! You've used all your guesses!
        The phrase was '{}.'
            """.format(self.active_phrase.phrase.capitalize()))
        elif self.active_phrase.check_complete(self.guesses) == True:
            print("""
        *** {}! ***\n
        Congratulations!  You guessed the phrase!
              Now go make yourself a treat!
        """.format(self.active_phrase.phrase.upper()))
        self.play_again()

    def play_again(self):
        self.input = input("Would you like to play another round? (Y/N)  ")
        if self.input.lower() == 'y':
            game = Game()
            game.start()
        else:
            stars = "*" * 51
            print(f"""
        {stars}
          Thank you for playing Python Wheel of Fortune!!
        {stars}
            """)

