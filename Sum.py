def aggregate_values(*elements):
    if len(elements) < 2:
        raise ValueError("INVALID_ARGUMENTS_COUNT")

    if not all(isinstance(item, (int, float)) for item in elements):
        raise TypeError("INVALID_ARGUMENT")

    total = sum(elements)
    return total

# Примеры использования:
try:
    print(aggregate_values(1, 2, 3))  # 6
except Exception as error:
    print(f"Error: {error}")

try:
    print(aggregate_values())  # Error: INVALID_ARGUMENTS_COUNT
except Exception as error:
    print(f"Error: {error}")

try:
    print(aggregate_values(0, 1, '1', 2))  # Error: INVALID_ARGUMENT
except Exception as error:
    print(f"Error: {error}")
