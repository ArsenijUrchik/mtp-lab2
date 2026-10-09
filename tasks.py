def factorial(n: int) -> int:
    """Вычисляет факториал целого неотрицательного числа n (Средняя сложность № 3)."""
    if not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом.")
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
