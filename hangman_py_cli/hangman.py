import os
import sys
from random import choice
import unicodedata
from category import Category
from message import Message


class Hangman:
    def __init__(self) -> None:
        self.categories_path = "./categories"
        self.categories_filepaths = self.get_categories_filepaths()

        self.message = Message()

        self.categories = []
        self._category = None
        self._tries = None
        self.word = None

        self.init_categories()

        self.start()

    def init_categories(self):
        for filepath in self.categories_filepaths:
            self.categories.append(Category(filepath))

    def get_categories_filepaths(self) -> list:
        return [
            f"{self.categories_path}/{file}"
            for file in os.listdir(self.categories_path)
            if file.lower().strip().endswith(".txt")
        ]

    @property
    def category(self) -> Category:
        return self._category

    @category.setter
    def category(self, category: Category) -> None:
        if category:
            category.get_words()
        self._category = category

    @property
    def tries(self) -> int:
        return self._tries

    @tries.setter
    def tries(self, value: int) -> None:
        self._tries = value
        if self._tries <= 0:
            self.message.gameover(self.word)
            self.ask_to_continue()

    def ask_to_continue(self):
        if self.message.retry_ask():
            self.reset()
        else:
            sys.exit()

    def show_choice_menu(self):
        self.message.choice_menu(self.categories)

    def choose_category(self):
        while not self.category:
            try:
                response = self.message.choose_category()
                index_categories = int(response) - 1
                self.category = self.categories[index_categories]
                self.message.choosed_category(self.category)
            except Exception as error:
                print(f"EXCEPTION {error}")

    def choose_random_word(self):
        self.word = choice(self.category.words)

    def init_tries(self):
        tries = len(set(self.word)) * 1.5
        if tries >= 19:
            tries = 18
        elif tries <= 6:
            tries = 6
        self._tries = round(tries)

    @staticmethod
    def normalize(word):
        return "".join(
            c
            for c in unicodedata.normalize("NFD", word)
            if unicodedata.category(c) != "Mn"
        ).lower()

    def play(self):
        current_state = ["_" if letter != "-" else "-" for letter in self.word]
        normalized_word = self.normalize(self.word)

        guessed_letter = []

        def validate_guess(guess):
            if guess in guessed_letter:
                print(f"Erro: ==>{guess}<== Você já digitou essa letra")
                return False
            guessed_letter.append(guess)
            return True

        def found_guess_in_word(guess):
            for index, normalized_letter in enumerate(normalized_word):
                found = False
                if guess == normalized_letter:
                    current_state[index] = guess
                    found = True
            return found

        while "_" in current_state and self.tries != 0:
            print(f"Você possui {self.tries} chances para acertar!!")
            print(*current_state)
            print()

            guess = input("Digite uma letra: ").lower()

            if not validate_guess(guess):
                continue

            if not found_guess_in_word(guess):
                self.tries -= 1

        self.message.won(self.word)
        self.ask_to_continue()

    def start(self):
        self.show_choice_menu()
        self.choose_category()
        self.choose_random_word()
        self.init_tries()
        self.play()

    def reset(self):
        self._category = None
        self._tries = None
        self.word = None
        self.start()
