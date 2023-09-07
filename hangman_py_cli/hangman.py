from utils import random_word_category
from utils import show_choice_menu

if __name__ == "__main__":
    show_choice_menu = show_choice_menu()
    random_word_category(chosen_category=show_choice_menu)
