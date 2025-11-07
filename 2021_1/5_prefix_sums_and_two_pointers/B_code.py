import sys
from typing import List, Tuple


def main() -> None:
    """Основная функция программы."""
    n, k = read_input()
    car_numbers = read_car_numbers(n)
    result = count_subarrays_with_sum(car_numbers, k)
    print(result)


def read_input() -> Tuple[int, int]:
    """
    Читает N и K из стандартного ввода.

    Returns:
        Кортеж (N, K) - количество машин и целевая сумма
    """
    return tuple(map(int, sys.stdin.readline().split()))  # type: ignore


def read_car_numbers(n: int) -> List[int]:
    """
    Читает номера машин из стандартного ввода.

    Args:
        n: Количество номеров для чтения

    Returns:
        Список номеров машин
    """
    return list(map(int, sys.stdin.readline().split()))


def count_subarrays_with_sum(car_numbers: List[int], k: int) -> int:
    """
    Подсчитывает количество подмассивов с суммой равной K.

    Args:
        car_numbers: Список номеров машин
        k: Целевая сумма

    Returns:
        Количество подмассивов с суммой k
    """
    n = len(car_numbers)
    prefix_sum = [0] * (n + 1)

    # Строим массив префиксных сумм
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + car_numbers[i]

    count = 0
    right = 0

    # Используем метод двух указателей
    for left in range(n):
        # Сдвигаем правый указатель, пока сумма меньше K
        while right < n and prefix_sum[right + 1] - prefix_sum[left] < k:
            right += 1

        # Проверяем, равна ли сумма K
        if right < n and prefix_sum[right + 1] - prefix_sum[left] == k:
            count += 1

        # Если right отстал от left, двигаем его вперед
        if right < left:
            right = left

    return count


if __name__ == '__main__':
    main()