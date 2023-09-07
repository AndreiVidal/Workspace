import random


PATH_ANIMAL = "static/animal.txt"
PATH_FRUIT = "static/fruits.txt"
PATH_RANDOM = "static/word_random.txt"

categories = {
    "1":"ANIMAIS",
    "2":"FRUTAS",
    "3":"ALEATÓRIAS",
}
selected_category = {
    "1":PATH_ANIMAL,
    "2":PATH_FRUIT,
    "3":PATH_RANDOM,
}

chosen_category = ""
while not chosen_category:
    for k, v in categories.items():
        print(f'{k} - {v}')
    chosen_category = input('escolha: ')
    if chosen_category not in categories.keys():
        print('escolha errada:')
        chosen_category = ""
    

    print(categories[chosen_category])


with open(selected_category[chosen_category], mode='r') as selected_c:
    words = []
    for word in selected_c.readlines():
        words.append(word.strip())


print(random.choice(words))