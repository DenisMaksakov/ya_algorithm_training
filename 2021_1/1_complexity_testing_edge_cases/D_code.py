def solve_square_root_equation(a: int, b: int, c: int) -> str | int:
    """
    Решает уравнение √(ax + b) = c в целых числах.

    Возвращает:
    - 'MANY SOLUTIONS' если решений бесконечно много
    - 'NO SOLUTION' если решений нет
    - целое число x, если решение одно
    - несколько целых чисел, если решений несколько (не предусмотрено условием, но для полноты)
    """
    # Случай: коэффициент a = 0
    if a == 0:
        # Уравнение превращается в √b = c
        if c < 0:
            # Квадратный корень не может быть отрицательным
            return "NO SOLUTION"
        elif c ** 2 == b:
            # Уравнение выполняется при любом x (бесконечно много решений)
            return "MANY SOLUTIONS"
        else:
            # Нет решений
            return "NO SOLUTION"

    # Случай: коэффициент a ≠ 0
    if c < 0:
        # Квадратный корень не может быть отрицательным
        return "NO SOLUTION"

    # Выражаем x из уравнения: ax + b = c^2 => x = (c^2 - b) / a
    numerator = c ** 2 - b

    # Проверяем, что числитель делится на знаменатель без остатка
    if numerator % a != 0:
        return "NO SOLUTION"

    x = numerator // a

    # Проверяем, что полученное x действительно является решением
    # (защита от возможных арифметических ошибок при делении)
    if a * x + b < 0:
        # Подкоренное выражение не может быть отрицательным
        return "NO SOLUTION"

    return x


def main() -> None:
    """Основная функция для ввода/вывода данных."""
    try:
        # Чтение входных данных
        a = int(input())
        b = int(input())
        c = int(input())

        # Решение уравнения
        result = solve_square_root_equation(a, b, c)

        # Вывод результата
        print(result)

    except ValueError:
        print("NO SOLUTION")  # Некорректный ввод
    except ZeroDivisionError:
        print("NO SOLUTION")  # Деление на ноль (если a = 0, но мы его обработали)


if __name__ == "__main__":
    main()