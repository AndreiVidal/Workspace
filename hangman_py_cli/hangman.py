from random import choice
from contants import CATEGORIES
from contants import SELECTED_CATEGORIES


def show_choice_menu():
    chosen_category = ""
    while not chosen_category:
        for k, v in CATEGORIES.items():
            print(f"{k} - {v}")
        chosen_category = input("escolha: ")
        if chosen_category not in CATEGORIES.keys():
            print("escolha errada:")
            chosen_category = ""

    return chosen_category


def random_word_category(chosen_category):
    with open(SELECTED_CATEGORIES[chosen_category], mode="r") as selected_c:
        words = []
        for word in selected_c.readlines():
            words.append(word.strip())
    selected_word = choice(words)
    print(selected_word)
    return selected_word


if __name__ == "__main__":
    x = show_choice_menu()
    random_word_category(x)
