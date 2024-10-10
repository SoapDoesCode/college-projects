def addition(*numbers: int|float, precision: int = 3) -> int|float:
    total = 0
    for num in numbers:
        total += float(num)
    return round(total, precision)

def subtract_numbers(*numbers: int|float, precision: int = 3):
    total = float(numbers[0])
    for num in numbers[1:]:
        total -= float(num)
    return round(total, precision)

def multiply_numbers(*numbers: int|float, precision: int = 3) -> int|float:
    total = 1
    numbers = list(numbers)
    for num in numbers:
        total *= float(num)
    return round(total, precision)

def divide(number: int|float, divisor: int|float, precision: int = 3):
    return round((float(number)/float(divisor)), precision) # returns number divided by the divisor

def nth_root(number: int|float, degree: int, precision: int = 5) -> float:
    root = 1 / degree
    return round(number**root, precision)

def exponentiate(number: int|float, exponent: int|float, precision: int = 5) -> float:
    return round(float(number)**float(exponent), precision) # returns number to the power of exponent

def arithmetic_mean(*numbers: int|float, precision: int = 3) -> float:
    total = addition(numbers, precision=precision*2)
    output = round(total / len(numbers), precision)
    return f"{output}"

def geometric_mean(*numbers: int|float, precision: int = 3) -> float:
    total = multiply_numbers(*numbers)
    return round(nth_root(total, len(numbers), precision=precision*2), precision)

def get_highest(*numbers: int|float) -> int|float:
    highest = 0
    for num in numbers:
        highest = num if num >= highest else highest
    return highest

def pythag(side_a, side_b, precision: int = 3) -> int|float:
    a_square = exponentiate(side_a, 2, precision=precision*2) # calculates square of A
    b_square = exponentiate(side_b, 2, precision=precision*2) # calculates square of B
    c_square = a_square + b_square # A^2 + B^2
    return round(nth_root(c_square, 2, precision=precision*2), precision) # returns the root of C^2

def factorial(number: int) -> int:
    total = 1
    for num in range(2, number+1):
        total *= int(num)
    return total

def triangle_number(number: int) -> int:
    total = 0
    for num in range(1, number+1):
        total += int(num)
    return total

def get_volume(length: int|float, width: int|float, height: int|float, precision: int = 3) -> int|float:
    total = multiply_numbers(length, width, height, precision=precision*2) # multiplies the sides together with double internal precision
    return round(total, precision) # returns the total after rounding to the desired precision