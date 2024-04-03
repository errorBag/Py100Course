# TODO Вызовите ошибку AssertionError с собственным текстом

def summ(a = int, b = int):
    return a + b
    if a not a.isdigit():
        raise AssertionError("Текст ошибки")

print(summ(3, 4))