# TODO Напишите функцию `calculate_parking_load`
def calculate_parking_load(total_parking_spaces, occupied_parking_spaces):
    parking_load = (occupied_parking_spaces / total_parking_spaces) * 100
    return round(parking_load)

total_seats = 5700
seats_occupied = 1243

print(calculate_parking_load(total_seats, seats_occupied), "%", sep='')
