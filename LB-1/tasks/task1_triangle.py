"""Задание 1. Гипотенуза и периметр прямоугольного треугольника.

Условие: даны катеты a и b прямоугольного треугольника.
Найти его гипотенузу c и периметр P.
"""

from __future__ import annotations

import math

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import fmt, read_float, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task1_triangle.py
    from common import fmt, read_float, show_results, show_task_header

TITLE = "Прямоугольный треугольник: гипотенуза и периметр"
STATEMENT = (
    "Даны катеты a и b прямоугольного треугольника.\n"
    "Найти гипотенузу c и периметр P.\n"
    "Формулы: c = sqrt(a^2 + b^2),  P = a + b + c."
)


def solve(a: float, b: float) -> tuple:
    """Возвращает пару (гипотенуза, периметр) для катетов a и b."""
    c = math.sqrt(a * a + b * b)
    p = a + b + c
    return c, p


def run() -> None:
    """Диалог с пользователем: ввод катетов и вывод результата."""
    show_task_header(1, TITLE, STATEMENT)
    a = read_float("Введите катет a (a > 0): ", greater_than=0)
    b = read_float("Введите катет b (b > 0): ", greater_than=0)

    c, p = solve(a, b)
    show_results(
        [
            ("Гипотенуза c", fmt(c)),
            ("Периметр P", fmt(p)),
        ]
    )


if __name__ == "__main__":
    run()
