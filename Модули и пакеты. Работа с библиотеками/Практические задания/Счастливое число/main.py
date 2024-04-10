def is_lucky_number(num: int) -> bool:
    if not len(str(num)) == 6:
        raise ValueError
    if num <= 0:
        raise  ValueError

    list_digits = [int(digit) for digit in str(num)]
    return sum(list_digits[:3]) == sum(list_digits[3:])



print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
