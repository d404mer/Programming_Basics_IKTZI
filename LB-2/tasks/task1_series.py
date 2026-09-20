"""Задание 1 (вариант 10, п. 4). Сумма членов функционального ряда.

Ряд: y(x) = -pi/2 + sum(n=0..inf) (-1)^(n+1) / ((2n+1) * x^(2n+1))
         = -pi/2 - 1/x + 1/(3x^3) - 1/(5x^5) + ...,   x < -1.

Для |x| > 1 этот ряд сходится к значению arctg(x), то есть
y(x) = arctg(x) при x < -1.
"""

from __future__ import annotations

import math
from typing import List, Tuple

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import THIN_SEPARATOR, fmt, read_float, read_int, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task1_series.py
    from common import THIN_SEPARATOR, fmt, read_float, read_int, show_results, show_task_header

TITLE = "Сумма членов функционального ряда (x < -1)"
STATEMENT = (
    "y(x) = -pi/2 + sum(n=0..inf) (-1)^(n+1) / ((2n+1) * x^(2n+1))\n"
    "     = -pi/2 - 1/x + 1/(3x^3) - 1/(5x^5) + ...,  при x < -1.\n"
    "Область сходимости: |x| > 1.\n"
    "Найти сумму ряда с заданной точностью eps.\n"
    "Примечание: сумма этого ряда равна arctg(x)."
)

TASK = (
    "Вариант 10, пункт 4: найти сумму функционального ряда\n"
    "y(x) = -pi/2 + sum(n=0..inf) (-1)^(n+1)/((2n+1)x^(2n+1)), x < -1."
)


def solve(x: float, eps: float, max_terms: int = 10000) -> Tuple[float, int, bool]:
    """Считает сумму ряда при x < -1 с точностью eps.

    Возвращает тройку: (сумма, число добавленных членов, признак сходимости).
    Цикл останавливается, когда очередной член по модулю не превосходит eps.
    """
    if x == 0:
        raise ValueError("x не может быть нулём: ряд определён при |x| > 1.")
    if abs(x) <= 1:
        raise ValueError("ряд сходится только при |x| > 1.")
    if eps <= 0:
        raise ValueError("точность eps должна быть положительной.")

    total = -math.pi / 2
    terms = 0
    power = x  # текущая степень x^(2n+1); при n = 0 это x^1
    converged = False

    for n in range(max_terms + 1):
        # Знаменатель степени умножаем на знак: при x < 0 он на каждой
        # итерации меняет знак, что и даёт чередование +, -, +, ...
        term = (-1) ** (n + 1) / ((2 * n + 1) * power)
        total += term
        terms += 1
        if abs(term) <= eps:
            converged = True
            break
        if n < max_terms:
            power *= x * x  # переходим от x^(2n+1) к x^(2n+3)

    return total, terms, converged


def run() -> None:
    """Диалог с пользователем: ввод x и eps, вывод суммы ряда."""
    show_task_header(1, TITLE, STATEMENT)
    x = read_float("Введите x (x < -1): ", less_than=-1)
    eps = read_float("Введите точность eps (например 0.0001): ", greater_than=0)

    total, terms, converged = solve(x, eps)
    lines: List[Tuple[str, object]] = [
        ("Сумма ряда", fmt(total, 6)),
        ("Учтено членов ряда", terms),
        ("Контроль arctg(x)", fmt(math.atan(x), 6)),
    ]
    show_results(lines)
    if not converged:
        print(f"  Внимание: за {terms} членов точность {fmt(eps)} не достигнута.")
    else:
        print(f"  Ряд сошёлся: очередной член стал меньше eps = {fmt(eps)}.")


if __name__ == "__main__":
    run()