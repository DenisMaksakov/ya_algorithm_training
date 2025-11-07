import sys
from string import ascii_letters, digits
from typing import Set, Dict, List, Tuple


def is_valid_identifier(word: str, can_start_with_digit: str) -> bool:
    """
    Проверяет, является ли слово валидным идентификатором.

    Args:
        word: Слово для проверки
        can_start_with_digit: 'yes' если идентификатор может начинаться с цифры, иначе 'no'

    Returns:
        True если слово является валидным идентификатором, иначе False
    """
    if not word:
        return False

    # Проверка начала идентификатора
    if can_start_with_digit == 'no' and word[0].isdigit():
        return False

    # Проверка что есть хотя бы один не-цифровой символ
    has_non_digit = any(char not in digits for char in word)
    if not has_non_digit:
        return False

    # Проверка что все символы допустимы
    allowed_chars = ascii_letters + digits + '_'
    return all(char in allowed_chars for char in word)


def preprocess_code(code: str, case_sensitive: str) -> str:
    """
    Предобрабатывает код программы: приводит к нижнему регистру если нужно
    и заменяет пунктуацию на пробелы.

    Args:
        code: Исходный код программы
        case_sensitive: 'yes' если регистр важен, иначе 'no'

    Returns:
        Предобработанный код
    """
    if case_sensitive == 'no':
        code = code.lower()

    # Заменяем пунктуацию на пробелы
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~'
    translation_table = str.maketrans(punctuation, ' ' * len(punctuation))
    return code.translate(translation_table)


def read_keywords(n: int, case_sensitive: str) -> Set[str]:
    """
    Читает ключевые слова из входных данных.

    Args:
        n: Количество ключевых слов
        case_sensitive: 'yes' если регистр важен, иначе 'no'

    Returns:
        Множество ключевых слов
    """
    keywords: Set[str] = set()
    if n > 0:
        for _ in range(n):
            keyword = sys.stdin.readline().strip()
            if case_sensitive == 'no':
                keyword = keyword.lower()
            keywords.add(keyword)
    return keywords


def find_most_frequent_identifier(
        code: str,
        keywords: Set[str],
        can_start_with_digit: str
) -> str:
    """
    Находит наиболее часто встречающийся идентификатор в коде.

    Args:
        code: Предобработанный код программы
        keywords: Множество ключевых слов
        can_start_with_digit: 'yes' если идентификатор может начинаться с цифры, иначе 'no'

    Returns:
        Наиболее часто встречающийся идентификатор
    """
    identifier_counts: Dict[str, int] = {}
    first_occurrence: Dict[str, int] = {}

    words = code.split()

    for position, word in enumerate(words):
        # Пропускаем ключевые слова и невалидные идентификаторы
        if word in keywords or not is_valid_identifier(word, can_start_with_digit):
            continue

        # Обновляем счетчик
        identifier_counts[word] = identifier_counts.get(word, 0) + 1

        # Запоминаем первую позицию
        if word not in first_occurrence:
            first_occurrence[word] = position

    if not identifier_counts:
        raise ValueError("В программе не найдено валидных идентификаторов")

    # Находим максимальную частоту
    max_count = max(identifier_counts.values())

    # Фильтруем идентификаторы с максимальной частотой
    most_frequent_identifiers = [
        identifier for identifier, count in identifier_counts.items()
        if count == max_count
    ]

    # Сортируем по первой позиции вхождения
    return min(most_frequent_identifiers, key=lambda id: first_occurrence[id])


def main() -> None:
    """Основная функция программы."""
    # Чтение параметров языка
    first_line = sys.stdin.readline().split()
    n_keywords = int(first_line[0])
    case_sensitive = first_line[1]  # 'yes' или 'no'
    can_start_with_digit = first_line[2]  # 'yes' или 'no'

    # Чтение ключевых слов
    keywords = read_keywords(n_keywords, case_sensitive)

    # Чтение и предобработка кода
    raw_code = sys.stdin.read()
    processed_code = preprocess_code(raw_code, case_sensitive)

    # Поиск наиболее частого идентификатора
    result = find_most_frequent_identifier(
        processed_code, keywords, can_start_with_digit
    )

    print(result)


if __name__ == '__main__':
    main()