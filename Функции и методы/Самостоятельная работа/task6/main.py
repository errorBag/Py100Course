ALLOW_SYMBOLS = ["0", "1"]  # Допустимые символы


def check_string(str_):
    # if not str_:
    #     return False
    # for i in set(str_):
    #     if i not in ALLOW_SYMBOLS:
    #         return False
    # return True
    # if str_ and str_.isdigit():
    if str_.isdigit() and str_.replace('0', '') == str_.replace('1', ''):
        return True
    else:
        return False


print(check_string("1010101010"))
print(check_string("101021231010103"))
print(check_string("asdawqe"))
print(check_string(""))
