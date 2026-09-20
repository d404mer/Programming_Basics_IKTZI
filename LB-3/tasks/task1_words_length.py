"""Задание 1. Длина самого короткого и самого длинного слова в строке.

Условие: дана строка, заканчивающаяся точкой.
Найти длину самого короткого слова и самого длинного слова.
"""

from __future__ import annotations

from typing import List, Tuple

try:  # запуск из main.py (модуль входит в пакет tasks)
    from .common import read_text, show_numbered_items, show_results, show_task_header
except ImportError:  # прямой запуск файла: python task1_words_length.py
    from common import read_text, show_numbered_items, show_results, show_task_header

TITLE = "Самое короткое и самое длинное слово в строке"
STATEMENT = (
    "Введите строку, заканчивающуюся точкой.\n"
    "Программа найдёт длину самого короткого и самого длинного слова.\n"
    "Слова разделяются пробелами; точка входит в последнее слово\n"
    "и при подсчёте длины не учитывается."
)

#: Строка-пример для подсказки (в ней 4 слова разной длины).
EXAMPLE = "Программирование это интересно и полезно."


def split_words(text: str) -> List[str]:
    """Разбивает строку на слова, отбрасывая пробелы и завершающую точку."""
    # Последняя точка - знак конца строки, а не часть слова.
    cleaned = text.rstrip()
    if cleaned.endswith("."):
        cleaned = cleaned[:-1]
    return cleaned.split()


def solve(text: str) -> dict:
    """Возвращает слова разной длины и длины самого короткого и самого длинного.

    Если подходящих слов несколько (например, несколько слов минимальной длины),
    возвращаются все - в примере это сделано, чтобы результат был нагляднее.
    """
    words = split_words(text)
    if not words:
        raise ValueError("в строке не найдено ни одного слова.")

    lengths = [len(word) for word in words]
    shortest = min(lengths)
    longest = max(lengths)

    return {
        "words": words,
        "lengths": lengths,
        "shortest_length": shortest,
        "longest_length": longest,
        "shortest_words": [w for w in words if len(w) == shortest],
        "longest_words": [w for w in words if len(w) == longest],
    }


def run() -> None:
    """Диалог с пользователем: ввод строки и вывод длин слов."""
    show_task_header(1, TITLE, STATEMENT)
    print(f"Пример: «{EXAMPLE}»")

    text = read_text("Введите строку, заканчивающуюся точкой: ")
    if not text.rstrip().endswith("."):
        print("      Примечание: строка не заканчивается точкой - обработана как есть.")

    result = solve(text)
    show_results(
        [
            ("Всего слов", len(result["words"])),
            ("Длина самого короткого слова", result["shortest_length"]),
            ("Длина самого длинного слова", result["longest_length"]),
            ("Самое короткое слово", ", ".join(result["shortest_words"])),
            ("Самое длинное слово", ", ".join(result["longest_words"])),
        ]
    )
    print("Слова и их длины (в порядке появления):")
    for index, (word, length) in enumerate(zip(result["words"], result["lengths"]), start=1):
        print(f"  {index:>2}. «{word}» - {length} симв.")


if __name__ == "__main__":
    run()