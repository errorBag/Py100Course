# TODO Запишите функцию `factorial`
def factorial(value):
    if value == 0:
        return 1
    result = 1
    for i in range(1, value + 1):
        result *= i
    return result


# TODO Вызовите функцию factorial и распечатайте результат 
print(f"Факториал числа 0 равен {factorial(0)}")
print(f"Факториал числа 5 равен {factorial(5)}")
