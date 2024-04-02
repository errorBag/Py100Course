# TODO реализовать функцию count
def count(list_1, num):
    return list_1.count(num)


list_items = [1, 2, "3", 1]
print(count(list_items, 1) == list_items.count(1))  # True
print(count(list_items, 3) == list_items.count(3))  # True
