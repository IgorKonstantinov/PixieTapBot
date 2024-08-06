import re

def increment_string_number(s):
    # Используем регулярное выражение для поиска последней последовательности цифр
    match = re.search(r'(\d+)$', s)
    if match:
        # Извлекаем цифры и увеличиваем их на 1
        number = int(match.group(1))
        new_number = number + 1
        # Заменяем старое число на новое в строке
        return s[:match.start(1)] + str(new_number)
    else:
        # Если цифры в конце строки нет, ничего не меняем
        return s

