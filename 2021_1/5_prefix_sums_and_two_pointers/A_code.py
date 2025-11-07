import sys
from typing import Tuple, List


def find_best_combination(shirts: List[int], pants: List[int]) -> Tuple[int, int]:
    """
    Находит пару майка-штаны с минимальной разницей в цвете.

    Args:
        shirts: Отсортированный список цветов маек
        pants: Отсортированный список цветов штанов

    Returns:
        Кортеж (цвет_майки, цвет_штанов) с минимальной разницей
    """
    shirt_idx, pants_idx = 0, 0
    best_shirt_idx, best_pants_idx = 0, 0
    min_difference = abs(shirts[0] - pants[0])

    # Проходим по обоим спискам одновременно
    while shirt_idx < len(shirts) and pants_idx < len(pants):
        current_difference = abs(shirts[shirt_idx] - pants[pants_idx])

        # Обновляем лучшую пару, если нашли лучше
        if current_difference < min_difference:
            min_difference = current_difference
            best_shirt_idx, best_pants_idx = shirt_idx, pants_idx

        # Двигаем указатель того списка, где текущий элемент меньше
        if shirts[shirt_idx] < pants[pants_idx]:
            shirt_idx += 1
        else:
            pants_idx += 1

    return shirts[best_shirt_idx], pants[best_pants_idx]


def read_input() -> Tuple[List[int], List[int]]:
    """
    Читает входные данные из стандартного ввода.

    Returns:
        Кортеж (список_маек, список_штанов)
    """
    n = int(sys.stdin.readline().strip())
    shirts = list(map(int, sys.stdin.readline().strip().split()))

    m = int(sys.stdin.readline().strip())
    pants = list(map(int, sys.stdin.readline().strip().split()))

    return shirts, pants


def main() -> None:
    """Основная функция программы."""
    shirts, pants = read_input()
    best_shirt, best_pants = find_best_combination(shirts, pants)
    print(best_shirt, best_pants)


if __name__ == '__main__':
    main()
