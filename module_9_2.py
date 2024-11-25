first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Сборка списка длин строк из first_strings, длина строк не менее 5 символов
first_result = [len(string) for string in first_strings if len(string) >= 5]

# 2. Сборка списка пар слов (кортежей) одинаковой длины
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# 3. Сборка словаря, где ключ - строка, значение - длина строки (чётная длина)
third_result = {string: len(string) for string in first_strings + second_strings if len(string) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)


