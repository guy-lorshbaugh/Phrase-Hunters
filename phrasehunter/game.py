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
            Phrase("Cant stop here this is bat country"),
        ]

        self.active_phrase = random.choice(self.phrases)
        self.guesses = []

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
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:

            print(f"You have used {self.missed} of 5 incorrect guesses.\n")
            self.active_phrase.display(self.guesses)
            self.user_guess = self.get_guess()
            self.guesses.append(self.user_guess)
            if not self.active_phrase.check_guess(self.user_guess):
                self.missed += 1
                print(f"\nSorry, '{self.user_guess}' is not in the phrase!\n")
            
        print("Bummer!  You've used all your guesses.\n")


    def get_guess(self):
        self.guess = input("Guess a letter!  ")
        return(self.guess)

        #  and self.active_phrase.check_complete(self.guesses) == False