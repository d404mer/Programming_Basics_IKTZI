"""Задание 5. Сумма и произведение цифр трёхзначного числа.

Условие: дано трёхзначное число. Найти сумму и произведение его цифр.
"""

from __future__ import annotations

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import digits_of, read_int, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task5_digits_sum.py
    from common import digits_of, read_int, show_results, show_task_header

TITLE = "Сумма и произведение цифр трёхзначного числа"
STATEMENT = (
    "Дано трёхзначное число (от 100 до 999).\n"
    "Найти сумму и произведение его цифр.\n"
    "Цифры выделяются так: сотни = n // 100,\n"
    "десятки = n // 10 % 10, единицы = n % 10."
)


def solve(number: int) -> tuple:
    """Возвращает тройку (цифры числа, сумма цифр, произведение цифр)."""
    digits = digits_of(number)
    total = sum(digits)
    product = 1
    for digit in digits:
        product *= digit
    return digits, total, product


def run() -> None:
    """Диалог с пользователем: ввод числа и вывод результата."""
    show_task_header(5, TITLE, STATEMENT)
    number = read_int("Введите трёхзначное число (от 100 до 999): ", at_least=100, at_most=999)

    digits, total, product = solve(number)
    show_results(
        [
            ("Цифры числа", ", ".join(str(d) for d in digits)),
            ("Сумма цифр", total),
            ("Произведение цифр", product),
        ]
    )


if __name__ == "__main__":
    run()
