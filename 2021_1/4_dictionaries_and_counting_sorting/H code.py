import sys
from typing import Dict


def main() -> None:
    """Основная функция для подсчета вхождений слова W в последовательность S."""
    # Чтение размеров данных
    word_length, sequence_length = map(int, input().split())

    # Чтение шаблона слова и анализируемой последовательности
    word_pattern = input().strip()
    character_sequence = input().strip()

    # Создание частотного словаря для шаблона слова
    pattern_frequency: Dict[str, int] = {}
    for char in word_pattern:
        pattern_frequency[char] = pattern_frequency.get(char, 0) + 1

    # Словарь для отслеживания частот в текущем окне
    current_window_frequency: Dict[str, int] = {}
    match_count = 0

    # Обработка последовательности скользящим окном
    for right_index in range(sequence_length):
        current_char = character_sequence[right_index]
        current_window_frequency[current_char] = current_window_frequency.get(current_char, 0) + 1

        # Пропускаем проверку, пока окно не достигнет нужного размера
        if right_index < word_length - 1:
            continue

        # Проверяем совпадение частот
        if current_window_frequency == pattern_frequency:
            match_count += 1

        # Удаляем крайний левый символ из окна
        left_char = character_sequence[right_index - word_length + 1]
        current_window_frequency[left_char] -= 1
        if current_window_frequency[left_char] == 0:
            del current_window_frequency[left_char]

    print(match_count)


if __name__ == '__main__':
    main()
