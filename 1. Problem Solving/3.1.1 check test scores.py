import os, sys
from getpass import getpass as prompt

from test_scores_utils import addition, subtract_numbers, multiply_numbers, divide, exponentiate, factorial

sys.set_int_max_str_digits(0)

def clear():
    os.system("cls")
    
def is_number(value):
    try:
        float(value)
        return True
    except:
        return False

while True:
    
    try:
        numbers = input("Numbers: ").split(", ")
        
        if all(is_number(num) for num in numbers):
            pass
        else:
            raise ValueError
        
        operator = input("Do you wish to add, subtract, multiply, divide or exponentiate them?\nOperator: ")
        
        match operator.lower():
            case "+" | "add" | "addition" | "plus":
                answer = addition(*numbers)
            case "-" | "sub" | "subtract" | "minus":
                answer = subtract_numbers(*numbers)
            case "*" | "mul" | "multiply" | "multiplication":
                answer = multiply_numbers(*numbers)
            case "/" | "div" | "divide" | "division":
                answer = divide(numbers[0], numbers[1])
            case "**" | "^" | "power" | "expoent"| "exponentiation":
                exponent = float(input("What should the exponent be?\nExponent: "))
                answer = exponentiate(*numbers, exponent)
            case "!" | "factorial":
                print("Working on it... This may take a while...")
                answer = factorial(int(numbers[0]))
            case _:
                answer = "Invalid operator, please try again!"
    except ZeroDivisionError:
        answer = "You must not divide by zero"
    except IndexError:
        answer = "Please input more than one number"
    except ValueError:
        answer = "Invalid input, please input a number"
    except EOFError:
        answer = "Please don't press that..."
    except KeyboardInterrupt:
        clear()
        print("Exiting calculator with no errors!")
        exit(0)
    except OverflowError:
        answer = "What the hell did you do that answer was way too big!"
    except MemoryError:
        answer = "Out of memory error! What did you do..."
    
    try:
        if isinstance(answer, (int, float)):
            print(f"The answer is: {answer}")
        else:
            print(answer)
    except ValueError:
        print("Oops! The length of the output was too long...")

    prompt(prompt="Press any key to continue...")
    clear()