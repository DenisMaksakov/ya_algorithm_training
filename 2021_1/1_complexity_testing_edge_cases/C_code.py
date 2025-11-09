from typing import Iterator


def normalize_phone_number(phone_number: str) -> str:
    """
    Нормализует телефонный номер к стандартному формату.

    Args:
        phone_number: Исходный номер телефона в любом из допустимых форматов

    Returns:
        Нормализованный номер в формате '8XXXXXXXXXX' (11 цифр)
    """
    # Удаляем все нецифровые символы кроме '+' (нужен для определения формата)
    cleaned = ''.join(char for char in phone_number if char.isdigit() or char == '+')

    # Обрабатываем префиксы
    if cleaned.startswith('+7'):
        cleaned = '8' + cleaned[2:]
    elif cleaned.startswith('8'):
        cleaned = cleaned
    else:
        # Для номеров без кода добавляем код 495
        cleaned = '8495' + cleaned

    return cleaned


def check_phone_numbers(new_number: str, existing_numbers: list[str]) -> Iterator[str]:
    """
    Проверяет, совпадает ли новый номер с каждым из существующих номеров.

    Args:
        new_number: Номер, который нужно добавить
        existing_numbers: Список существующих номеров

    Yields:
        'YES' если номер совпадает, 'NO' в противном случае
    """
    normalized_new = normalize_phone_number(new_number)

    for existing_number in existing_numbers:
        normalized_existing = normalize_phone_number(existing_number)
        yield 'YES' if normalized_existing == normalized_new else 'NO'


def main() -> None:
    """Основная функция программы."""
    # Читаем входные данные
    new_number = input().strip()
    existing_numbers = [input().strip() for _ in range(3)]

    # Проверяем номера и выводим результат
    results = check_phone_numbers(new_number, existing_numbers)

    for result in results:
        print(result)


if __name__ == '__main__':
    main()