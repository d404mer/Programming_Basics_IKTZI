"""Задание 4. Решето Эратосфена и числа, кратные семи.

Условие: описан алгоритм «решето Эратосфена» (шаги 1-5).
Требуется вычислить все числа от 1 до n, кратные 7;
для выполнения задания использовать списки и множества.
"""

from __future__ import annotations

from typing import Dict, List, Sequence

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import read_int, show_numbered_items, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task4_sieve.py
    from common import read_int, show_numbered_items, show_results, show_task_header

TITLE = "Решето Эратосфена и числа, кратные 7"
STATEMENT = (
    "Алгоритм «решето Эратосфена» находит все простые числа до n:\n"
    "  1) выписать числа от 2 до n;\n"
    "  2) p = 2 - первое простое число;\n"
    "  3) зачеркнуть кратные p, начиная с 2p;\n"
    "  4) найти первое незачёркнутое число, большее p, и сделать его новым p;\n"
    "  5) повторять шаги 3-4, пока это возможно.\n"
    "По условию задания требуется также вычислить все числа от 1 до n,\n"
    "кратные 7. Решето реализовано на списке, отбор простых чисел - через\n"
    "множество, кратные семи - тоже через множество."
)

DEFAULT_N = 100
#: Делитель, по которому отбираются числа в основной части задания.
DIVISOR = 7


def sieve(n: int) -> List[bool]:
    """Решето Эратосфена: возвращает список флагов простоты для чисел 0..n."""
    if n < 2:
        return [False] * (n + 1)

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2  # шаг 2: первое простое число
    while p * p <= n:
        # шаг 3: зачёркиваем кратные p, начиная с 2p
        for multiple in range(2 * p, n + 1, p):
            is_prime[multiple] = False
        # шаг 4: новое p - первое незачёркнутое число, большее p
        p += 1
        while p <= n and not is_prime[p]:
            p += 1
    return is_prime


def primes_up_to(n: int) -> List[int]:
    """Список простых чисел от 2 до n (через решето)."""
    return [number for number, prime in enumerate(sieve(n)) if prime]


def multiples_of(n: int, divisor: int) -> List[int]:
    """Числа от 1 до n, кратные divisor, полученные как множество."""
    # Множество заодно убирает любые повторы в наборе чисел.
    return sorted({number for number in range(divisor, n + 1, divisor)})


def solve(n: int) -> Dict[str, object]:
    """Возвращает простые числа до n и числа, кратные 7."""
    primes = primes_up_to(n)
    multiples = multiples_of(n, DIVISOR)
    return {
        "primes": primes,
        "prime_set": set(primes),
        "multiples": multiples,
        "multiples_set": set(multiples),
    }


def _format_numbers(numbers: Sequence[int], limit: int = 40) -> str:
    """Печатает не больше `limit` чисел, иначе - сокращает с многоточием."""
    shown = list(numbers[:limit])
    text = ", ".join(str(value) for value in shown)
    if len(numbers) > limit:
        text += f", ... (всего {len(numbers)})"
    return text


def run() -> None:
    """Диалог с пользователем: ввод n и вывод результатов."""
    show_task_header(4, TITLE, STATEMENT)
    n = read_int(f"Введите n (например {DEFAULT_N}): ", at_least=1)

    result = solve(n)
    primes = result["primes"]
    multiples = result["multiples"]

    show_results(
        [
            ("Простых чисел от 2 до n", len(primes)),
            ("Простые числа", _format_numbers(primes, 25)),
            (f"Чисел кратных {DIVISOR} от 1 до n", len(multiples)),
            (f"Числа, кратные {DIVISOR}", _format_numbers(multiples)),
        ]
    )
    if n >= DIVISOR:
        print(f"  Наибольшее число, кратное {DIVISOR}: {multiples[-1]}.")
    else:
        print(f"  Среди чисел от 1 до {n} нет чисел, кратных {DIVISOR}.")
    print(f"  Число {DIVISOR} простое: {DIVISOR in result['prime_set']}.")

    # Небольшая проверка: множество простых и множество кратных семи не должны
    # пересекаться, кроме самого числа 7.
    common = result["prime_set"] & result["multiples_set"]
    show_numbered_items(
        "Проверка через множества",
        [
            f"Мощность множества простых чисел: {len(result['prime_set'])}",
            f"Мощность множества чисел, кратных {DIVISOR}: {len(result['multiples_set'])}",
            f"Общие элементы: {sorted(common) if common else 'нет'}",
        ],
    )


if __name__ == "__main__":
    run()