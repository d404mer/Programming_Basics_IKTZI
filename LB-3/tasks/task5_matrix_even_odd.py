"""Задание 5. Подсчёт чётных и нечётных чисел в матрице.

Условие: ввести с помощью генератора случайных чисел целочисленную матрицу
размерности n x m (заданы константами). Подсчитать количество чётных и нечётных
чисел. Вывести на экран полученные значения.
"""

from __future__ import annotations

import random
from typing import Dict, List, Sequence

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import read_choice, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task5_matrix_even_odd.py
    from common import read_choice, show_results, show_task_header

TITLE = "Чётные и нечётные числа в матрице n x m"
STATEMENT = (
    "Матрица размерности n x m заполняется целыми случайными числами.\n"
    "Размерности заданы константами (их можно изменить, выбрав другой вариант).\n"
    "Требуется подсчитать количество чётных и нечётных чисел и вывести их."
)

#: Варианты размерностей матрицы (заданы константами).
ROWS = 4
COLS = 6
SIZE_PRESETS = [(4, 6), (3, 3), (5, 8)]
RANGE_PRESETS = [(0, 99), (-50, 50)]


def make_matrix(rows: int, cols: int, low: int, high: int,
                seed: int | None = None) -> List[List[int]]:
    """Создаёт матрицу rows x cols из случайных целых чисел [low, high]."""
    rng = random.Random(seed)
    return [[rng.randint(low, high) for _ in range(cols)] for _ in range(rows)]


def solve(matrix: Sequence[Sequence[int]]) -> Dict[str, object]:
    """Считает чётные, нечётные и нули в матрице.

    Ноль - чётное число, поэтому он попадает в счётчик чётных;
    отдельно считается количество нулей.
    """
    if not matrix or not matrix[0]:
        raise ValueError("матрица должна быть непустой.")

    even = 0
    odd = 0
    zeros = 0
    even_sum = 0
    odd_sum = 0
    for row in matrix:
        for value in row:
            if value % 2 == 0:
                even += 1
                even_sum += value
                if value == 0:
                    zeros += 1
            else:
                odd += 1
                odd_sum += value

    total = even + odd
    return {
        "even": even,
        "odd": odd,
        "zeros": zeros,
        "total": total,
        "even_sum": even_sum,
        "odd_sum": odd_sum,
        "even_share": even / total,
        "odd_share": odd / total,
    }


def print_matrix(matrix: Sequence[Sequence[int]]) -> None:
    """Печатает матрицу ровными столбцами."""
    width = max(len(str(value)) for row in matrix for value in row)
    for index, row in enumerate(matrix, start=1):
        cells = " ".join(str(value).rjust(width) for value in row)
        print(f"  {index:>2}| {cells}")


def run() -> None:
    """Диалог с пользователем: выбор размеров и диапазона, вывод подсчёта."""
    show_task_header(5, TITLE, STATEMENT)

    size_index = read_choice(
        "Выберите размерность матрицы (Enter - первый вариант): ",
        [f"{r} x {c}" for r, c in SIZE_PRESETS],
    )
    rows, cols = SIZE_PRESETS[size_index - 1]

    range_index = read_choice(
        "Выберите диапазон значений (Enter - первый вариант): ",
        [f"от {low} до {high}" for low, high in RANGE_PRESETS],
    )
    low, high = RANGE_PRESETS[range_index - 1]

    matrix = make_matrix(rows, cols, low, high)
    print()
    print(f"Матрица {rows} x {cols} со значениями от {low} до {high}:")
    print_matrix(matrix)
    print(f"  (константы задания: ROWS = {ROWS}, COLS = {COLS})")

    stats = solve(matrix)
    show_results(
        [
            ("Всего элементов", stats["total"]),
            ("Чётных чисел", f"{stats['even']} ({stats['even_share']:.0%})"),
            ("Нечётных чисел", f"{stats['odd']} ({stats['odd_share']:.0%})"),
            ("Из них нулей (тоже чётные)", stats["zeros"]),
            ("Сумма чётных", stats["even_sum"]),
            ("Сумма нечётных", stats["odd_sum"]),
        ]
    )
    print(f"  Проверка: {stats['even']} + {stats['odd']} = {stats['total']} "
          f"элементов матрицы.")


if __name__ == "__main__":
    run()