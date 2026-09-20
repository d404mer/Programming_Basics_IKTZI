"""Задание 7. Перенос первой цифры трёхзначного числа в конец.

Условие: дано трёхзначное число. В нём зачеркнули первую слева цифру
и приписали её справа. Вывести полученное число.
"""

from __future__ import annotations

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import read_int, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task7_shift_first_digit.py
    from common import read_int, show_results, show_task_header

TITLE = "Первую цифру числа зачеркнули и приписали справа"
STATEMENT = (
    "Дано трёхзначное число (от 100 до 999).\n"
    "В нём зачеркнули первую слева цифру и приписали её справа.\n"
    "Вывести полученное число.\n"
    "Формула: (n % 100) * 10 + n // 100.\n"
    "Пример: 123 -> 231."
)


def solve(number: int) -> int:
    """Возвращает число, полученное переносом первой цифры в конец."""
    first_digit = number // 100
    last_two_digits = number % 100
    return last_two_digits * 10 + first_digit


def run() -> None:
    """Диалог с пользователем: ввод числа и вывод результата."""
    show_task_header(7, TITLE, STATEMENT)
    number = read_int("Введите трёхзначное число (от 100 до 999): ", at_least=100, at_most=999)

    result = solve(number)
    show_results(
        [
            ("Исходное число", number),
            ("Первая цифра", number // 100),
            ("Две последние цифры", number % 100),
            ("Полученное число", result),
        ]
    )
    if result < 100:
        # Например, 907 -> "079": ведущий ноль не входит в запись числа.
        print(f"  В трёхзначной записи это {result:03d} (ведущий ноль отбрасывается).")


if __name__ == "__main__":
    run()
