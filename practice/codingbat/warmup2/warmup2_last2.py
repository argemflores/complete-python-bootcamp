# last2

# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

def last2(str):
    found_count = 0
    
    if len(str) < 2:
        return found_count
    
    last2chars = str[-2:]
    
    for i, s in enumerate(str):
        if last2chars in str[i:i+2]:
            found_count += 1
    
    return found_count-1
