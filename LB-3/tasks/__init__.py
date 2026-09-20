"""Пакет с заданиями лабораторной работы №3.

Каждое задание находится в отдельном файле task<N>_*.py и предоставляет:
  TITLE     - короткое название для меню;
  STATEMENT - текст условия и используемые формулы;
  TASK      - постановка задачи из методички, если она нужна для сверки;
  solve()   - расчётная функция (без ввода-вывода, её удобно проверять);
  run()     - диалог с пользователем.
"""

from __future__ import annotations

from typing import List

from . import (
    task1_words_length,
    task2_move_negatives,
    task3_remove_negatives,
    task4_sieve,
    task5_matrix_even_odd,
    task6_3d_max,
)
from .common import TaskItem

#: Список заданий для меню: (номер, название, функция запуска).
TASKS: List[TaskItem] = [
    (1, task1_words_length.TITLE, task1_words_length.run),
    (2, task2_move_negatives.TITLE, task2_move_negatives.run),
    (3, task3_remove_negatives.TITLE, task3_remove_negatives.run),
    (4, task4_sieve.TITLE, task4_sieve.run),
    (5, task5_matrix_even_odd.TITLE, task5_matrix_even_odd.run),
    (6, task6_3d_max.TITLE, task6_3d_max.run),
]

__all__ = ["TASKS", "TaskItem"]