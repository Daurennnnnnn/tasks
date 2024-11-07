def sum_args(*args):
    # Проверка на количество аргументов
    if len(args) < 2:
        raise ValueError('INVALID_ARGUMENTS_COUNT')

    # Проверка на тип аргументов
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError('INVALID_ARGUMENT')

    # Суммирование аргументов
    return sum(args)

# Примеры
try:
    print(sum_args(1, 2, 3))  # 6
except (ValueError, TypeError) as e:
    print(e)

try:
    print(sum_args())  # error INVALID_ARGUMENTS_COUNT
except (ValueError, TypeError) as e:
    print(e)

try:
    print(sum_args(0, 1, '1', 2))  # error INVALID_ARGUMENT
except (ValueError, TypeError) as e:
    print(e)