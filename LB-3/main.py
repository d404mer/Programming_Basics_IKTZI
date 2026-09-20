"""Лабораторная работа №3. Строки, списки, множества, многомерные массивы.

Точка входа программы: показывает меню и запускает выбранное задание.
Решения самих заданий лежат в отдельных файлах пакета tasks/.

Запуск:
    python main.py
"""

from __future__ import annotations

from tasks import TASKS
from tasks.common import SEPARATOR, THIN_SEPARATOR, pause

WORK_TITLE = "Лабораторная работа №3. Строки, списки, множества, массивы"
EXIT_WORDS = {"0", "q", "й", "выход", "exit"}


def show_menu() -> None:
    """Печатает список заданий и номер пункта выхода."""
    print()
    print(SEPARATOR)
    print(WORK_TITLE)
    print(SEPARATOR)
    for number, title, _ in TASKS:
        print(f"  {number}. {title}")
    print()
    print("  0. Выход")
    print(THIN_SEPARATOR)


def dispatch(choice: str) -> None:
    """Запускает задание по выбранному номеру или сообщает о неверном вводе."""
    if not choice.isdigit() or not 1 <= int(choice) <= len(TASKS):
        print(f"      Пункта «{choice}» в меню нет. Введите число от 0 до {len(TASKS)}.")
        return

    number, title, action = TASKS[int(choice) - 1]
    try:
        action()
    except KeyboardInterrupt:
        print(f"\nВыполнение задания {number} прервано пользователем.")
    pause()


def main() -> int:
    """Основной цикл: меню -> задание -> снова меню, пока пользователь не выйдет."""
    print(WORK_TITLE)
    print("Выберите номер задания. В любой момент можно выйти пунктом 0.")

    while True:
        show_menu()
        try:
            choice = input("Введите номер задания: ").strip().lower()
        except EOFError:
            print()
            break

        if choice in EXIT_WORDS:
            break
        dispatch(choice)

    print("Работа завершена. До свидания!")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nВыход из программы (Ctrl+C).")
        raise SystemExit(130)