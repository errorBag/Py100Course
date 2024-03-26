list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

# TODO завести отдельные счетчики для четных и нечетных чисел
even_numbers = 0
not_even_numbers = 0
# TODO с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных
for i in list_:
    if i % 2 == 0:
        even_numbers += i
    elif i % 2 != 0:
        not_even_numbers += i
if even_numbers > not_even_numbers:
    print("Четных чисел больше")
elif even_numbers < not_even_numbers:
    print("Нечетных чисел больше")
elif even_numbers == not_even_numbers:
    print("Четных и нечетных одинаковое количество")
# TODO вывести каких чисел больше
