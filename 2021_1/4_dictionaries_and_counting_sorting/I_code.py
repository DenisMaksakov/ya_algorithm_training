import sys
from typing import Dict, List


def has_exactly_one_uppercase(word: str) -> bool:
    """Проверяет, содержит ли слово ровно одну заглавную букву."""
    return sum(char.isupper() for char in word) == 1


def build_accent_dict(n: int) -> Dict[str, List[str]]:
    """
    Строит словарь ударений из входных данных.

    Args:
        n: Количество слов в словаре

    Returns:
        Словарь, где ключ - слово в нижнем регистре,
        значение - список вариантов с ударениями
    """
    accent_dict: Dict[str, List[str]] = {}

    for _ in range(n):
        word = input().strip()
        lower_key = word.lower()

        if lower_key not in accent_dict:
            accent_dict[lower_key] = []
        accent_dict[lower_key].append(word)

    return accent_dict


def count_errors_in_text(accent_dict: Dict[str, List[str]], text: str) -> int:
    """
    Подсчитывает количество ошибок в тексте согласно словарю ударений.

    Args:
        accent_dict: Словарь ударений
        text: Текст для проверки

    Returns:
        Количество найденных ошибок
    """
    error_count = 0

    for word in text.split():
        lower_word = word.lower()

        if lower_word in accent_dict:
            # Слово есть в словаре - проверяем правильность ударения
            if word not in accent_dict[lower_word]:
                error_count += 1
        else:
            # Слова нет в словаре - проверяем ровно одно ударение
            if not has_exactly_one_uppercase(word):
                error_count += 1

    return error_count


def main() -> None:
    """Основная функция программы."""
    try:
        n = int(input().strip())
        accent_dict = build_accent_dict(n)
        text = input().strip()

        errors = count_errors_in_text(accent_dict, text)
        print(errors)

    except (ValueError, EOFError) as e:
        print(f"Ошибка ввода: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
