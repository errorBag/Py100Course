# TODO Напишите функцию calculate_average_age
def calculate_average_age(list_):
    studen = len(list_)

    age = [student[age]
           for student in list_
           for age in student
           if age == "age"
           ]
    average_age = sum(age) / studen
    return average_age

# TODO Напишите функцию filter_students_by_age
def filter_students_by_age(student_list, age_: float):
    age_students = [student
                    for student in student_list
                    if student['age'] < age_
                    ]

    return age_students

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


    average_age_of_students = calculate_average_age(students_list)
    filtered_students = filter_students_by_age(students_list, average_age_of_students)
    print("Средний возраст учеников:", average_age_of_students)
    print("Список учеников с возрастом меньше среднего:")
    for current_student in filtered_students:
        print(current_student['name'])
