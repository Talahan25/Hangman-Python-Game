from wonderwords import RandomWord
import os


# -----------------------------
# Helper Functions
# -----------------------------
def clear_screen():
    """Clears the terminal window."""
    os.system("cls" if os.name == "nt" else "clear")


def generate_word(min_len=4, max_len=5):
    """Returns a random word (as uppercase list) and display list."""
    r = RandomWord()
    word = r.word(word_min_length=min_len, word_max_length=max_len).upper()
    display = ["-"] * len(word)
    return list(word), display


# -----------------------------
# Hangman Game Class
# -----------------------------
class HangmanGame:
    def __init__(self, lives=10):
        self.lives_left = lives
        self.letters_guessed = []
        self.word, self.display = generate_word()
        self.win = False

    # ---- Display ----
    def show_status(self):
        print(" >>>> HANGMAN <<<<\t\t Turns left:", self.lives_left)
        print("\t\t\t Letters Guessed:", ", ".join(self.letters_guessed))
        print("\n >>| " + " ".join(self.display) + " |<<\n")

    # ---- Input Processing ----
    def get_guess(self):
        guess = input("Guess a letter or word:\n---> ").upper()
        clear_screen()
        return guess

    # ---- Game Logic ----
    def process_guess(self, guess):
        # Word-length guess
        if len(guess) == len(self.word):
            return self.full_word_guess(guess)

        # Single-letter guess
        elif len(guess) == 1:
            return self.single_letter_guess(guess)

        # Invalid guess
        else:
            print(f"Guess must be 1 letter OR a {len(self.word)}-letter word.")
            return

    def full_word_guess(self, guess):
        """Handles full-word guesses."""
        if guess == "".join(self.word):
            self.win = True
            return

        print("Incorrect full-word guess.")
        self.letters_guessed.append(guess)
        self.lives_left -= 1

    def single_letter_guess(self, guess):
        """Handles single-letter guesses."""
        if guess in self.letters_guessed:
            print("You already guessed that letter.")
            return

        self.letters_guessed.append(guess)

        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.display[i] = letter

            if self.display == self.word:
                self.win = True
        else:
            print("Letter not in word.")
            self.lives_left -= 1

    # ---- Game Loop ----
    def play(self):
        """Main game loop."""
        clear_screen()
        print(">>> STARTING HANGMAN <<<\n")

        while self.lives_left > 0 and not self.win:
            self.show_status()
            guess = self.get_guess()
            self.process_guess(guess)

        # End results
        if self.win:
            print("You win! The word was:", "".join(self.word))
        else:
            print("You lose! The word was:", "".join(self.word))


# -----------------------------
# Run the Game
# -----------------------------
if __name__ == "__main__":
    game = HangmanGame(lives=10)
    game.play()
