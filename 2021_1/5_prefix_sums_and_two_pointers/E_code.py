from collections import defaultdict
from typing import Tuple


def find_minimal_segment_with_all_types(
        trees: list[int],
        k: int
) -> Tuple[int, int]:
    """
    Находит минимальный подотрезок массива, содержащий все K типов деревьев.

    Args:
        trees: Список типов деревьев
        k: Количество различных типов, которые должны присутствовать

    Returns:
        Кортеж (left, right) с 1-индексацией границ отрезка
    """
    n = len(trees)

    # Счетчик типов деревьев в текущем окне
    tree_count = defaultdict(int)

    # Количество уникальных типов в текущем окне
    unique_types = 0

    # Границы окна (0-индексированные)
    left = 0

    # Лучший найденный отрезок
    min_length = float('inf')
    best_left, best_right = 0, 0

    # Проходим по всем деревьям правым указателем
    for right in range(n):
        # Добавляем текущее дерево в окно
        tree_type = trees[right]

        if tree_count[tree_type] == 0:
            unique_types += 1
        tree_count[tree_type] += 1

        # Если собрали все типы, пытаемся сузить окно слева
        while unique_types == k:
            # Проверяем текущее окно
            current_length = right - left + 1
            if current_length < min_length:
                min_length = current_length
                best_left, best_right = left, right

            # Пытаемся удалить левый элемент
            left_tree_type = trees[left]
            tree_count[left_tree_type] -= 1

            if tree_count[left_tree_type] == 0:
                unique_types -= 1

            left += 1

    # Возвращаем с 1-индексацией
    return best_left + 1, best_right + 1


def main() -> None:
    """Основная функция для ввода/вывода данных."""
    try:
        # Чтение входных данных
        n, k = map(int, input().split())
        trees = list(map(int, input().split()))

        # Поиск минимального отрезка
        left, right = find_minimal_segment_with_all_types(trees, k)

        # Вывод результата
        print(left, right)

    except (ValueError, EOFError) as e:
        print(f"Ошибка ввода: {e}")
        return


if __name__ == "__main__":
    main()
