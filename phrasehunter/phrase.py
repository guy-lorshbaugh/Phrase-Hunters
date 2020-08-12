class Phrase:
    def __init__(self, phrase):
        '''Converts the phrases provided into 
        lowercase for processing in the script.
        '''
        self.phrase = phrase.lower()
        
    def display(self, guesses):
        '''Displays puzzle phrase as underscores and
        fills them in as user guesses coorectly.
        '''
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end = " ")
            else:
                print("_", end = " ")
        print("\n")
        # print("***  ", *self.output, "  ***\n")
        if len(guesses) > 1:
            print("You've guessed the following lettters:", *guesses, "\n")  
        

    def check_guess(self, guess):
        '''Checks user guess against the puzzle phrase.'''
        if guess.lower() in self.phrase:
            return True
        else:
            return False

    def check_complete(self, guesses):
        '''Tells the program when user has guessed all the letters'''
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True