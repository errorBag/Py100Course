# TODO Напишите функцию get_oldest_participant
def get_oldest_participant(dict_):
    return max(dict_, key=lambda item: item["age"])






if __name__ == "__main__":
    participants_list = [
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

print(get_oldest_participant(participants_list))

    # oldest_participant = ...  # TODO Найдите самого старшего участника
    # print(oldest_participant)
