from replit import clear
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)
operators = ['+', '-', '*', '/', '%']

def input_number(text):
    while True:
        number = input(text)
        try:
            val = int(number)
            return number
        except ValueError:
            print("That's not an integer! Please try again.")


def input_operator():
    op = input(f"Pick up an operator from this: {operators}\n")
    while op not in operators:
        op = input(f"Pick up an operator from this: {operators} \n")
    return op

def input_repeat():
    repeat = input(
        "Do you want to continue this operaton. Type y to continue or n to next calculation or e to exit ?: \n").lower()
    while repeat not in ['y', 'n', 'e']:
        repeat = input(
            "Invalid input. Type y to continue or n to next calculation or e to exit ?: \n").lower()
    return repeat


def calculate(operand1, op, operand2):
    try:
        result = eval(operand1+op+operand2)
        print(result)
        return result
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def repeat_operation(result, op):
    while True:
        op = input_operator()
        next_number = input_number("What`s the second number?: \n")
        result = calculate(str(result), op, next_number)
        if result is None:
            continue
        repeat = input_repeat()
        if repeat != 'y':
            clear()
            break
    return result

while True:
    operand1 = input_number("What`s the first number?: \n")
    op = input_operator()
    operand2 = input_number("What`s the second number?: \n")
    result = calculate(operand1, op, operand2)
    if result is None:
        continue
    repeat = input_repeat()
    if repeat == 'y':
        result = repeat_operation(result, op)
    elif repeat == 'n':
        clear()
    else:
        clear()
        break
