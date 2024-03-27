# TODO Напишите функцию calculate_average_age для расчета среднего возраста студентов
def calculate_average_age(dict_):
    list_ = dict_.values()
    general_age = sum(list_)
    number_students = len(students_dict)
    average_age = general_age / number_students
    return average_age


students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}
calculate_average_age(students_dict)

print(f"Средний возраст студентов: {calculate_average_age(students_dict)}")  # TODO Распечатайте средний возраст студентов
print()

pass