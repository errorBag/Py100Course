# TODO Напишите функцию decimal_to_hex
import os
def decimal_to_hex():
    # return {decimal: hex(decimal) for decimal in range(16)}
    hex_dict = {}
    for decimal in range(16):
        decimal_hex = hex(decimal)
        hex_dict.update({decimal: decimal_hex})
    return hex_dict

if __name__ == '__main__':
    converted_dict = decimal_to_hex()
    print(converted_dict) # TODO Распечатайте словарь с десятичными и шестнадцатеричными числами


print(os.name)