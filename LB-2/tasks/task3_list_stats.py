"""Задание 3. Статистика по списку из 6 элементов (вариант 10).

Условие: пользователь вводит с клавиатуры последовательно (через запятые)
6 целых чисел - элементов списка. Требуется:
  1) вывести на экран 4-й элемент;
  2) вывести все элементы, начиная с 3-го;
  3) вывести все элементы в обратном порядке;
  4) найти сумму элементов;
  5) найти среднее арифметическое элементов.
"""

from __future__ import annotations

from typing import List, Tuple

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import THIN_SEPARATOR, read_int_list, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task3_list_stats.py
    from common import THIN_SEPARATOR, read_int_list, show_results, show_task_header

TITLE = "Статистика по списку из 6 элементов"
STATEMENT = (
    "Введите через запятую 6 целых чисел - элементов списка.\n"
    "Например: 4, 8, 15, 16, 23, 42\n"
    "Программа выведет:\n"
    "  1) 4-й элемент списка;\n"
    "  2) все элементы, начиная с 3-го;\n"
    "  3) все элементы в обратном порядке;\n"
    "  4) сумму и среднее арифметическое элементов."
)

COUNT = 6
#: Пример для подсказки пользователю.
EXAMPLE = "4, 8, 15, 16, 23, 42"


def solve(numbers: List[int]) -> dict:
    """Считает статистику по списку чисел.

    Возвращает словарь с четвёртым элементом, срезом с 3-го элемента,
    обратным списком, суммой и средним арифметическим.
    """
    if len(numbers) != COUNT:
        raise ValueError(f"в списке должно быть ровно {COUNT} элементов.")

    total = sum(numbers)
    return {
        "fourth": numbers[3],
        "from_third": numbers[2:],
        "reversed": numbers[::-1],
        "total": total,
        "average": total / len(numbers),
    }


def run() -> None:
    """Диалог с пользователем: ввод списка и вывод статистики."""
    show_task_header(3, TITLE, STATEMENT)
    print(f"Пример ввода: {EXAMPLE}")
    print(THIN_SEPARATOR)

    numbers = read_int_list(f"Введите {COUNT} чисел через запятую: ", count=COUNT)
    print(THIN_SEPARATOR)
    print("Введённый список (индекс -> значение):")
    for index, value in enumerate(numbers):
        print(f"  [{index}] = {value}")

    stats = solve(numbers)
    show_results(
        [
            ("4-й элемент (индекс 3)", stats["fourth"]),
            ("Элементы с 3-го по 6-й", stats["from_third"]),
            ("Элементы в обратном порядке", stats["reversed"]),
            ("Сумма элементов", stats["total"]),
            ("Среднее арифметическое", round(stats["average"], 4)),
        ]
    )
    print(f"  Числа после 4-го выведены срезом numbers[3:6]: {stats['from_third']}.")
    print(f"  Обратный порядок получен срезом numbers[::-1]: {stats['reversed']}.")


if __name__ == "__main__":
    run()