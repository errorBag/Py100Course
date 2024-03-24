# Список словарей со студентами и их оценками

students = [
    {"name": "Маша", "grade": 4},
    {"name": "Петя", "grade": 3},
    {"name": "Саша", "grade": 5},
    {"name": "Кирилл", "grade": 2},
    {"name": "Оля", "grade": 4},
]



for students in students:
    if students['grade'] > 3:
        print(f'{students["name"]}. Оценка: {students["grade"]}')
# TODO Распечатать имена студентов с оценками выше тройки
