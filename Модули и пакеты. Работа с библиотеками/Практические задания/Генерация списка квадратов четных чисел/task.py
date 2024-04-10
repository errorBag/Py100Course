def generate_even_squares(n):
    generate_even_squares = [n*n for n in range(n+1) if n % 2 == 0]
    return generate_even_squares
    # even_squares = []
    # for i in range(n+1):
    #     if i % 2 == 0:
    #         even_squares.append(i**2)
    # return even_squares


if __name__ == '__main__':
    # Проверка работы функции
    print(generate_even_squares(5))  # [0, 4, 16]
    print(generate_even_squares(10))  # [0, 4, 16, 36, 64, 100]
    print(generate_even_squares(0))  # [0]
