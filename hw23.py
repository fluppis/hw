def popular_words(text, words):
    text_words= text.lower().split()
    word_count = {}
    for k in words:
        count = text_words.count(k.lower())
        word_count[k] = count
    return word_count

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')