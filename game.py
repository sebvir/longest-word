# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import string
import random

class Game:
    string.ascii_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def __init__(self):
        self.random_grid()
        
    def random_grid(self):
        self.grid = []
        for i in range(9):
            self.grid.append(random.choice(string.ascii_letters))
        self.is_valid(self.grid)
        
    def is_valid(self, word):
        if len(word) > 0:
            for i in word:
                if i not in self.grid:
                    return False
            return True
        return False
    
    #solution from web
    #def is_valid(self, word):
        #if not word:
            #return False
        #letters = self.grid.copy() # Consume letters from the grid
        #for letter in word:
            #if letter in letters:
                #letters.remove(letter)
            #else:
                #return False
        #return True
