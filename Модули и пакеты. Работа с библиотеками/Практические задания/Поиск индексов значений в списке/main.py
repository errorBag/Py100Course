from typing import Any
def index(list_of_values: list, value: Any):
    try:
        return list_of_values.index(value)
    except ValueError:
        raise ValueError(f"Элемента {value} нет в списке")


if __name__ == '__main__':
    list_items = [1, 2, "3", 1]
    print(index(list_items, 1) == [0, 3])  # True
