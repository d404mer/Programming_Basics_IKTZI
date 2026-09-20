"""Задание 6. Поиск наибольшего числа в трёхмерном массиве.

Условие: массив T имеет размерность 3x5x7. Найти наибольшее содержащееся
в нём число и вывести его и его индексы на экран.
"""

from __future__ import annotations

import random
from typing import Dict, List, Sequence, Tuple

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import show_results, show_task_header
except ImportError:  # прямой запуск файла: python task6_3d_max.py
    from common import show_results, show_task_header

TITLE = "Наибольшее число в трёхмерном массиве 3 x 5 x 7"
STATEMENT = (
    "Массив T размерности 3 x 5 x 7 (то есть 3 слоя, в каждом 5 строк по 7 чисел)\n"
    "заполняется целыми случайными числами.\n"
    "Требуется найти наибольшее число и вывести его вместе с индексами\n"
    "по всем трём измерениям."
)

#: Размерности массива заданы условием задачи.
DIM1, DIM2, DIM3 = 3, 5, 7
RANGE_PRESETS = [(0, 99), (-50, 50), (1, 1000)]


def make_array(dim1: int, dim2: int, dim3: int,
               low: int, high: int, seed: int | None = None) -> List[List[List[int]]]:
    """Создаёт трёхмерный массив dim1 x dim2 x dim3 из случайных чисел."""
    rng = random.Random(seed)
    return [
        [[rng.randint(low, high) for _ in range(dim3)] for _ in range(dim2)]
        for _ in range(dim1)
    ]


def find_max(array: Sequence[Sequence[Sequence[int]]]) -> Tuple[int, Tuple[int, int, int]]:
    """Возвращает пару (наибольшее значение, индексы (i, j, k)).

    Перебор идёт по всем элементам, поэтому находятся все позиции максимума;
    возвращается первая из них.
    """
    if not array or not array[0] or not array[0][0]:
        raise ValueError("массив должен быть непустым.")

    best_value = array[0][0][0]
    best_index = (0, 0, 0)
    for i, layer in enumerate(array):
        for j, row in enumerate(layer):
            for k, value in enumerate(row):
                if value > best_value:
                    best_value = value
                    best_index = (i, j, k)
    return best_value, best_index


def all_max_positions(array: Sequence[Sequence[Sequence[int]]],
                      best_value: int) -> List[Tuple[int, int, int]]:
    """Возвращает список всех позиций, где встречается наибольшее значение."""
    positions: List[Tuple[int, int, int]] = []
    for i, layer in enumerate(array):
        for j, row in enumerate(layer):
            for k, value in enumerate(row):
                if value == best_value:
                    positions.append((i, j, k))
    return positions


def iter_elements(array: Sequence[Sequence[Sequence[int]]]):
    """Последовательно выдаёт все элементы трёхмерного массива."""
    for layer in array:
        for row in layer:
            for value in row:
                yield value


def solve(array: Sequence[Sequence[Sequence[int]]]) -> Dict[str, object]:
    """Возвращает максимум, его индексы и общее число элементов."""
    best_value, best_index = find_max(array)
    return {
        "value": best_value,
        "index": best_index,
        "positions": all_max_positions(array, best_value),
        "count": sum(1 for _ in iter_elements(array)),
        "total": sum(iter_elements(array)),
        "minimum": min(iter_elements(array)),
    }


def run() -> None:
    """Диалог с пользователем: генерация массива и поиск максимума."""
    show_task_header(6, TITLE, STATEMENT)

    print("Варианты диапазона значений:")
    for index, (low, high) in enumerate(RANGE_PRESETS, start=1):
        print(f"  {index}. от {low} до {high}")
    answer = input("Выберите вариант (Enter - первый): ").strip()
    if answer.isdigit() and 1 <= int(answer) <= len(RANGE_PRESETS):
        low, high = RANGE_PRESETS[int(answer) - 1]
    else:
        low, high = RANGE_PRESETS[0]
        if answer:
            print("      Примечание: неверный номер варианта, выбран первый диапазон.")

    array = make_array(DIM1, DIM2, DIM3, low, high)
    print(f"\nМассив T[{DIM1}][{DIM2}][{DIM3}] со значениями от {low} до {high}:")
    for i, layer in enumerate(array, start=1):
        print(f"  Слой {i}:")
        width = max(len(str(value)) for row in layer for value in row)
        for j, row in enumerate(layer, start=1):
            cells = " ".join(str(value).rjust(width) for value in row)
            print(f"    строка {j}| {cells}")

    stats = solve(array)
    i, j, k = stats["index"]
    show_results(
        [
            ("Наибольшее число", stats["value"]),
            ("Индексы (слой, строка, столбец)", f"({i}, {j}, {k})"),
            ("Индексы с нумерацией от 1", f"({i + 1}, {j + 1}, {k + 1})"),
            ("Всего элементов", stats["count"]),
            ("Наименьшее число", stats["minimum"]),
            ("Сумма всех элементов", stats["total"]),
        ]
    )
    if len(stats["positions"]) > 1:
        print(f"  Наибольшее значение встречается {len(stats['positions'])} раз(а): "
              f"{stats['positions']}")


if __name__ == "__main__":
    run()