import sys
from typing import List, Tuple


def count_valid_pairs(n: int, r: int, monuments: List[int]) -> int:
    """
    Подсчитывает количество пар памятников, расстояние между которыми превышает r.

    Args:
        n: Количество памятников
        r: Максимальное расстояние, на котором мальчики могут увидеть друг друга
        monuments: Отсортированный список расстояний до памятников

    Returns:
        Количество валидных пар памятников
    """
    count = 0
    left_ptr = 0
    right_ptr = 1

    while left_ptr < n - 1 and right_ptr < n:
        distance = monuments[right_ptr] - monuments[left_ptr]

        if distance > r:
            # Все памятники справа от right_ptr также будут удовлетворять условию
            count += n - right_ptr
            left_ptr += 1
        else:
            right_ptr += 1

        # Поддерживаем правильный порядок указателей
        if right_ptr <= left_ptr:
            right_ptr = left_ptr + 1

    return count


def main() -> None:
    """Основная функция программы."""
    # Чтение входных данных
    n, r = map(int, sys.stdin.readline().split())
    monuments = list(map(int, sys.stdin.readline().split()))

    # Подсчет результата
    result = count_valid_pairs(n, r, monuments)

    # Вывод результата
    print(result)


if __name__ == '__main__':
    main()
