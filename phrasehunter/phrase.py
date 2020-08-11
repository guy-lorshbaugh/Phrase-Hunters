# Create your Phrase class logic here.

class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def display(self, guesses):
        self.letters = []
        self.output = []
        self.letters.extend(self.phrase)
        for letter in self.letters:
            if letter == " ":
                self.output.append(" ")
            elif letter in guesses:
                self.output.append(letter)
            else:
                self.output.append("_")
        print("***  ", *self.output, "  ***\n")
        if len(guesses) > 1:
            print("You've guessed the following lettters:", *guesses, "\n")  
        

    def check_guess(self, guess):
        if guess in self.letters:
            return True
        else:
            return False

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True