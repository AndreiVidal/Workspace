from utils import random_word_category
from utils import show_choice_menu
from utils import play


if __name__ == "__main__":
    chosen_category = show_choice_menu()
    selected_word = random_word_category(chosen_category=chosen_category)

    play(selected_word)
