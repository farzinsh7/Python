# to see Problems : CTRL + SHIFT + M
# T see Command Pallete : CTRL + SHIFT + P
# to run in terminal : CTRL + ALT + N
# Built in functions: https://docs.python.org/3/library/functions.html
# Math funvtion: https://docs.python.org/3/library/math.html


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return'FizzBuzz'
    if input % 3 == 0:
        return'Fizz'
    if input % 5 == 0:
        return'Buzz'
    return input


print(fizz_buzz(15))
