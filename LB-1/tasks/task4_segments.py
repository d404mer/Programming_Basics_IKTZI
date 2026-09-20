"""Задание 4. Размещение отрезков длины B на отрезке длины A.

Условие: даны целые положительные числа A и B (A > B). На отрезке длины A
размещено максимально возможное количество отрезков длины B (без наложений).
Используя операцию деления нацело, найти количество отрезков B,
размещённых на отрезке A.
"""

from __future__ import annotations

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import read_int, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task4_segments.py
    from common import read_int, show_results, show_task_header

TITLE = "Сколько отрезков длины B помещается на отрезке длины A"
STATEMENT = (
    "Даны целые положительные числа A и B, причём A > B.\n"
    "Найти количество отрезков длины B, которые помещаются на отрезке длины A.\n"
    "Формула: k = A // B (деление нацело)."
)


def solve(a: int, b: int) -> tuple:
    """Возвращает пару (количество отрезков, длина незанятой части)."""
    return a // b, a % b


def run() -> None:
    """Диалог с пользователем: ввод длин и вывод результата."""
    show_task_header(4, TITLE, STATEMENT)
    a = read_int("Введите длину отрезка A (целое, A > 0): ", at_least=1)
    # at_most = a - 1 обеспечивает выполнение условия A > B.
    b = read_int(f"Введите длину отрезка B (целое, 0 < B < {a}): ", at_least=1, at_most=a - 1)

    count, rest = solve(a, b)
    show_results(
        [
            (f"Количество отрезков: {a} // {b}", f"{count} шт."),
            (f"Остаток: {a} % {b}", rest),
        ]
    )
    print(f"  На отрезке длины {a} помещается {count} отрезк(ов) длины {b},")
    print(f"  свободной остаётся часть длины {rest}.")


if __name__ == "__main__":
    run()
