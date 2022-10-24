# Опишите функцию, которая вычисляет сумму цифр заданного числа.

# CYCLE

# def find_sum(number):
#     s = 0
#     while number != 0:
#         sum = s + number % 10
#         number = number // 10
#     return s
#
#
# def main():
#     number = int(input("Input your number: "))
#     result = find_sum(number)
#     msg = f"Digit's summa [{number}] is {result}."
#     print(msg)
#
#
# main()


# RECURSION

def find_sum(number):
    if number < 10:
        return number
    else:
        return find_sum(number % 10) + find_sum(number // 10)


def main():
    number = int(input("Input your number: "))
    result = find_sum(number)
    msg = f"Digit's summa [{number}] is {result}."
    print(msg)


main()
