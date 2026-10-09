from tasks import (
    count_word_frequencies,
    factorial,
    find_min_element,
    generate_fibonacci,
    get_primes_up_to_100,
)


def main() -> None:
    print("=== Лабораторная работа № 2 (Вариант 3) ===")

    # 1. Факториал числа (Средняя сложность № 3)
    num = 6
    print(f"[Средняя № 3] {num}! = {factorial(num)}")

    # 2. Простые числа до 100 (Средняя сложность № 5)
    primes = get_primes_up_to_100()
    print(f"[Средняя № 5] Простые числа до 100 ({len(primes)} шт.): {primes}")

    # 3. Минимальный элемент списка (Средняя сложность № 9)
    sample_list = [42, -18, 95, 3.14, 0, -27.5, 104]
    print(f"[Средняя № 9] Минимум в {sample_list} = {find_min_element(sample_list)}")

    # 4. Список Фибоначчи (Повышенная сложность № 3)
    fib_count = 10
    print(f"[Повышенная № 3] Первые {fib_count} чисел Фибоначчи: {generate_fibonacci(fib_count)}")

    # 5. Частота слов из файла (Повышенная сложность № 7)
    word_freq = count_word_frequencies("data.txt")
    print("[Повышенная № 7] Анализ слов в data.txt (топ-5):")
    for word, count in sorted(word_freq.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"  - '{word}': {count}")


if __name__ == "__main__":
    main()