# TODO Напишите функцию `is_palindrome`

def is_palindrome(line):
    list_ = line.lower().split()
    list_2 = ''.join(list_)
    list_backwards = list_2[::-1]

    if list_2 == list_backwards:
        return True
    return False


is_palindrome('Ты милок иди яром у дороги мина за дорогой огород а за ним и город у моря иди коли мыт')