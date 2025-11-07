def main() -> None:
    """Основная функция программы."""
    a, b, c = read_triangle_sides()
    result = check_triangle_possible(a, b, c)
    print(result)


def read_triangle_sides() -> tuple[int, int, int]:
    """
    Читает три натуральных числа из стандартного ввода.

    Returns:
        Кортеж из трех целых чисел - сторон треугольника
    """
    a = int(input())
    b = int(input())
    c = int(input())
    return a, b, c


def check_triangle_possible(a: int, b: int, c: int) -> str:
    """
    Проверяет, возможно ли построить треугольник с заданными сторонами.

    Args:
        a, b, c: Длины сторон треугольника

    Returns:
        "YES" если треугольник возможен, "NO" в противном случае
    """
    # Проверяем неравенство треугольника: каждая сторона должна быть меньше суммы двух других
    if (a < b + c) and (b < a + c) and (c < a + b):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    main()
