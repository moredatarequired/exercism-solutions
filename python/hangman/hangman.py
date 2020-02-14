# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.word = word
        self.unguessed = set(word)
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("Sorry, the game is over")
        c = char.lower()
        if c in self.unguessed:
            self.unguessed.remove(c)
        else:
            self.remaining_guesses -= 1
        self.update_status()

    def update_status(self):
        if not self.unguessed:
            self.status = STATUS_WIN
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        return "".join("_" if l.lower() in self.unguessed else l for l in self.word)

    def get_status(self):
        return self.status
