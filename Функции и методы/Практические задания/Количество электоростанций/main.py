def count_powerful_powerplants(powerplants_list):
    count = 0
    for power in powerplants_list:
        if power["power"] > threshold_power:
            count += 1
    return count

    ...  # TODO Найдите количество электростанций, мощность которых превышает заданное значение


powerplants = [
    {"name": "ГЭС-1", "power": 1200},
    {"name": "АЭС-2", "power": 3200},
    {"name": "ТЭЦ-3", "power": 2800},
    {"name": "СГУ-4", "power": 500},
    {"name": "ВЭС-5", "power": 1800},
]

threshold_power = 2000

powerplants_count = count_powerful_powerplants(powerplants)  # TODO Вызовите функцию count_powerful_powerplants
print(f"Количество электростанций, мощность которых превышает заданное значение: {powerplants_count}")
