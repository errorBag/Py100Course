# TODO реализовать функцию
def remove_whitespace(text_):
    text_no = text_.split(' ')
    list_ = []
    for value in text_no:
        if value:
            list_.append(value)
    return ' '.join(list_)

str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
