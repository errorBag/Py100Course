# TODO  Напишите функцию get_shortest_word
# def get_shortest_word(list_):
#     max_word = 1_000_000
#     min_slov = ''
#     for word in list_:
#         if len(word) < max_word:
#             min_slov = word
#     return min_slov

def my_min(word):
    return [len(len_) for len_ in word]

# words_list = ["apple", "banana", "orange", "grapefruit", "kiwi"]
# print(my_min(words_list))
if __name__ == "__main__":
    words_list = ["apple", "banana", "orange", "grapefruit", "kiwi"]
    shortest_word = min(words_list, key=my_min)  # TODO Найдите самое короткое слово
    print(shortest_word)  # kiwi
