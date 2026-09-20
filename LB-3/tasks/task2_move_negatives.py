"""Задание 2. Перемещение отрицательных элементов с нечётным номером в «хвост».

Условие: в одномерном списке A=(a1, a2, ..., an) все отрицательные элементы,
имеющие нечётный порядковый номер, отправить в «хвост» списка, то есть поместить
на место последних элементов. Элементы списка вводятся генератором случайных чисел.

Порядковые номера считаются с единицы, как в условии: a1 - 1-й элемент.
Перемещение выполняется устойчиво: отобранные элементы сохраняют взаимный
порядок и ставятся в конец списка сразу после оставшихся.
"""

from __future__ import annotations

import random
from typing import List, Sequence, Tuple

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import THIN_SEPARATOR, read_int, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task2_move_negatives.py
    from common import THIN_SEPARATOR, read_int, show_results, show_task_header

TITLE = "Отрицательные элементы с нечётным номером - в хвост списка"
STATEMENT = (
    "Список заполняется генератором случайных чисел.\n"
    "В списке A=(a1, a2, ..., an) все отрицательные элементы с нечётным\n"
    "порядковым номером (a1, a3, a5, ...) требуется поместить в конец списка.\n"
    "Порядковые номера считаются с единицы; порядок остальных элементов\n"
    "и взаимный порядок переносимых элементов сохраняется.\n"
    "Пример: [3, -1, -4, -6, 7] -> [3, -1, -6, 7, -4] (перенесён a3 = -4)."
)

DEFAULT_SIZE = 12
DEFAULT_MIN = -20
DEFAULT_MAX = 20


def make_list(size: int, low: int, high: int, seed: int | None = None) -> List[int]:
    """Создаёт список из `size` случайных целых чисел из диапазона [low, high]."""
    rng = random.Random(seed)
    return [rng.randint(low, high) for _ in range(size)]


def select_negative_odd(numbers: Sequence[int]) -> Tuple[List[int], List[int]]:
    """Делит список на переносимые элементы и все остальные.

    Возвращает пару (переносимые элементы, остальные элементы).
    Переносимые - отрицательные элементы на нечётных порядковых номерах.
    """
    moved: List[int] = []
    kept: List[int] = []
    for position, value in enumerate(numbers, start=1):  # нумерация с 1
        if value < 0 and position % 2 == 1:
            moved.append(value)
        else:
            kept.append(value)
    return moved, kept


def solve(numbers: Sequence[int]) -> Tuple[List[int], List[int]]:
    """Возвращает пару (исходный список, список с перенесёнными элементами)."""
    moved, kept = select_negative_odd(numbers)
    return list(numbers), kept + moved


def run() -> None:
    """Диалог с пользователем: генерация списка и вывод результата."""
    show_task_header(2, TITLE, STATEMENT)

    if _wants_input():
        size = read_int("Размер списка n: ", at_least=1)
    else:
        size = DEFAULT_SIZE

    low = DEFAULT_MIN
    high = DEFAULT_MAX
    print(f"Список из {size} чисел будет заполнен числами от {low} до {high}.")

    numbers = make_list(size, low, high)
    source, result = solve(numbers)

    print(THIN_SEPARATOR)
    print("Исходный список (позиция -> значение):")
    for position, value in enumerate(source, start=1):
        mark = " <-- отрицательное на нечётной позиции" if value < 0 and position % 2 == 1 else ""
        print(f"  a{position:<3}= {value:>4}{mark}")

    moved, kept = select_negative_odd(source)
    show_results(
        [
            ("Исходный список", source),
            ("Перенесено в хвост", moved),
            ("Осталось в начале", kept),
            ("Список после перемещения", result),
        ]
    )
    print(f"  Перенесено элементов: {len(moved)}; длина списка не изменилась: {len(result)}.")


def _wants_input() -> bool:
    """Спрашивает, задавать ли размер списка вручную; по умолчанию - нет."""
    answer = input("Задать размер списка вручную? (y/N): ").strip().lower()
    return answer in {"y", "yes", "д", "да"}


if __name__ == "__main__":
    run()