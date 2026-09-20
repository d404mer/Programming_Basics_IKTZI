"""Задание 2. Площади двух концентрических кругов и кольца между ними.

Условие: даны два круга с общим центром и радиусами R1 и R2 (R1 > R2).
Найти площади этих кругов S1 и S2, а также площадь S3 кольца,
внешний радиус которого равен R1, а внутренний - R2.
"""

from __future__ import annotations

import math

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import fmt, read_float, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task2_circles.py
    from common import fmt, read_float, show_results, show_task_header

TITLE = "Два концентрических круга и кольцо между ними"
STATEMENT = (
    "Даны два круга с общим центром и радиусами R1 и R2, причём R1 > R2.\n"
    "Найти площади кругов S1, S2 и площадь кольца S3.\n"
    "Формулы: S1 = pi*R1^2,  S2 = pi*R2^2,  S3 = S1 - S2."
)


def solve(r1: float, r2: float) -> tuple:
    """Возвращает тройку (S1, S2, S3) для радиусов r1 > r2."""
    s1 = math.pi * r1 * r1
    s2 = math.pi * r2 * r2
    s3 = s1 - s2
    return s1, s2, s3


def run() -> None:
    """Диалог с пользователем: ввод радиусов и вывод результата."""
    show_task_header(2, TITLE, STATEMENT)
    r1 = read_float("Введите внешний радиус R1 (R1 > 0): ", greater_than=0)
    # Второе ограничение гарантирует выполнение условия R1 > R2.
    r2 = read_float(
        f"Введите внутренний радиус R2 (0 < R2 < {fmt(r1)}): ",
        greater_than=0,
        less_than=r1,
    )

    s1, s2, s3 = solve(r1, r2)
    show_results(
        [
            ("Площадь круга S1", fmt(s1)),
            ("Площадь круга S2", fmt(s2)),
            ("Площадь кольца S3", fmt(s3)),
        ]
    )


if __name__ == "__main__":
    run()
