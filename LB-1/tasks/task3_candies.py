"""Задание 3. Цена килограмма конфет и сравнение стоимости.

Условие: известно, что X кг шоколадных конфет стоит A рублей,
а Y кг ирисок стоит B рублей. Определить, сколько стоит 1 кг шоколадных
конфет, 1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок.
"""

from __future__ import annotations

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import fmt, read_float, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task3_candies.py
    from common import fmt, read_float, show_results, show_task_header

TITLE = "Стоимость 1 кг конфет и ирисок, сравнение цен"
STATEMENT = (
    "X кг шоколадных конфет стоит A рублей, Y кг ирисок стоит B рублей.\n"
    "Найти цену 1 кг шоколадных конфет, цену 1 кг ирисок\n"
    "и определить, во сколько раз шоколадные конфеты дороже ирисок.\n"
    "Формулы: p1 = A / X,  p2 = B / Y,  k = p1 / p2."
)


def solve(x: float, a: float, y: float, b: float) -> tuple:
    """Возвращает тройку (цена 1 кг конфет, цена 1 кг ирисок, отношение цен)."""
    price_chocolate = a / x
    price_toffee = b / y
    ratio = price_chocolate / price_toffee
    return price_chocolate, price_toffee, ratio


def run() -> None:
    """Диалог с пользователем: ввод масс и цен, вывод результата."""
    show_task_header(3, TITLE, STATEMENT)
    x = read_float("Введите массу шоколадных конфет X, кг (X > 0): ", greater_than=0)
    a = read_float(f"Введите стоимость A рублей за {fmt(x)} кг конфет (A >= 0): ", at_least=0)
    y = read_float("Введите массу ирисок Y, кг (Y > 0): ", greater_than=0)
    # Цена ирисок должна быть ненулевой, иначе отношение цен не определено.
    b = read_float(f"Введите стоимость B рублей за {fmt(y)} кг ирисок (B > 0): ", greater_than=0)

    price_chocolate, price_toffee, ratio = solve(x, a, y, b)
    show_results(
        [
            ("1 кг шоколадных конфет", f"{fmt(price_chocolate)} руб."),
            ("1 кг ирисок", f"{fmt(price_toffee)} руб."),
            ("Отношение цен", f"{fmt(ratio)} раза"),
        ]
    )
    if ratio >= 1:
        print(f"  Шоколадные конфеты дороже ирисок в {fmt(ratio)} раза.")
    else:
        print(f"  Шоколадные конфеты дешевле ирисок в {fmt(1 / ratio)} раза.")


if __name__ == "__main__":
    run()
