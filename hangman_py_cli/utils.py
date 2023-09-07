from random import choice
from contants import CATEGORIES
from contants import SELECTED_CATEGORIES


def show_choice_menu():
    """Mostra o menu das categorias disponíveis para escolha

    :return: Retorna a categoria escolhida pelo usuário
    :rtype: str
    """
    chosen_category = ""
    while not chosen_category:
        print("CATEGORIAS DISPONÍVEIS")
        for k, v in CATEGORIES.items():
            print(f"{k} - {v}")
        chosen_category = input("Escolha uma categoria:\n")
        if chosen_category not in CATEGORIES.keys():
            print(f"\n\n### {chosen_category} não é uma opção válida###\n\n")
            chosen_category = ""

    return chosen_category


def random_word_category(chosen_category):
    """
    Escolhe uma palavra de forma aleatória \
    partir da categotia escolhida pelo usuário

    :param chosen_category: Categoria escolhida
    :type chosen_category: str
    :return: Retorna a palavra que foi escolhida
    :rtype: str
    """
    with open(SELECTED_CATEGORIES[chosen_category], mode="r") as selected_c:
        words = []
        for word in selected_c.readlines():
            words.append(word.strip().lower())
    selected_word = choice(words)
    print(selected_word)
    return selected_word
