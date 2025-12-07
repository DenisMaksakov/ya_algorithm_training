import sys
from typing import List, Tuple, Optional, Set


def read_input() -> Tuple[int, int, int, int, int]:
    """Чтение входных данных."""
    data = sys.stdin.readline().strip().split()
    if len(data) != 5:
        raise ValueError(f"Ожидается 5 чисел, получено {len(data)}")

    K1, M, K2, P2, N2 = map(int, data)
    return K1, M, K2, P2, N2


def get_possible_flats_per_floor(K2: int, P2: int, N2: int, M: int) -> List[int]:
    """
    Определение возможных значений квартир на этаже (Xi),
    удовлетворяющих заданным условиям.

    Args:
        K2: номер известной квартиры
        P2: известный подъезд
        N2: известный этаж
        M: количество этажей в доме

    Returns:
        Список возможных значений квартир на этаже
    """
    if N2 > M:
        return []

    # Вычисляем порядковый номер квартиры в доме от начала
    # (P2 - 1) * M + N2 - это порядковый номер этажа от начала дома
    # Умножаем на Xi - получаем общее количество квартир до этой
    target_floor_position = (P2 - 1) * M + N2

    possible_xi_values = []
    max_value = max(K2, 10 ** 6)  # Берем максимальное возможное значение

    for xi in range(1, max_value + 1):
        # Проверяем, на каком этаже будет квартира K2 при данном xi
        # ceil(K2 / xi) - порядковый номер этажа от начала дома
        calculated_floor = (K2 + xi - 1) // xi

        if calculated_floor == target_floor_position:
            possible_xi_values.append(xi)

    return possible_xi_values


def calculate_entrance(K1: int, M: int, flats_per_floor: int) -> int:
    """
    Вычисление номера подъезда для квартиры K1.

    Args:
        K1: номер квартиры
        M: количество этажей в доме
        flats_per_floor: количество квартир на этаже

    Returns:
        Номер подъезда (начинается с 1)
    """
    flats_per_entrance = M * flats_per_floor
    entrance = (K1 - 1) // flats_per_entrance + 1
    return entrance


def calculate_floor(K1: int, M: int, flats_per_floor: int) -> int:
    """
    Вычисление номера этажа для квартиры K1.

    Args:
        K1: номер квартиры
        M: количество этажей в доме
        flats_per_floor: количество квартир на этаже

    Returns:
        Номер этажа (начинается с 1)
    """
    flats_per_entrance = M * flats_per_floor
    # Номер квартиры относительно начала подъезда (от 0 до flats_per_entrance-1)
    flat_in_entrance = (K1 - 1) % flats_per_entrance
    floor_in_entrance = flat_in_entrance // flats_per_floor + 1
    return floor_in_entrance


def analyze_solution(possible_flats_per_floor: List[int],
                     K1: int, M: int) -> Tuple[int, int]:
    """
    Анализ возможных решений и определение итоговых значений.

    Args:
        possible_flats_per_floor: список возможных значений квартир на этаже
        K1: номер квартиры, для которой нужно найти подъезд и этаж
        M: количество этажей в доме

    Returns:
        Кортеж (P1, N1) - номер подъезда и этажа
    """
    if not possible_flats_per_floor:
        return -1, -1

    entrance_set: Set[int] = set()
    floor_set: Set[int] = set()

    for xi in possible_flats_per_floor:
        entrance_set.add(calculate_entrance(K1, M, xi))
        floor_set.add(calculate_floor(K1, M, xi))

    # Определяем результат согласно условию задачи
    P1 = entrance_set.pop() if len(entrance_set) == 1 else 0
    N1 = floor_set.pop() if len(floor_set) == 1 else 0

    return P1, N1


def validate_input(K1: int, M: int, K2: int, P2: int, N2: int) -> bool:
    """
    Проверка корректности входных данных.

    Args:
        K1, M, K2, P2, N2: входные параметры

    Returns:
        True если данные корректны, иначе False
    """
    if any(val <= 0 for val in (K1, M, K2, P2, N2)):
        return False

    if any(val > 10 ** 6 for val in (K1, M, K2, P2, N2)):
        return False

    if N2 > M or P2 < 1:
        return False

    return True


def optimize_flats_per_floor_search(K2: int, P2: int, N2: int, M: int) -> List[int]:
    """
    Оптимизированный поиск возможных значений квартир на этаже.
    Вместо перебора всех значений до max(K2, 10^6) используем математические ограничения.

    Args:
        K2: номер известной квартиры
        P2: известный подъезд
        N2: известный этаж
        M: количество этажей в доме

    Returns:
        Список возможных значений квартир на этаже
    """
    if N2 > M:
        return []

    target_floor_position = (P2 - 1) * M + N2

    # Выводим границы для xi из условия:
    # (target_floor_position - 1) * xi < K2 ≤ target_floor_position * xi

    min_xi = (K2 - 1) // target_floor_position + 1
    max_xi = K2 // (target_floor_position - 1) if target_floor_position > 1 else 10 ** 6

    # Учитываем, что xi должно быть целым положительным числом
    min_xi = max(1, min_xi)
    max_xi = min(max_xi, 10 ** 6)

    possible_xi_values = []

    for xi in range(min_xi, max_xi + 1):
        calculated_floor = (K2 + xi - 1) // xi
        if calculated_floor == target_floor_position:
            possible_xi_values.append(xi)

    return possible_xi_values


def solve() -> None:
    """Основная функция решения задачи."""
    try:
        # Чтение входных данных
        K1, M, K2, P2, N2 = read_input()

        # Проверка корректности данных
        if not validate_input(K1, M, K2, P2, N2):
            print(-1, -1)
            return

        # Поиск возможных значений квартир на этаже
        possible_flats_per_floor = optimize_flats_per_floor_search(K2, P2, N2, M)

        # Анализ решений и вывод результата
        P1, N1 = analyze_solution(possible_flats_per_floor, K1, M)
        print(P1, N1)

    except ValueError as e:
        print(f"Ошибка ввода: {e}", file=sys.stderr)
        print(-1, -1)
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}", file=sys.stderr)
        print(-1, -1)


def solve_simple() -> None:
    """Упрощенная версия решения (ближе к оригиналу)."""
    K1, M, K2, P2, N2 = map(int, sys.stdin.readline().split())

    # Определяем возможные значения квартир на этаже
    x_max = max(K1, K2)
    possible_x: List[int] = []

    for xi in range(1, x_max + 1):
        # ceil(K2 / xi) == (P2 - 1) * M + N2
        if (K2 + xi - 1) // xi == (P2 - 1) * M + N2:
            possible_x.append(xi)

    # Проверка на противоречивость данных
    if not possible_x or N2 > M:
        print(-1, -1)
        return

    # Вычисление возможных значений P1 и N1
    entrances: Set[int] = set()
    floors: Set[int] = set()

    for xi in possible_x:
        # Вычисление подъезда
        entrance = (K1 - 1) // (M * xi) + 1
        entrances.add(entrance)

        # Вычисление этажа
        flat_in_entrance = (K1 - 1) % (M * xi)
        floor_in_entrance = flat_in_entrance // xi + 1
        floors.add(floor_in_entrance)

    # Формирование ответа согласно условию
    P1 = entrances.pop() if len(entrances) == 1 else 0
    N1 = floors.pop() if len(floors) == 1 else 0

    print(P1, N1)


if __name__ == "__main__":
    # Выбираем версию решения
    # solve()  # Улучшенная версия с оптимизациями
    solve_simple()  # Более простая версия, ближе к оригиналу