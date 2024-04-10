# TODO Напишите функцию get_student_names
def get_student_names(list_):
    name_student = [
    person[term]
    for person in list_
    for term in person
    if term == "name"
    ]
    return name_student


if __name__ == '__main__':
    # Пример списка учеников
    students_list = [
        {
            "name": "Саша",
            "age": 27,
        },
        {
            "name": "Кирилл",
            "age": 52,
        },
        {
            "name": "Маша",
            "age": 14,
        },
        {
            "name": "Петя",
            "age": 36,
        },
        {
            "name": "Оля",
            "age": 43,
        },
    ]
    print(get_student_names(students_list))  # TODO Вызовите функцию get_student_names
