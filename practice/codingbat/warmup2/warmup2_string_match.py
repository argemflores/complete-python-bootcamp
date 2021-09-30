# string_match

# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0

def string_match(a, b):
    same_count_2 = 0
    
    # get the shorter number of characters between the two strings
    min_len = min(len(a), len(b))
    
    # iterate through the shorter string
    for i in range(0, min_len - 1):
        # count 1 if 2 consecutive letters in both strings match
        if a[i] == b[i] and a[i+1] == b[i+1]:
            same_count_2 += 1
    
    return same_count_2
