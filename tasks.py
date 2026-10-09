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


def get_primes_up_to_100() -> list[int]:
    """Генерирует список простых чисел в диапазоне от 2 до 100 (Средняя сложность № 5)."""
    primes: list[int] = []
    for num in range(2, 101):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def find_min_element(numbers: list[int | float]) -> int | float:
    """Находит минимальный элемент переданного числового списка (Средняя сложность № 9)."""
    if not numbers:
        raise ValueError("Список не должен быть пустым.")
    min_val = numbers[0]
    for item in numbers[1:]:
        if item < min_val:
            min_val = item
    return min_val

def generate_fibonacci(count: int) -> list[int]:
    """Генерирует последовательность Фибоначчи заданной длины count (Повышенная сложность № 3)."""
    if not isinstance(count, int):
        raise TypeError("Количество элементов должно быть целым числом.")
    if count <= 0:
        return []
    if count == 1:
        return [0]
    sequence = [0, 1]
    for _ in range(2, count):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence