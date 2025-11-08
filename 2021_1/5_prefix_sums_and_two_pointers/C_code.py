import sys
from typing import List, Tuple


def main() -> None:
    """Основная функция для обработки ввода и вычисления суммарной высоты подъемов."""
    # Чтение количества точек горной цепи
    N: int = int(sys.stdin.readline())
    mountain: List[Tuple[int, int]] = []

    # Чтение координат точек горной цепи
    for _ in range(N):
        xi, yi = map(int, sys.stdin.readline().split())
        mountain.append((xi, yi))

    # Чтение количества трасс
    M: int = int(sys.stdin.readline())
    routes: List[Tuple[int, int]] = []

    # Чтение описаний трасс
    for _ in range(M):
        si, fi = map(int, sys.stdin.readline().split())
        routes.append((si, fi))

    # Префиксные суммы для подъемов слева направо
    pref_forward: List[int] = [0] * N
    # Префиксные суммы для подъемов справа налево (спусков слева направо)
    pref_backward: List[int] = [0] * N

    # Заполнение префиксных массивов
    for i in range(1, N):
        x1, y1 = mountain[i - 1]
        x2, y2 = mountain[i]
        delta: int = y2 - y1

        # Для движения слева направо учитываем только подъемы (delta > 0)
        pref_forward[i] = pref_forward[i - 1] + max(0, delta)

        # Для движения справа налево учитываем спуски как подъемы в обратном направлении
        pref_backward[i] = pref_backward[i - 1] + max(0, -delta)

    # Обработка каждой трассы
    for start, end in routes:
        if start < end:
            # Движение слева направо
            result: int = pref_forward[end - 1] - pref_forward[start - 1]
        else:
            # Движение справа налево
            result = pref_backward[start - 1] - pref_backward[end - 1]

        print(result)


if __name__ == '__main__':
    main()
