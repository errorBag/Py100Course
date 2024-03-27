# TODO Напишите функцию find_common_items
def find_common_items(last_week_items, current_week_items):
    m = list(set(last_week_items).intersection(current_week_items))
    k = sorted(m)
    return k



last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']

print(f"Общие товары: {find_common_items(last_week_items, current_week_items)}")  # TODO Распечатайте общие товары
