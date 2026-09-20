"""Пакет с заданиями лабораторной работы №1.

Каждое задание находится в отдельном файле task<N>_*.py и предоставляет:
  TITLE     - короткое название для меню;
  STATEMENT - текст условия и используемые формулы;
  solve()   - расчётная функция (без ввода-вывода, её удобно проверять);
  run()     - диалог с пользователем.
"""

from __future__ import annotations

from typing import List

from . import (
    task1_triangle,
    task2_circles,
    task3_candies,
    task4_segments,
    task5_digits_sum,
    task6_reverse,
    task7_shift_first_digit,
)
from .common import TaskItem

#: Список заданий для меню: (номер, название, функция запуска).
TASKS: List[TaskItem] = [
    (1, task1_triangle.TITLE, task1_triangle.run),
    (2, task2_circles.TITLE, task2_circles.run),
    (3, task3_candies.TITLE, task3_candies.run),
    (4, task4_segments.TITLE, task4_segments.run),
    (5, task5_digits_sum.TITLE, task5_digits_sum.run),
    (6, task6_reverse.TITLE, task6_reverse.run),
    (7, task7_shift_first_digit.TITLE, task7_shift_first_digit.run),
]

__all__ = ["TASKS", "TaskItem"]
