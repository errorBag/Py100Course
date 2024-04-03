# TODO реализовать функцию
def get_sentences_list(text):
    list_ = []
    for i in text.split("."):
        if i:
            list_.append(i.strip())

    return list_


print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
