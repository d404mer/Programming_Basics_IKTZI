"""Пакет с заданиями лабораторной работы №2.

Каждое задание находится в отдельном файле task<N>_*.py и предоставляет:
  TITLE     - короткое название для меню;
  STATEMENT - текст условия и используемые формулы;
  TASK      - постановка задачи из методички, если она нужна для сверки;
  solve()   - расчётная функция (без ввода-вывода, её удобно проверять);
  run()     - диалог с пользователем.
"""

from __future__ import annotations

from typing import List

from . import task1_series, task2_middle_char, task3_list_stats
from .common import TaskItem

#: Список заданий для меню: (номер, название, функция запуска).
TASKS: List[TaskItem] = [
    (1, task1_series.TITLE, task1_series.run),
    (2, task2_middle_char.TITLE, task2_middle_char.run),
    (3, task3_list_stats.TITLE, task3_list_stats.run),
]

__all__ = ["TASKS", "TaskItem"]