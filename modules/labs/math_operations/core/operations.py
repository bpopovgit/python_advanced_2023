def sum_nums(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        num1 / num2
    except ZeroDivisionError:
        return None


def power(num1, num2):
    return num1 ** num2
