"""
Calculator library containing basic math operations.
"""


def calculate(op, number1, number2):
    if op == "ADD":
        return int(number1) + int(number2)
    if op == "SUBTRACT":
        return int(number1) - int(number2)
