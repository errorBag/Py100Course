number = 2342354235235

list_digits = [int(num) for num in str(number)]
sum_number = sum(int(num) for num in str(number) if int(num) % 2 == 0)
#print(list_digits)  # TODO c помощью list comprehension получить список цифр числа

print(sum(list_digits))  # TODO найти сумму цифр числа
print(sum_number)  # TODO найти сумму всех четных чисел
print(len(list_digits))  # TODO найти количество цифр
print(min(list_digits))  # TODO найти минимальную цифру
print(list_digits[0] - list_digits[-1])  # TODO найти разность между первой и последней цифрой
