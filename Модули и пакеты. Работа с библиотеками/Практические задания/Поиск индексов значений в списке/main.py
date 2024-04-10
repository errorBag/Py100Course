from typing import Any
def index(list_of_values: list, value: Any):
    index_value = [i for i, index_value in enumerate(list_of_values) if index_value == value]
    # print(index_value)
    if not index_value:
        raise ValueError

    return index_value

    # try:
    #     return list_of_values.index(value)
    # except ValueError:
    #     raise ValueError(f"Элемента {value} нет в списке")


if __name__ == '__main__':
    list_items = [1, 2, "3", 1]
    print(index(list_items, 1) == [0, 3])  # True
