class ExpressionCalculator:
    def __init__(self):
        self.operator_functions = {}

    def register_operation(self, symbol, operation):
        if not isinstance(symbol, str) or not callable(operation):
            raise TypeError("INVALID_ARGUMENT")
        self.operator_functions[symbol] = operation

    def evaluate(self, expression):
        if not isinstance(expression, str):
            raise TypeError("INVALID_ARGUMENT")

        try:
            left_operand, operator, right_operand = expression.split()
            left_operand = float(left_operand)
            right_operand = float(right_operand)
        except ValueError:
            raise ValueError("INVALID_OPERAND")

        if operator not in self.operator_functions:
            raise ValueError("UNKNOWN_OPERATION")

        return self.operator_functions[operator](left_operand, right_operand)

# Пример использования
calc = ExpressionCalculator()

# Регистрируем операции
calc.register_operation("+", lambda a, b: a + b)
calc.register_operation("*", lambda a, b: a * b)
calc.register_operation("/", lambda a, b: a / b)
calc.register_operation("**", lambda a, b: a ** b)

# Выполняем вычисления
try:
    print(calc.evaluate("2 ** 3"))  # 8.0
    print(calc.evaluate("2 + 3"))   # 5.0
    print(calc.evaluate("3 * 5"))   # 15.0
    print(calc.evaluate("10 / 2"))  # 5.0
    print(calc.evaluate("h - 10"))  # Error: INVALID_OPERAND
except Exception as e:
    print(f"Error: {e}")

# Примеры ошибок
try:
    calc.register_operation(1, lambda a, b: a + b)  # Error: INVALID_ARGUMENT
except Exception as e:
    print(f"Error: {e}")

try:
    calc.register_operation("+", 10)  # Error: INVALID_ARGUMENT
except Exception as e:
    print(f"Error: {e}")

try:
    print(calc.evaluate(1 + 3))  # Error: INVALID_ARGUMENT
except Exception as e:
    print(f"Error: {e}")

try:
    print(calc.evaluate("3 - 5"))  # Error: UNKNOWN_OPERATION
except Exception as e:
    print(f"Error: {e}")
