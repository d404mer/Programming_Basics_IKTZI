"""Задание 6. Число, прочитанное справа налево.

Условие: дано трёхзначное число. Вывести число, полученное при прочтении
исходного числа справа налево.
"""

from __future__ import annotations

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import digits_of, read_int, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task6_reverse.py
    from common import digits_of, read_int, show_results, show_task_header

TITLE = "Число, прочитанное справа налево (перевёртыш)"
STATEMENT = (
    "Дано трёхзначное число (от 100 до 999).\n"
    "Вывести число, полученное при прочтении исходного числа справа налево.\n"
    "Пример: 123 -> 321."
)


def solve(number: int) -> int:
    """Возвращает число, записанное цифрами `number` в обратном порядке."""
    reversed_digits = digits_of(number)[::-1]
    result = 0
    for digit in reversed_digits:
        result = result * 10 + digit
    return result


def run() -> None:
    """Диалог с пользователем: ввод числа и вывод результата."""
    show_task_header(6, TITLE, STATEMENT)
    number = read_int("Введите трёхзначное число (от 100 до 999): ", at_least=100, at_most=999)

    reversed_number = solve(number)
    lines = [
        ("Исходное число", number),
        ("Число справа налево", reversed_number),
    ]
    if str(reversed_number) != str(number)[::-1]:
        # Например, 120 -> "021": ведущий ноль не входит в запись числа.
        lines.append(("Его запись строкой", str(number)[::-1]))
    show_results(lines)


if __name__ == "__main__":
    run()
