# TODO Вызовите ошибку AssertionError с собственным текстом

def summ(a = int, b = int):
    if not isinstance(a, (int, float)):
        raise AssertionError('a не является числом')
    if not isinstance(b, (int, float)):
        raise AssertionError('b не является числом')
    return a + b


print(summ(int(input('Введите число   ')), input('Введите число   ')))