def popular_words (text, words):

    """
        Count how many times each word in 'words' appears in 'text' (case-insensitive).

        :param text: str, the input text to search within
        :param words: list of str, words to count in the text
        :return: dict, keys are words from 'words', values are their counts in the text
        """

    text = text.lower()
    worlds_split = text.split()
    result = {}

    for i in words:
        result[i] = worlds_split.count(i)
    return result

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')


