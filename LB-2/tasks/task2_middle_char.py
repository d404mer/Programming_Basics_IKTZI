"""Задание 2. Символ посередине строки (работа со срезами).

Условие: пользователь вводит с клавиатуры любую фразу (от 10 символов).
Используя срезы, вывести на экран символ, стоящий посередине этой фразы.
"""

from __future__ import annotations

from typing import List, Tuple

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import read_text, show_numbered_items, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task2_middle_char.py
    from common import read_text, show_numbered_items, show_results, show_task_header

TITLE = "Символ посередине фразы (срезы строк)"
STATEMENT = (
    "Введите любую фразу длиной от 10 символов.\n"
    "Программа найдёт символ, стоящий посередине фразы.\n"
    "Середина выделяется срезом:\n"
    "  начало = (len(s) - 1) // 2,  конец = len(s) - начало,\n"
    "  середина = s[начало:конец].\n"
    "Если длина чётная, в середине оказываются два символа - выводятся оба."
)

MIN_LENGTH = 10
#: Фраза для примера - 15 символов, середина одна (8-й символ).
EXAMPLE_PHRASE = "информатика это"


def middle_index(length: int) -> int:
    """Индекс «правого» среднего символа строки длиной length.

    Для нечётной длины это единственный центральный символ,
    для чётной - правый из двух центральных.
    """
    if length <= 0:
        raise ValueError("длина строки должна быть положительной.")
    return length // 2


def middle_slice(text: str) -> Tuple[str, int, int]:
    """Возвращает (средняя часть строки, начало среза, конец среза).

    Для нечётной длины это один символ, для чётной - два центральных.
    """
    start = (len(text) - 1) // 2
    end = len(text) - start
    return text[start:end], start, end


def middle_char(text: str) -> str:
    """Возвращает символ, стоящий посередине строки."""
    middle, _, _ = middle_slice(text)
    return middle[0]


def run() -> None:
    """Диалог с пользователем: ввод фразы и вывод её середины."""
    show_task_header(2, TITLE, STATEMENT)
    print(f"Пример: «{EXAMPLE_PHRASE}» -> {middle_char(EXAMPLE_PHRASE)}")
    print(f"       (длина фразы {len(EXAMPLE_PHRASE)}, "
          f"середина - символ номер {middle_index(len(EXAMPLE_PHRASE)) + 1})")
    print(f"{'-' * 64}")

    text = read_text(f"Введите фразу (от {MIN_LENGTH} символов): ", min_length=MIN_LENGTH)
    middle, start, end = middle_slice(text)
    index = middle_index(len(text))

    show_results(
        [
            ("Введённая фраза", f"«{text}»"),
            ("Длина фразы", f"{len(text)} символов"),
            ("Срез середины", f"текст[{start}:{end}]"),
            ("Символ посередине", f"«{middle}»"),
            ("Его номер в строке", index + 1),
        ]
    )
    if len(text) % 2 == 0:
        print("  Длина чётная: в середине два символа, показаны оба.")
    else:
        print("  Длина нечётная: середина - ровно один символ.")

    print()
    show_numbered_items(
        "Наглядная разбивка фразы",
        [
            f"начало:   «{text[:start]}» ({start} симв.)",
            f"середина: «{middle}» ({len(middle)} симв.)",
            f"конец:    «{text[end:]}» ({len(text) - end} симв.)",
        ],
    )
    print("  Начало и конец одинаковой длины, поэтому середина - ровно в центре фразы.")


if __name__ == "__main__":
    run()