def first_word(text):
    """ Поиск первого слова """
    words = re.findall(r"(?<!')[\w']+|[^\W\s]+", text)
    return words[0]

import re

# Тесты
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')