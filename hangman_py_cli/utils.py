import re
from random import choice
from constants import CATEGORIES
from constants import SELECTED_CATEGORIES


def remove_accents(word):
    """
    Função com regular expression usada para verificar e substituir \
    acentos e "ç".
    :param word: palavra que irá ser verificada 
    :type word: str
    :return: Retorna a letras sem acentos e com "c" no lugar de "ç"
    :rtype: str
    """
    word = re.sub(r"[ç]", "c", word)
    word = re.sub(r"[áàâãÁÀÂÃ]", "a", word)
    word = re.sub(r"[éèêÉÈÊ]", "e", word)
    word = re.sub(r"[íìîÍÌÎ]", "i", word)
    word = re.sub(r"[óòôõÓÒÔÕ]", "o", word)
    word = re.sub(r"[úùûÚÙÛ]", "u", word)

    return word


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
    partir da categoria escolhida pelo usuário

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


def total_tries(selected_word):
    """
    Número de chances baseado no tamanho da palvra
    evitando que as chances não sejam maior que 18 e menor que 8

    :param selected_word: palavra para verificação da quantidade de chances
    :type selected_word: str
    :return: retorna um numero de caracteres
    :rtype: int
    """
    tries = len(set(selected_word)) * 1.5
    if tries >= 19:
        tries = 18
    elif tries <= 6:
        tries = 6
    return round(tries)


def play(selected_word, total_tries=total_tries):
    """
    Executa o jogo de adivinhação de palavras.
    A função primeiro substitui todas as letras na palavra selecionada por sublinhados ('_'),
    mantendo os hifens intactos. Em seguida, solicita ao jogador para adivinhar uma letra de cada vez.
    Se a letra adivinhada estiver na palavra selecionada, a função substitui o sublinhado correspondente
    pela letra correta. O jogo continua até que todas as letras sejam adivinhadas corretamente.

    :param selected_word:  A palavra que o jogador deve adivinhar.
    :type selected_word: str
    """  # noqa: E501
    current_state = ["_" if letter != "-" else "-" for letter in selected_word]
    total_tries = total_tries(selected_word)
    while "_" in current_state and total_tries != 0:
        print(f"Voçê possui {total_tries} chances para acertar!!")
        without_accents = remove_accents(selected_word)
        print(*current_state)
        guess = input("Digite uma letra: ").lower()
        if len(guess) != 1:
            print(f"Erro: numero de letras ==>{len(guess)}<== digite apenas 1 por vez ")
        elif not guess.isalpha():
            print(f"Erro: ==>{guess}<== Digite apenas letra")
        else:
            found = False
            for index in range(len(without_accents)):
                if guess in without_accents[index] and guess:
                    current_state[index] = guess
                    found = True
            if not found:
                total_tries -= 1
    print(selected_word)
