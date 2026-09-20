"""Общие вспомогательные функции для всех заданий лабораторной работы.

Здесь нет решений задач - только то, что делает интерфейс понятным:
  * show_task_header() - печатает номер, название и условие задания;
  * read_int() / read_float() - ввод чисел с проверкой и повторным запросом;
  * read_text() - ввод строки с проверкой длины;
  * read_int_list() - ввод нескольких целых чисел через запятую;
  * fmt() - аккуратный вывод вещественных чисел;
  * pause() - возврат в меню по нажатию Enter.
"""

from __future__ import annotations

import math
from typing import Callable, List, Optional, Sequence, Tuple

SEPARATOR = "=" * 64
THIN_SEPARATOR = "-" * 64

#: Префикс сообщений об ошибке ввода, чтобы они отличались от результата.
ERROR_PREFIX = "      Ошибка: "

#: Символы, которые пользователь может использовать как разделитель в списке.
LIST_SEPARATORS = ",;"


def show_task_header(number: int, title: str, statement: str) -> None:
    """Показывает заголовок и условие задания перед вводом данных."""
    print()
    print(SEPARATOR)
    print(f"Задание {number}. {title}")
    print(SEPARATOR)
    print(statement)
    print(THIN_SEPARATOR)


def fmt(value: float, digits: int = 4) -> str:
    """Форматирует число: округляет до `digits` знаков и убирает лишние нули."""
    rounded = round(float(value), digits)
    if rounded == int(rounded) and abs(rounded) < 1e15:
        return str(int(rounded))
    return f"{rounded:.{digits}f}".rstrip("0").rstrip(".")


def _bounds_error(
    value: float,
    greater_than: Optional[float],
    at_least: Optional[float],
    less_than: Optional[float],
    at_most: Optional[float],
) -> Optional[str]:
    """Возвращает текст ошибки, если число не попало в заданные границы."""
    if greater_than is not None and not value > greater_than:
        return f"значение должно быть больше {fmt(greater_than)}."
    if at_least is not None and not value >= at_least:
        return f"значение должно быть не меньше {fmt(at_least)}."
    if less_than is not None and not value < less_than:
        return f"значение должно быть меньше {fmt(less_than)}."
    if at_most is not None and not value <= at_most:
        return f"значение должно быть не больше {fmt(at_most)}."
    return None


def read_float(
    prompt: str,
    *,
    greater_than: Optional[float] = None,
    at_least: Optional[float] = None,
    less_than: Optional[float] = None,
    at_most: Optional[float] = None,
) -> float:
    """Запрашивает вещественное число и повторяет запрос, пока ввод не станет верным.

    Допускается ввод как с точкой (4.5), так и с запятой (4,5).
    """
    while True:
        text = input(prompt).strip().replace(",", ".")
        try:
            value = float(text)
        except ValueError:
            print(f"{ERROR_PREFIX}нужно ввести число, например 3 или 4.5.")
            continue
        if not math.isfinite(value):
            print(f"{ERROR_PREFIX}нужно ввести конечное число.")
            continue
        error = _bounds_error(value, greater_than, at_least, less_than, at_most)
        if error is not None:
            print(f"{ERROR_PREFIX}{error}")
            continue
        return value


def read_int(
    prompt: str,
    *,
    at_least: Optional[int] = None,
    at_most: Optional[int] = None,
) -> int:
    """Запрашивает целое число и повторяет запрос, пока ввод не станет верным."""
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print(f"{ERROR_PREFIX}нужно ввести целое число, например 123.")
            continue
        error = _bounds_error(value, None, at_least, None, at_most)
        if error is not None:
            print(f"{ERROR_PREFIX}{error}")
            continue
        return value


def read_text(
    prompt: str,
    *,
    min_length: int = 0,
    max_length: Optional[int] = None,
) -> str:
    """Запрашивает непустую строку и проверяет её длину."""
    while True:
        text = input(prompt)
        if not text.strip():
            print(f"{ERROR_PREFIX}строка не должна быть пустой.")
            continue
        if len(text) < min_length:
            print(
                f"{ERROR_PREFIX}строка должна содержать не меньше {min_length} символов, "
                f"а введено {len(text)}."
            )
            continue
        if max_length is not None and len(text) > max_length:
            print(f"{ERROR_PREFIX}строка должна содержать не больше {max_length} символов.")
            continue
        return text


def read_int_list(prompt: str, count: int) -> List[int]:
    """Запрашивает `count` целых чисел, введённых в одной строке через запятую."""
    while True:
        text = input(prompt).strip()
        if not text:
            print(f"{ERROR_PREFIX}нужно ввести числа через запятую, например: 1, 2, 3.")
            continue

        parts = text.replace(";", ",").split(",")
        if len(parts) != count:
            print(
                f"{ERROR_PREFIX}ожидается ровно {count} чисел через запятую, "
                f"а получено {len(parts)}."
            )
            continue

        values: List[int] = []
        bad_part: Optional[str] = None
        for part in parts:
            try:
                values.append(int(part.strip()))
            except ValueError:
                bad_part = part.strip()
                break
        if bad_part is not None:
            print(f"{ERROR_PREFIX}«{bad_part}» не является целым числом.")
            continue

        return values


def show_results(lines) -> None:
    """Печатает блок результатов: каждая строка - это (подпись, значение).

    Подписи выравниваются по самой длинной, поэтому столбец значений
    получается ровным независимо от текста в задании.
    """
    rows = list(lines)
    print(THIN_SEPARATOR)
    print("Результат:")
    if rows:
        width = max(len(str(label)) for label, _ in rows)
        for label, value in rows:
            print(f"  {str(label).ljust(width)} = {value}")
    print(THIN_SEPARATOR)


def show_numbered_items(title: str, items: Sequence[str]) -> None:
    """Печатает список пронумерованных строк (например, элементы списка)."""
    print(f"{title}:")
    for index, item in enumerate(items, start=1):
        print(f"  {index}. {item}")


def pause(text: str = "Нажмите Enter, чтобы вернуться в меню...") -> None:
    """Ждёт нажатия Enter перед возвратом в меню."""
    print()
    try:
        input(text)
    except EOFError:
        print()


# Тип элемента меню: (номер, название, функция запуска задания).
TaskItem = Tuple[int, str, Callable[[], None]]