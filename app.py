# Import your Game class

# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop

from phrasehunter.game import Game
# from phrasehunter.phrase import Phrase

if __name__ == "__main__":
    
# ====TEST CODE====
    # phrase = Phrase()
    # game = Game()
    # print(phrase)
    # print(game)

    # game = Game()
    # for phrase in game.phrases:
    #     print(phrase.phrase)

    # def print_phrase(phrase_object):
    #     print(f"The phrase is: '{phrase_object.phrase}'.")

    # game = Game()
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())

    # game = Game()
    # print(game.active_phrase)
    # print(game.active_phrase.phrase)

    # game = Game()
    # print(game.active_phrase.phrase)
    # game.active_phrase.display(game.guesses)
    
    game = Game()   
    print(game.active_phrase.phrase)
    game.start()
    


# ==== END TEST CODE ====