def myfunc(word):
    new_word = ''
    
    for i, letter in enumerate(word):
        if i % 2 == 0:
            new_word += letter.upper()
        else:
            new_word += letter.lower()
    
    return new_word