class InvalidArgumentError(Exception):
    pass

class InvalidOperandError(Exception):
    pass

class UnknownOperationError(Exception):
    pass

class Calculator:
    def __init__(self):
        self.operations = {}

    def add_method(self, operation, func):
        if not isinstance(operation, str) or not callable(func):
            raise InvalidArgumentError('INVALID_ARGUMENT')
        self.operations[operation] = func

    def calculate(self, expression):
        if not isinstance(expression, str):
            raise InvalidArgumentError('INVALID_ARGUMENT')

        try:
            a, operator, b = expression.split()
            a = float(a)
            b = float(b)
        except ValueError:
            raise InvalidOperandError('INVALID_OPERAND')

        if operator not in self.operations:
            raise UnknownOperationError('UNKNOWN_OPERATION')

        return self.operations[operator](a, b)

# Пример использования
calc = Calculator()

try:
    calc.add_method('+', lambda a, b: a + b)
    calc.add_method('*', lambda a, b: a * b)
    calc.add_method('/', lambda a, b: a / b)
    calc.add_method('**', lambda a, b: a ** b)

    print(calc.calculate("2 ** 3"))  # 8
    print(calc.calculate("2 + 3"))   # 5
    print(calc.calculate("2 * 3"))   # 6
    print(calc.calculate("2 / 3"))   # 0.6666666666666666

    calc.add_method(1, lambda a, b: a + b)  # error INVALID_ARGUMENT
except InvalidArgumentError as e:
    print(e)

try:
    calc.add_method('+', 10)  # error INVALID_ARGUMENT
except InvalidArgumentError as e:
    print(e)

try:
    print(calc.calculate('h - 10'))  # error INVALID_OPERAND
except InvalidOperandError as e:
    print(e)

try:
    print(calc.calculate('3 * 5'))  # 15 (теперь операция * добавлена)
except UnknownOperationError as e:
    print(e)

try:
    print(calc.calculate(1 + 3))  # error INVALID_ARGUMENT
except InvalidArgumentError as e:
    print(e)
