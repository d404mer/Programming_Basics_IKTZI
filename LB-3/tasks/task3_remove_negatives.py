"""Задание 3. Удаление отрицательных элементов, расположенных между положительными.

Условие: в одномерном списке A=(a1, a2, ..., an) удалить все отрицательные
элементы, расположенные между положительными. Элементы списка вводятся
генератором случайных чисел.
"""

from __future__ import annotations

import random
from typing import List, Sequence, Tuple

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import THIN_SEPARATOR, read_int, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task3_remove_negatives.py
    from common import THIN_SEPARATOR, read_int, show_results, show_task_header

TITLE = "Удаление отрицательных элементов между положительными"
STATEMENT = (
    "Список заполняется генератором случайных чисел.\n"
    "Требуется удалить все отрицательные элементы, расположенные между\n"
    "положительными, то есть отрицательные элементы, у которых есть\n"
    "положительный сосед и слева, и справа (например, ... 5, -3, 8 ...).\n"
    "Нули не считаются положительными, поэтому такие элементы сохраняются.\n"
    "Пример: [1, -1, 2, -2, -3, 3] -> [1, 2, -2, -3, 3] (удалён только -1)."
)

DEFAULT_SIZE = 15
DEFAULT_MIN = -10
DEFAULT_MAX = 10


def make_list(size: int, low: int, high: int, seed: int | None = None) -> List[int]:
    """Создаёт список из `size` случайных целых чисел из диапазона [low, high]."""
    rng = random.Random(seed)
    return [rng.randint(low, high) for _ in range(size)]


def solve(numbers: Sequence[int]) -> Tuple[List[int], List[int]]:
    """Удаляет отрицательные элементы между положительными.

    Возвращает пару (список после удаления, удалённые элементы).
    Элемент удаляется, если он отрицателен и имеет положительный сосед
    слева и справа.
    """
    if len(numbers) < 3:
        return list(numbers), []

    removed: List[int] = []
    result: List[int] = []
    for index, value in enumerate(numbers):
        has_left_positive = index > 0 and numbers[index - 1] > 0
        has_right_positive = index + 1 < len(numbers) and numbers[index + 1] > 0
        if value < 0 and has_left_positive and has_right_positive:
            removed.append(value)
        else:
            result.append(value)
    return result, removed


def run() -> None:
    """Диалог с пользователем: генерация списка и вывод результата."""
    show_task_header(3, TITLE, STATEMENT)

    if _wants_input():
        size = read_int("Размер списка n: ", at_least=1)
    else:
        size = DEFAULT_SIZE

    low = DEFAULT_MIN
    high = DEFAULT_MAX
    print(f"Список из {size} чисел будет заполнен числами от {low} до {high}.")

    numbers = make_list(size, low, high)
    result, removed = solve(numbers)

    print(THIN_SEPARATOR)
    print("Исходный список с пометками:")
    for index, value in enumerate(numbers):
        has_left_positive = index > 0 and numbers[index - 1] > 0
        has_right_positive = index + 1 < len(numbers) and numbers[index + 1] > 0
        mark = " <-- удаляется" if value < 0 and has_left_positive and has_right_positive else ""
        print(f"  [{index:>2}] = {value:>4}{mark}")

    show_results(
        [
            ("Исходный список", list(numbers)),
            ("Удалённые элементы", removed),
            ("Список после удаления", result),
            ("Было / стало элементов", f"{len(numbers)} / {len(result)}"),
        ]
    )


def _wants_input() -> bool:
    """Спрашивает, задавать ли размер списка вручную; по умолчанию - нет."""
    answer = input("Задать размер списка вручную? (y/N): ").strip().lower()
    return answer in {"y", "yes", "д", "да"}


if __name__ == "__main__":
    run()