from typing import List, Tuple


def read_input() -> Tuple[List[int], List[int]]:
    """
    Чтение входных данных.
    Возвращает два списка: 
    - требования к мощности для каждого класса
    - минимальные цены для каждой возможной мощности
    """
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    m = int(input().strip())

    # Создаем массив для хранения минимальной цены для каждой мощности
    # Мощности от 1 до 1000 (по условию), заполняем большим значением
    min_price_for_power = [1001] * 1001  # 1001 - больше максимальной возможной цены 1000

    max_power = 0

    # Чтение данных о кондиционерах
    for _ in range(m):
        power, price = map(int, input().strip().split())
        max_power = max(max_power, power)

        # Сохраняем минимальную цену для данной мощности
        if price < min_price_for_power[power]:
            min_price_for_power[power] = price

    # Обратный проход для нахождения минимальной цены для мощностей больше или равных текущей
    for power in range(max_power, 0, -1):
        if min_price_for_power[power] < min_price_for_power[power - 1]:
            min_price_for_power[power - 1] = min_price_for_power[power]

    return a, min_price_for_power


def calculate_minimal_cost(power_requirements: List[int], min_prices: List[int]) -> int:
    """
    Вычисление минимальной суммарной стоимости кондиционеров.

    Args:
        power_requirements: требования к мощности для каждого класса
        min_prices: минимальные цены для каждой мощности

    Returns:
        Минимальная суммарная стоимость
    """
    total_cost = 0

    for requirement in power_requirements:
        # Для каждого класса берем минимальную цену кондиционера 
        # с мощностью не ниже требуемой
        total_cost += min_prices[requirement]

    return total_cost


def main() -> None:
    """
    Основная функция программы.
    """
    try:
        # Чтение входных данных
        power_requirements, min_prices = read_input()

        # Вычисление минимальной стоимости
        min_cost = calculate_minimal_cost(power_requirements, min_prices)

        # Вывод результата
        print(min_cost)

    except (ValueError, IndexError) as e:
        print(f"Ошибка обработки данных: {e}")


if __name__ == "__main__":
    main()
