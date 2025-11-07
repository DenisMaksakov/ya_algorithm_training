def main() -> None:
    """Основная функция программы."""
    room_temp, setpoint = map(int, input().split())
    mode = input().strip()

    result = calculate_temperature(room_temp, setpoint, mode)
    print(result)


def calculate_temperature(room_temp: int, setpoint: int, mode: str) -> int:
    """
    Вычисляет температуру в комнате через час работы кондиционера.

    Args:
        room_temp: Текущая температура в комнате
        setpoint: Желаемая температура, установленная на кондиционере
        mode: Режим работы кондиционера

    Returns:
        Температура, которая установится в комнате через час
    """
    # Все возможные режимы работы кондиционера
    MODES = {"freeze", "heat", "auto", "fan"}

    if mode not in MODES:
        raise ValueError(f"Неизвестный режим работы: {mode}")

    # Если температуры равны или режим вентиляции - температура не меняется
    if room_temp == setpoint or mode == "fan":
        return room_temp

    # Автоматический режим - всегда достигаем желаемой температуры
    if mode == "auto":
        return setpoint

    # Режим охлаждения - уменьшаем температуру только если нужно
    if mode == "freeze":
        return min(room_temp, setpoint)

    # Режим нагрева - увеличиваем температуру только если нужно
    if mode == "heat":
        return max(room_temp, setpoint)

    # На всякий случай возвращаем исходную температуру
    return room_temp


if __name__ == "__main__":
    main()