list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0
max_value = list_numbers[max_index]

# Находим максимальное значение и его индекс
for i, current_value in enumerate(list_numbers):
    if current_value >= max_value:
        max_value = current_value
        max_index = i

# Меняем местами последний максимальный и последний элементы
list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]

print(list_numbers)
