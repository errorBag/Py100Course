# TODO реализовать функцию
def get_unique_words(code):
    list_ = code.split()
    plenty = set(list_)
    list_ = list(plenty)
    list2 = sorted(list_)


    return list2


print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
