def functiondic(numbers):
    even_number = []

    for number in numbers:
        if number % 2 == 0:
            even_number.append(number)

    return even_number

numbers1 = [2, 3, 6, 8, 13, 45, 67, 88, 99, 100]
print(functiondic(numbers1))